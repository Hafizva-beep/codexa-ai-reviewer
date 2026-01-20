# Codexa AI Code Reviewer

> **Enterprise-grade AI-powered code analysis platform demonstrating Codexa governance capabilities**

A production-ready web application showcasing Codexa's AI-driven code analysis and governance validation for Azure and Microsoft engineering teams.

---

## 🎯 What This Demonstrates

This project showcases **Codexa's capabilities** for:

### 1. **Real-time Code Analysis**
- Multi-language support (Python, JavaScript, TypeScript, Java, C#, Go)
- Quality, security, and alignment scoring
- Issue detection with severity levels
- AI-powered recommendations

### 2. **Governance Intelligence**
- Repository-wide compliance checking
- Policy enforcement via Cosmos DB
- Coherence scoring (0-100)
- Violation tracking and remediation

### 3. **Enterprise Features**
- Analytics dashboard with trends
- Historical analysis tracking
- Multi-repository support
- RESTful API endpoints
- Azure-native architecture

### 4. **Production-Ready**
- Scalable Flask application
- Azure App Service deployment
- GitHub Actions CI/CD
- Environment-based configuration
- Health check endpoints

---

## 🚀 Live Demo

**Web Interface:** http://localhost:5000 (local)
**API Health:** http://localhost:5000/api/health
**Dashboard:** http://localhost:5000/dashboard

---

## 📊 Features

### Web Interface
✅ **Code Analyzer** - Submit code and get instant AI-powered analysis
✅ **Visual Scoring** - Quality, Security, Alignment, and Overall scores
✅ **Issue Detection** - Categorized by severity (High, Medium, Low)
✅ **AI Recommendations** - Actionable improvement suggestions
✅ **Governance Validation** - Real-time policy compliance checking

### Analytics Dashboard
✅ **Aggregate Statistics** - Total analyses, average scores
✅ **Compliance Metrics** - Governance compliance rate tracking
✅ **Language Distribution** - Analysis breakdown by programming language
✅ **Historical Trends** - Track improvements over time
✅ **Recent Activity** - Latest 20 analyses with full details

### REST API
```bash
# Analyze code
POST /analyze
{
  "code": "your code here",
  "language": "python",
  "repository": "my-project"
}

# Check governance
POST /governance/check
{
  "repository": "my-project",
  "files": ["app.py", "utils.py"]
}

# Get statistics
GET /api/stats

# Health check
GET /api/health
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│         Web Application                 │
│    (Flask + HTML/CSS/JavaScript)        │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│    Codexa AI Reviewer Backend           │
│  - Analysis Engine                      │
│  - Governance Validator                 │
│  - Statistics Calculator                │
│  - Recommendation Generator             │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│    Codexa Azure Functions API           │
│  https://codexa-engine-func             │
│    .azurewebsites.net/api               │
│                                         │
│  - POST /analyze (Code Analysis)        │
│  - POST /governance/check (Validation)  │
│  - GET /health (Status)                 │
└──────────────┬──────────────────────────┘
               │
        ┌──────┴──────┐
        ▼             ▼
┌─────────────┐ ┌──────────────┐
│  Azure AI   │ │  Cosmos DB   │
│  Foundry    │ │  (Policies)  │
└─────────────┘ └──────────────┘
```

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Python 3.11 + Flask |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **API Integration** | Codexa Azure Functions |
| **Database** | Cosmos DB (via Codexa API) |
| **Hosting** | Azure App Service |
| **CI/CD** | GitHub Actions |
| **Monitoring** | Application Insights |

---

## 📥 Installation & Setup

### Prerequisites
- Python 3.11+
- Azure subscription
- Codexa Functions deployed

### Local Development

```bash
# Clone repository
git clone https://github.com/Hafizva-beep/codexa-ai-reviewer.git
cd codexa-ai-reviewer

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.template .env
# Edit .env with your Codexa API endpoint

# Run application
python app.py

# Visit http://localhost:5000
```

### Azure Deployment

```bash
# Create App Service
az webapp create \
  --resource-group rg-hafiz_va-4308 \
  --plan ASP-rgHafizva4308-82ea \
  --name codexa-ai-reviewer \
  --runtime "PYTHON:3.11"

# Configure environment variables
az webapp config appsettings set \
  --name codexa-ai-reviewer \
  --resource-group rg-hafiz_va-4308 \
  --settings CODEXA_API_BASE="https://codexa-engine-func.azurewebsites.net/api"

# Deploy
az webapp deployment source config \
  --name codexa-ai-reviewer \
  --resource-group rg-hafiz_va-4308 \
  --repo-url https://github.com/Hafizva-beep/codexa-ai-reviewer \
  --branch main \
  --manual-integration
```

---

## 🎨 Screenshots

### Code Analyzer Interface
- Beautiful gradient design
- Real-time code input
- Language selection
- One-click analysis

### Results Display
- Visual score cards (Quality, Security, Alignment, Overall)
- Color-coded severity levels
- Detailed issue descriptions
- AI-generated recommendations
- Governance compliance status

### Analytics Dashboard
- Aggregate metrics
- Compliance trends
- Language distribution
- Recent activity table

---

## 🧪 Testing

### Sample Code to Test
```python
# This code has intentional issues for demonstration
def calculate_risk(amount, probability):
    password = "admin123"  # Hardcoded credential
    api_key = "sk_test_12345"  # API key in code
    
    if amount > 0:
        risk = amount * probability
        return risk
    return 0
```

**Expected Results:**
- Security Score: ~6.0 (HIGH severity issues detected)
- Quality Score: ~7.5 (Missing documentation)
- Issues: 2 HIGH severity security violations
- Recommendations: Remove hardcoded credentials, add input validation

---

## 📈 Key Metrics Tracked

| Metric | Description |
|--------|-------------|
| **Quality Score** | Code structure, maintainability, documentation |
| **Security Score** | Vulnerability detection, credential scanning |
| **Alignment Score** | Governance policy compliance |
| **Overall Score** | Composite assessment |
| **Compliance Rate** | % of analyses meeting governance standards |
| **Coherence Score** | Repository-wide policy alignment (0-100) |

---

## 🔐 Security & Governance

### Built-in Checks
- ✅ Hardcoded credential detection
- ✅ API key scanning
- ✅ Security vulnerability patterns
- ✅ Code complexity analysis
- ✅ Documentation requirements
- ✅ Best practice validation

### Policy Enforcement
- Powered by Cosmos DB policy engine
- Real-time validation
- Customizable severity levels
- Detailed remediation guidance

---

## 🚀 For Azure/Microsoft Engineers

### Why This Matters

**1. Demonstrates Azure Integration**
- Native Azure Functions consumption
- Cosmos DB integration
- App Service deployment
- Application Insights monitoring

**2. Shows AI Capabilities**
- Real-time code analysis
- Pattern recognition
- Intelligent recommendations
- Governance automation

**3. Enterprise-Ready**
- Scalable architecture
- RESTful API design
- Environment-based config
- CI/CD pipeline

**4. Practical Use Case**
- Solves real developer pain points
- Automates manual code reviews
- Enforces organizational standards
- Tracks compliance metrics

---

## 📝 API Documentation

### POST /analyze
Analyze code with Codexa AI engine.

**Request:**
```json
{
  "code": "string (required)",
  "language": "string (required)",
  "repository": "string (optional)"
}
```

**Response:**
```json
{
  "id": "string",
  "timestamp": "ISO-8601",
  "analysis": {
    "scores": { "quality": 7.5, "security": 8.0, "alignment": 7.0, "overall": 7.5 },
    "issues": [...],
    "governance_status": "compliant"
  },
  "recommendations": [...],
  "governance": {...}
}
```

### GET /api/stats
Get aggregate analytics.

**Response:**
```json
{
  "total_analyses": 42,
  "avg_quality": 7.8,
  "avg_security": 8.2,
  "avg_alignment": 7.5,
  "compliance_rate": 85.7,
  "languages": { "python": 25, "javascript": 17 }
}
```

---

## 🎯 Demo Talking Points

### For Microsoft/Azure Teams

1. **"This shows how Codexa brings governance intelligence to developer workflows"**
   - Real-time analysis prevents issues before deployment
   - AI recommendations guide developers to better practices

2. **"Built entirely on Azure-native services"**
   - Functions for serverless compute
   - Cosmos DB for policy management
   - App Service for web hosting
   - Application Insights for monitoring

3. **"Scalable from individual developers to enterprise teams"**
   - Consumption-based pricing
   - No infrastructure management
   - Automatic scaling

4. **"Integrates seamlessly with existing workflows"**
   - REST API for CI/CD integration
   - GitHub Actions support
   - Real-time feedback loop

---

## 📦 Project Structure

```
codexa-ai-reviewer/
├── app.py                 # Main Flask application
├── templates/
│   ├── index.html        # Code analyzer interface
│   └── dashboard.html    # Analytics dashboard
├── requirements.txt      # Python dependencies
├── Procfile             # Azure deployment config
├── .env.template        # Environment variables template
├── .github/
│   └── workflows/
│       └── deploy.yml   # CI/CD pipeline
└── README.md            # This file
```

---

## 🤝 Contributing

This is a demonstration project for showcasing Codexa capabilities. For the core Codexa platform:
- **GitHub:** https://github.com/Hafizva-beep/codexa
- **API:** https://codexa-engine-func.azurewebsites.net

---

## 📄 License

MIT License - See LICENSE file for details

---

## 🆘 Support

- **Issues:** [GitHub Issues](https://github.com/Hafizva-beep/codexa-ai-reviewer/issues)
- **Documentation:** This README
- **Codexa Platform:** [Main Repository](https://github.com/Hafizva-beep/codexa)

---

**Built with ❤️ to demonstrate Codexa's AI governance capabilities**

*Showcasing the future of automated code governance for Azure and Microsoft engineering teams*
