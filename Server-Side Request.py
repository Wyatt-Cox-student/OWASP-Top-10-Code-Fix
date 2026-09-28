import requests
from urllib.parse import urlparse

ALLOWED_HOSTS = [
    "example.com",
    "api.example.com"
]

def get_url(url):

    parsed_url = urlparse(url)

    if parsed_url.scheme != "https":
        raise ValueError("Only HTTPS URLs are allowed")

    if parsed_url.hostname not in ALLOWED_HOSTS:
        raise ValueError("This website is not allowed")

    response = requests.get(
        url,
        timeout=5,
        allow_redirects=False
    )

    return response.text


url = input("Enter URL: ")

try:
    print(get_url(url))
except Exception as error:
    print("Request blocked:", error)