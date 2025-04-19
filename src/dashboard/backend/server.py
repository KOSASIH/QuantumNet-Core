# src/dashboard/backend/server.py

import os
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from api import app as api_app
import uvicorn

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Change to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Network Monitoring Dashboard"}

@app.get("/health")
def health_check():
    """Health check endpoint."""
    return JSONResponse(content={"status": "healthy"}, status_code=200)

# Include the API routes
app.mount("/api/v1", api_app)  # Versioning the API

# Example usage
if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    logging.info(f"Starting server at http://{host}:{port}")
    uvicorn.run(app, host=host, port=port)
