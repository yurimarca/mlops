from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Value(BaseModel):
    value: int

# Use POST action to send data to the server
@app.post("/{path}")
async def exercise_function(path: int, query: int, body: Value):
    return {"path": path, "query": query, "body": body}
