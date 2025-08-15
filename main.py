from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import httpx
import os

app = FastAPI()

# Serve static files like your HTML page
app.mount("/static", StaticFiles(directory="static"), name="static")

# Route to serve your HTML page
@app.get("/")
def serve_itinerary():
    return FileResponse(os.path.join("static", "itinerary.html"))

# Optional: Your existing joke API
@app.get("/call-external")
async def call_external_api():
    url = "https://api.chucknorris.io/jokes/random"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
    return {"joke": data.get("value")}
