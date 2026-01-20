# 🚀 Quick Start Guide

## Your Code Location
**Project Directory:** `/home/hafiz/codexa-ai-reviewer/`

## ✅ Current Status
- ✅ App running at: http://localhost:5000
- ✅ Code committed to git
- ✅ Ready to push to GitHub

## 📤 Push to GitHub

### If repository doesn't exist yet:
```bash
# Create the repository on GitHub first at:
# https://github.com/new
# Name it: codexa-ai-reviewer
# Make it public, don't initialize

# Then push:
cd /home/hafiz/codexa-ai-reviewer
git push -u origin main
```

**You'll be prompted for:**
- Username: `Hafizva-beep`
- Password: Use a **Personal Access Token** (not your password)

### Get a Personal Access Token:
1. Go to: https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Give it a name: "Codexa Deployment"
4. Check: `repo` (all repo permissions)
5. Click "Generate token"
6. Copy the token (starts with `ghp_...`)
7. Use this as your password when git asks

## ☁️ Deploy to Azure

```bash
cd /home/hafiz/codexa-ai-reviewer

# Deploy using zip deployment
az webapp deploy \
  --resource-group rg-hafiz_va-4308 \
  --name codexa-ai-reviewer \
  --src-path codexa-ai-reviewer.zip \
  --type zip
```

## 🌐 Access URLs

- **Local:** http://localhost:5000
- **GitHub:** https://github.com/Hafizva-beep/codexa-ai-reviewer (after push)
- **Azure:** https://codexa-ai-reviewer.azurewebsites.net (after deployment)

## 📁 Project Files

```
/home/hafiz/codexa-ai-reviewer/
├── app.py                  # Main Flask application
├── templates/
│   ├── index.html         # Code analyzer UI
│   └── dashboard.html     # Analytics dashboard
├── requirements.txt       # Python dependencies
├── README.md             # Full documentation
├── DEMO_GUIDE.md         # Demo script
├── DEPLOYMENT_STATUS.md  # Deployment info
├── Procfile              # Production config
└── .github/workflows/
    └── deploy.yml        # CI/CD pipeline
```

## 🎯 Next Steps

1. **Create GitHub repo** at https://github.com/new
2. **Get personal access token** from https://github.com/settings/tokens
3. **Push code:** `git push -u origin main` (use token as password)
4. **Share the URL:** https://github.com/Hafizva-beep/codexa-ai-reviewer
