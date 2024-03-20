import uuid
import io
from fastapi import FastAPI, Path, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from PIL import Image

# App FastAPI object
app = FastAPI()

origins = ['http://localhost:8501',]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"Data": "CORS Enable"}

@app.get("/about")
def about():
    return "Encouragement Stroytelling Platform Under Construction"

@app.get("/about-test")
def about_test():
    return "Encouragement Stroytelling Platform Under Construction"
