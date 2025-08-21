from fastapi import FastAPI
from starlette.responses import Response, JSONResponse

app = FastAPI()

@app.get("/ping")
def ping():
    return JSONResponse(content="pong", status_code=200, media_type="text/plain")