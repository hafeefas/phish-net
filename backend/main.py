from fastapi import FastAPI, HTTPException  # For creating the API server
from fastapi.middleware.cors import CORSMiddleware  # For handling cross-origin requests
from app.ai_simulator import AIPhoneCallSimulator  # Import our AI simulator
import uvicorn  # ASGI server for running FastAPI

# Create FastAPI application instance
app = FastAPI()

# Configure Cross-Origin Resource Sharing (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins in development (customize in production)
    allow_credentials=True,  # Allow credentials (cookies, authorization headers)
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Create an instance of our AI simulator
simulator = AIPhoneCallSimulator()

@app.get("/")
async def root():
    """Root endpoint - returns welcome message"""
    return {"message": "Welcome to Phish-Net API"}

@app.get("/personas")
async def get_personas():
    """Endpoint to get all available phone scam personas"""
    return simulator.get_personas()

# Run the server if this file is run directly
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Run on all network interfaces, port 8000 