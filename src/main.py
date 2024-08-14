from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Home Page", 
        "documentation": "Visit /docs to see the documentation"
    }