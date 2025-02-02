from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI()

class RequestBody(BaseModel):
    body: str

@app.post("/items/{path}")
async def exercise_function(
    path: str = Path(..., description="Path parameter"),
    query: str = Query(..., description="Query parameter"),
    body: RequestBody = ...
):
    return {"path": path, "query": query, "body": body.body}
