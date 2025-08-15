#!/bin/bash

echo "🚀 Deploying Australia Trip Itinerary Web App"
echo "=============================================="

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "❌ Git repository not initialized. Please run 'git init' first."
    exit 1
fi

# Check if we have uncommitted changes
if [ -n "$(git status --porcelain)" ]; then
    echo "📝 Committing changes..."
    git add .
    git commit -m "Update: $(date)"
fi

echo "✅ Your app is ready for deployment!"
echo ""
echo "📋 Next steps:"
echo "1. Create a GitHub repository at https://github.com/new"
echo "2. Name it: australia-trip-itinerary"
echo "3. Make it public"
echo "4. Run these commands:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/australia-trip-itinerary.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "5. Deploy to Render:"
echo "   - Go to https://render.com"
echo "   - Create new Web Service"
echo "   - Connect your GitHub repo"
echo "   - Deploy!"
echo ""
echo "🎉 Your app will be live at: https://australia-trip-itinerary.onrender.com" 