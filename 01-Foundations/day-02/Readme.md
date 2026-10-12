## Day 2 — Assignment (90 minutes):
1. Extend api_request_demo.py to make a POST request using JSON data.
2. Print the status code and the returned JSON response.
3. Add error handling with response.raise_for_status().
4. Document GET vs POST, HTTP headers, and status codes in 01-Foundations/day-02/Readme.md.
5. Commit your work and report back with any errors.

<hr>

# Day 02 — HTTP and API Requests

## 1. What is an API?

An API (Application Programming Interface) allows two software applications to communicate with each other.

For example, a Python program can use an API to request information from a server.

## 2. GET vs POST

### GET

- Used to retrieve data from a server.
- Usually sends parameters through the URL.
- Should not be used to create or modify resources.
- Example: Fetching post number 5.

```python
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/5",
    timeout=5
)
```

### POST

- Used to send data to a server, often to create a resource.
- Data is commonly sent in the request body.
- The server decides what to do with the submitted data.
- Example: Submitting a new post.

```python
new_post = {
    "title": "My First API Post",
    "body": "Learning APIs",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post,
    timeout=5
)
```

## 3. HTTP Headers

HTTP headers carry additional information about a request or response.

Examples:

- `Content-Type`: Describes the format of the request or response body, such as `application/json`.
- `Accept`: Tells the server which response formats the client can accept.
- `Authorization`: Can carry authentication credentials, such as a bearer token.

When using `requests.post(..., json=new_post)`, the Requests library automatically sets an appropriate JSON content type.

Example:

```python
headers = {
    "Accept": "application/json"
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/5",
    headers=headers,
    timeout=5
)
```

## 4. HTTP Status Codes

Status codes tell us the outcome of an HTTP request.

| Code | Meaning |
|---|---|
| 200 | OK — request succeeded |
| 201 | Created — resource was created |
| 400 | Bad Request — request is invalid |
| 401 | Unauthorized — authentication is required or invalid |
| 403 | Forbidden — access is not allowed |
| 404 | Not Found — resource was not found |
| 429 | Too Many Requests — rate limit exceeded |
| 500 | Internal Server Error — server encountered an error |

## 5. Error Handling

The `response.raise_for_status()` method raises a `requests.exceptions.HTTPError` when the response has an HTTP error status code (400 or higher).

The `try` and `except` blocks help us handle errors without abruptly stopping the program.

```python
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/5",
        timeout=5
    )

    response.raise_for_status()
    data = response.json()

    print(data)

except requests.exceptions.Timeout:
    print("The request took too long.")

except requests.exceptions.RequestException as error:
    print("Request failed:", error)
```

Important: `raise_for_status()` does not automatically handle network failures, invalid JSON, or every possible application-level error. Those require appropriate handling of their own.

## 6. What I Practised

- Sending GET requests using Python's `requests` library.
- Sending POST requests with JSON data.
- Reading status codes and JSON responses.
- Using timeouts to avoid waiting indefinitely.
- Handling HTTP and request errors using `try` and `except`.
- Understanding HTTP headers and common status codes.

Note: JSONPlaceholder is a mock API. Its POST endpoint returns a simulated created resource; it does not permanently store the new post.