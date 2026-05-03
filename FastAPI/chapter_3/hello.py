from fastapi import FastAPI, Body, Header, Response
from typing import Optional
from web import tag as web_tag

app = FastAPI()


app.include_router(web_tag.router, prefix="/tags", tags=["Tags"])


@app.get("/hi")
def greet(who: Optional[str] = None):
    if not who:
        return "Hello? World?"
    return f"Hello? {who}?"


# Example 21
@app.post("/hi")
def greet(who: str = Body(embed=True)):
    return f"Hello? {who}?"


# Example 24
@app.get("/hello")
def greet(who: str = Header()):
    return f"Hello? {who}?"


# Example 26
@app.get("/agent")
def get_agent(user_agent: str = Header()):
    return user_agent


# Example 28
@app.get("/happy")
def happy(status_code=200):
    return ":)"


# Example 30
# Response Type
# JSONResponse, HTMLResponse, PlainTextResponse, RedirectResponse, FileResponse, StreamingResponse
@app.get("/header/{name}/{value}")
def header(name: str, value: str, response: Response):
    response.headers[name] = value
    return "normal body"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("hello:app", reload=True)
