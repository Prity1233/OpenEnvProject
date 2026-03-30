from fastapi import FastAPI

app = FastAPI()

@app.post("/")
def reset_env():
    return {"message": "Environment reset successful"}