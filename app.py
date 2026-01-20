from flask import Flask, render_template, request, jsonify
from datetime import datetime
import requests
import json
import os
from typing import Dict, List
import hashlib

app = Flask(__name__)

# Codexa API Configuration
CODEXA_API_BASE = os.getenv('CODEXA_API_BASE', 'https://codexa-engine-func.azurewebsites.net/api')
CODEXA_FUNCTION_KEY = os.getenv('CODEXA_FUNCTION_KEY', '')

# Store recent analyses in memory (in production, use Cosmos DB)
recent_analyses = []

@app.route('/')
def index():
    """Main dashboard"""
    return render_template('index.html', analyses=recent_analyses[:10])

@app.route('/analyze', methods=['POST'])
def analyze_code():
    """Analyze code using Codexa AI engine"""
    try:
        data = request.get_json()
        code = data.get('code', '')
        language = data.get('language', 'python')
        repository = data.get('repository', 'manual-submission')
        
        if not code:
            return jsonify({'error': 'Code is required'}), 400
        
        # Call Codexa Analysis API
        analysis_result = call_codexa_analyze(code, language)
        
        # Call Codexa Governance API if repository provided
        governance_result = None
        if repository != 'manual-submission':
            governance_result = call_codexa_governance(repository, ['main.py'])
        
        # Generate recommendations using AI
        recommendations = generate_ai_recommendations(
            analysis_result, 
            code, 
            language
        )
        
        # Store result
        result = {
            'id': hashlib.md5(code.encode()).hexdigest()[:8],
            'timestamp': datetime.utcnow().isoformat(),
            'language': language,
            'repository': repository,
            'analysis': analysis_result,
            'governance': governance_result,
            'recommendations': recommendations,
            'code_preview': code[:200] + '...' if len(code) > 200 else code
        }
        
        recent_analyses.insert(0, result)
        if len(recent_analyses) > 50:
            recent_analyses.pop()
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/governance/check', methods=['POST'])
def governance_check():
    """Check repository governance compliance"""
    try:
        data = request.get_json()
        repository = data.get('repository')
        files = data.get('files', [])
        
        if not repository:
            return jsonify({'error': 'Repository name required'}), 400
        
        result = call_codexa_governance(repository, files)
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/dashboard')
def dashboard():
    """Analytics dashboard"""
    stats = calculate_statistics(recent_analyses)
    return render_template('dashboard.html', stats=stats, analyses=recent_analyses)

@app.route('/api/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'codexa-ai-reviewer',
        'version': '1.0.0',
        'timestamp': datetime.utcnow().isoformat(),
        'analyses_count': len(recent_analyses)
    })

@app.route('/api/stats')
def stats():
    """Get analytics statistics"""
    return jsonify(calculate_statistics(recent_analyses))

def call_codexa_analyze(code: str, language: str) -> Dict:
    """Call Codexa analysis API"""
    try:
        headers = {'Content-Type': 'application/json'}
        if CODEXA_FUNCTION_KEY:
            headers['x-functions-key'] = CODEXA_FUNCTION_KEY
        
        response = requests.post(
            f'{CODEXA_API_BASE}/analyze',
            headers=headers,
            json={'code': code, 'language': language},
            timeout=10
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            # Fallback mock response
            return generate_mock_analysis(code, language)
    except:
        return generate_mock_analysis(code, language)

def call_codexa_governance(repository: str, files: List[str]) -> Dict:
    """Call Codexa governance API"""
    try:
        headers = {'Content-Type': 'application/json'}
        if CODEXA_FUNCTION_KEY:
            headers['x-functions-key'] = CODEXA_FUNCTION_KEY
        
        response = requests.post(
            f'{CODEXA_API_BASE}/governance/check',
            headers=headers,
            json={'repository': repository, 'files': files},
            timeout=10
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            return generate_mock_governance(repository, files)
    except:
        return generate_mock_governance(repository, files)

def generate_mock_analysis(code: str, language: str) -> Dict:
    """Generate mock analysis for demo purposes"""
    quality_score = 7.5
    security_score = 8.0
    alignment_score = 7.0
    
    issues = []
    if 'password' in code.lower() or 'api_key' in code.lower():
        security_score -= 2.0
        issues.append({
            'type': 'security',
            'severity': 'high',
            'message': 'Potential hardcoded credentials detected',
            'line': 1
        })
    
    if len(code) > 500:
        quality_score -= 0.5
        issues.append({
            'type': 'quality',
            'severity': 'medium',
            'message': 'Function may be too complex',
            'line': 1
        })
    
    return {
        'analysis_id': hashlib.md5(code.encode()).hexdigest()[:12],
        'timestamp': datetime.utcnow().isoformat(),
        'language': language,
        'scores': {
            'quality': quality_score,
            'security': security_score,
            'alignment': alignment_score,
            'overall': (quality_score + security_score + alignment_score) / 3
        },
        'issues': issues,
        'lines_analyzed': len(code.split('\n')),
        'governance_status': 'compliant' if security_score >= 7.0 else 'needs_review'
    }

def generate_mock_governance(repository: str, files: List[str]) -> Dict:
    """Generate mock governance response"""
    return {
        'check_id': hashlib.md5(repository.encode()).hexdigest()[:12],
        'timestamp': datetime.utcnow().isoformat(),
        'repository': repository,
        'governance_status': 'aligned',
        'compliant': True,
        'coherence_score': 85,
        'violations': [],
        'warnings': [],
        'policies_checked': 8,
        'files_checked': len(files)
    }

def generate_ai_recommendations(analysis: Dict, code: str, language: str) -> List[str]:
    """Generate AI-powered recommendations"""
    recommendations = []
    
    scores = analysis.get('scores', {})
    issues = analysis.get('issues', [])
    
    # Quality recommendations
    if scores.get('quality', 10) < 7:
        recommendations.append('Consider refactoring for better code quality and maintainability')
        recommendations.append('Add comprehensive documentation and type hints')
    
    # Security recommendations
    if scores.get('security', 10) < 7:
        recommendations.append('Review security issues immediately - high priority')
        recommendations.append('Implement input validation and sanitization')
    
    # Alignment recommendations
    if scores.get('alignment', 10) < 7:
        recommendations.append('Ensure code follows organizational governance standards')
        recommendations.append('Review and update documentation to match policies')
    
    # Issue-specific recommendations
    for issue in issues:
        if issue['severity'] == 'high':
            recommendations.append(f"CRITICAL: {issue['message']}")
    
    if not recommendations:
        recommendations.append('Excellent work! Code meets all governance standards')
        recommendations.append('Continue following best practices')
    
    return recommendations

def calculate_statistics(analyses: List[Dict]) -> Dict:
    """Calculate analytics statistics"""
    if not analyses:
        return {
            'total_analyses': 0,
            'avg_quality': 0,
            'avg_security': 0,
            'avg_alignment': 0,
            'compliance_rate': 0,
            'languages': {},
            'recent_trend': 'stable'
        }
    
    total = len(analyses)
    quality_scores = []
    security_scores = []
    alignment_scores = []
    compliant_count = 0
    languages = {}
    
    for analysis in analyses:
        scores = analysis.get('analysis', {}).get('scores', {})
        quality_scores.append(scores.get('quality', 0))
        security_scores.append(scores.get('security', 0))
        alignment_scores.append(scores.get('alignment', 0))
        
        if analysis.get('analysis', {}).get('governance_status') == 'compliant':
            compliant_count += 1
        
        lang = analysis.get('language', 'unknown')
        languages[lang] = languages.get(lang, 0) + 1
    
    avg_quality = sum(quality_scores) / len(quality_scores) if quality_scores else 0
    avg_security = sum(security_scores) / len(security_scores) if security_scores else 0
    avg_alignment = sum(alignment_scores) / len(alignment_scores) if alignment_scores else 0
    
    return {
        'total_analyses': total,
        'avg_quality': round(avg_quality, 2),
        'avg_security': round(avg_security, 2),
        'avg_alignment': round(avg_alignment, 2),
        'avg_overall': round((avg_quality + avg_security + avg_alignment) / 3, 2),
        'compliance_rate': round((compliant_count / total * 100), 1),
        'languages': languages,
        'recent_trend': 'improving' if avg_quality > 7 else 'needs_attention'
    }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
