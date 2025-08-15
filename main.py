from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
import httpx
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

logger.info(f"Base directory: {BASE_DIR}")
logger.info(f"Static directory: {STATIC_DIR}")
logger.info(f"Static directory exists: {os.path.exists(STATIC_DIR)}")

# Serve static files like your HTML page
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Route to serve your HTML page
@app.get("/", response_class=HTMLResponse)
def serve_itinerary():
    html_path = os.path.join(STATIC_DIR, "itinerary.html")
    logger.info(f"HTML path: {html_path}")
    logger.info(f"HTML file exists: {os.path.exists(html_path)}")
    
    if not os.path.exists(html_path):
        logger.error(f"HTML file not found at {html_path}")
        raise HTTPException(status_code=404, detail="HTML file not found")
    
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        logger.info(f"Successfully loaded HTML file, size: {len(html_content)} characters")
        return HTMLResponse(content=html_content)
    except Exception as e:
        logger.error(f"Error reading HTML file: {e}")
        raise HTTPException(status_code=500, detail=f"Error reading HTML file: {str(e)}")

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "Australia Trip Itinerary is running!"}

# Optional: Your existing joke API
@app.get("/call-external")
async def call_external_api():
    url = "https://api.chucknorris.io/jokes/random"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
    return {"joke": data.get("value")}
