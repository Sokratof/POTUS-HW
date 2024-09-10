from fastapi import FastAPI
from starlette.responses import JSONResponse
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """   
    <!DOCTYPE html>
    <html>
    <head>
        <title>FastAPI Page</title>
    </head>
    <body>
        <h1>Welcome to FastAPI page!</h1>
        <p>This is OTUUUS!!!.</p>
    </body>
    </html>
    """

@app.get("/ping/")
async def read_root():
    return JSONResponse({"message": "pong"})

