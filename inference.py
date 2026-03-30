from fastapi import FastAPI
import os

app = FastAPI()

@app.post("/openenv/reset")
def reset_env():
    os.environ["MY_VAR"] = "Hello from OpenEnv"
    return {"message": "Environment reset successful"}

@app.get("/openenv/validate")
def validate_env():
    value = os.getenv("MY_VAR", None)
    return {"MY_VAR": value}
