# Parameters and Input in FastAPI

A simple script that creates a FastAPI app and defines a POST method that takes one path parameter, 
one query parameter, and a request body containing a single field. Have this function return all three in a dict.

```python
@app.post(...)
async def exercise_function(...):
  return {"path": path, "query": query, "body": body}
```

## 1. bar.py
This file contains a FastAPI application that defines a POST endpoint. The endpoint takes:
- A path parameter (path).
- A query parameter (query).
- A request body (body), which contains a single integer field.

```sh
uvicorn bar:app --reload
```

- The --reload flag ensures the server automatically reloads if you make changes to the code.
- By default, the app will be accessible at http://127.0.0.1:8000.

### POST request:

```sh
curl -X 'POST' \
  'http://127.0.0.1:8000/42?query=5' \
  -H 'Content-Type: application/json' \
  -d '{"value": 10}'
```

**Response**:
```json
{
    "path": 42,
    "query": 5,
    "body": {
        "value": 10
    }
}
```

## 2. test_bar.py

This file contains automated tests using pytest and FastAPI's TestClient. 
It verifies whether the API behaves as expected.

- TestClient(app) allows us to send requests without starting a real server.
- Test Function:
    - Creates test data ({"value": 10}).
    - Sends a POST request to /42?query=5.
    - Asserts that the response contains the correct path, query, and body.

```sh
pytest test_bar.py
```
