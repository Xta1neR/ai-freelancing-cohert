import requests

url = "https://jsonplaceholder.typicode.com/posts/5"

try:
    response = requests.get(url, timeout=5)
    print("Status Code:", response.status_code)

    data = response.json()

    print("Post ID: ", data['id'])
    # print("User ID: ", data['userId'])
    print("Title: ", data['title'])
    # print("Body: ", data['body'])

except requests.exceptions.Timeout:
    print("The request took too long. Please try again later.")

