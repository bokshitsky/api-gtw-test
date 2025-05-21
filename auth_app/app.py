from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response

app = FastAPI()


@app.get("/session_auth")
async def session_auth(request: Request, response: Response):
    print(request.headers)
    response.headers.append("x-hh-session", "TEST_SESSION")
    return {"message": "2Hello World"}


@app.get("/session_auth2")
async def session_auth2(request: Request, response: Response):
    print(request.headers)
    response.headers.append("x-hh-session2", "TEST_SESSION2")
    return {"message 2": "Hello World 2"}


@app.get("/")
async def root(response: Response):
    # response.headers.append("x-hh-session", "TEST_SESSION")
    return {"message": "root_response"}
