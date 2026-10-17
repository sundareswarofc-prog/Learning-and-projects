import requests

# response = requests.get(
#     "https://jsonplaceholder.typicode.com/posts/1"
# )

# print(response.status_code)
# print(response.json())


try:
    response=requests.get("https://jsonplaceholder.typicode.com/posts/1",
                        timeout=5
    )
    print(response.json())

except requests.exceptions.Timeout:
    print("this requests take too long")

except requests.exceptions.HTTPError as e:
    print(f"this requests take too long {e}")

except requests.exceptions.RequestException as error:
    print("Request failed:", error)


# Send data with POST


url = "https://jsonplaceholder.typicode.com/posts"

new_post = {
    "title": "Learning Python",
    "body": "I am learning HTTP APIs",
    "userId": 1
}

response = requests.post(
    url,
    json=new_post, #this converts python dict to json
    timeout=5
)

print(response.status_code)
print(response.json())





# httpx supports both synchronous and asynchronous HTTP requests. Asynchronous requests are especially useful when an application needs to handle many network operations concurrently. 


