from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

app = FastAPI()

# Get allowed origins from environment variable or use a default for development
allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000,http://localhost:8080").split(",")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,  # Only specific origins are allowed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to Phish-Net API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)