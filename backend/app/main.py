from fastapi import FastAPI
from pydantic import BaseModel

from .director.director import Director


app = FastAPI(
    title="Atlas AI",
    version="0.2.0"
)


class AgentRequest(BaseModel):
    task: str


@app.get("/")
def home():
    return {
        "project": "Atlas AI",
        "version": "0.2.0",
        "status": "running"
    }


@app.post("/agent/test")
def run_agent(request: AgentRequest):

    director = Director()

    result = director.execute(request.task)

    return result
