
import requests

# -------------------------
# 1. GET REQUEST
# -------------------------

url = "https://jsonplaceholder.typicode.com/posts/5"

try:
    response = requests.get(url, timeout=5)

    # Raise an error if the server returns an HTTP error
    response.raise_for_status()

    print("GET Status Code:", response.status_code)

    data = response.json()

    print("Post ID:", data["id"])
    print("Title:", data["title"])

except requests.exceptions.Timeout:
    print("The GET request took too long.")

except requests.exceptions.RequestException as error:
    print("GET request failed:", error)


# -------------------------
# 2. POST REQUEST
# -------------------------

post_url = "https://jsonplaceholder.typicode.com/posts"

new_post = {
    "title": "My First API Post",
    "body": "I am learning APIs step by step!",
    "userId": 1
}

try:
    response = requests.post(
        post_url,
        json=new_post,
        timeout=5
    )

    # Raise an error if the server returns an HTTP error
    response.raise_for_status()

    print("\nPOST Status Code:", response.status_code)
    print("Returned JSON Response:", response.json())

except requests.exceptions.Timeout:
    print("The POST request took too long.")

except requests.exceptions.RequestException as error:
    print("POST request failed:", error)
