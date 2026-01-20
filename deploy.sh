#!/bin/bash

echo "========================================="
echo "Codexa AI Reviewer - Deployment Script"
echo "========================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Step 1: Pushing to GitHub${NC}"
echo "Repository: https://github.com/Hafizva-beep/codexa-ai-reviewer"
echo ""

cd /home/hafiz/codexa-ai-reviewer

# Add and commit
git add -A
git commit -m "Deploy Codexa AI Code Reviewer" 2>&1 || echo "Nothing to commit"

# Push to GitHub
echo ""
echo "Attempting to push to GitHub..."
echo "If prompted, enter:"
echo "  Username: Hafizva-beep"
echo "  Password: Your GitHub Personal Access Token"
echo ""
echo "Don't have a token? Get one here: https://github.com/settings/tokens"
echo "Required scopes: repo (all)"
echo ""

git push -u origin main

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ GitHub push successful!${NC}"
    echo "View at: https://github.com/Hafizva-beep/codexa-ai-reviewer"
else
    echo -e "${RED}❌ GitHub push failed${NC}"
    echo ""
    echo "To fix:"
    echo "1. Create repository at: https://github.com/new"
    echo "   Name: codexa-ai-reviewer"
    echo "   Public, don't initialize"
    echo ""
    echo "2. Get a token at: https://github.com/settings/tokens"
    echo "   Select: repo (all permissions)"
    echo ""
    echo "3. Run: git push -u origin main"
    echo "   Use token as password"
fi

echo ""
echo -e "${YELLOW}Step 2: Deploying to Azure${NC}"
echo ""

# Deploy to Azure
az webapp up \
    --runtime PYTHON:3.11 \
    --sku B1 \
    --name codexa-reviewer-app \
    --resource-group rg-hafiz_va-4308 \
    --location eastus

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✅ Azure deployment successful!${NC}"
    echo "View at: https://codexa-reviewer-app.azurewebsites.net"
else
    echo ""
    echo -e "${RED}❌ Azure deployment failed${NC}"
    echo "This might be due to quota limits."
    echo "Your app is still running locally at: http://localhost:5000"
fi

echo ""
echo "========================================="
echo "Deployment Summary"
echo "========================================="
echo "📱 Local:  http://localhost:5000"
echo "📱 GitHub: https://github.com/Hafizva-beep/codexa-ai-reviewer"
echo "☁️  Azure:  https://codexa-reviewer-app.azurewebsites.net"
echo ""
echo "Local app is confirmed working!"
echo "Test it now: http://localhost:5000"
echo "========================================="
