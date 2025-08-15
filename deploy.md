# Deployment Instructions

Your Australia Trip Itinerary web app is ready to be deployed! Here are the steps:

## Option 1: Deploy to Render (Recommended - Free)

1. Go to [render.com](https://render.com) and sign up/login
2. Click "New +" and select "Web Service"
3. Connect your GitHub account (you'll need to push this to GitHub first)
4. Select this repository
5. Render will automatically detect it's a Python app
6. Set the following:
   - **Name**: australia-trip-itinerary
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
7. Click "Create Web Service"

## Option 2: Deploy to Railway (Alternative - Free)

1. Go to [railway.app](https://railway.app) and sign up/login
2. Click "New Project" → "Deploy from GitHub repo"
3. Connect your GitHub account and select this repository
4. Railway will automatically detect the Python app
5. Deploy!

## Option 3: Deploy to Heroku (Alternative)

1. Go to [heroku.com](https://heroku.com) and sign up/login
2. Create a new app
3. Connect to GitHub and select this repository
4. Deploy!

## To push to GitHub first:

```bash
# Create a new repository on GitHub.com
# Then run these commands:
git remote add origin https://github.com/YOUR_USERNAME/australia-trip-itinerary.git
git branch -M main
git push -u origin main
```

## Your app features:
- Beautiful Australia trip itinerary with swipe navigation
- Responsive design for mobile and desktop
- FastAPI backend with static file serving
- Chuck Norris joke API integration

Once deployed, you'll get a URL like: `https://australia-trip-itinerary.onrender.com` 