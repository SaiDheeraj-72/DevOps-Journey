import requests

response = requests.get("https://api.github.com")

print(response.status_code)



# Output
200


# Explanation

requests is a popular third-party package from PyPI used for making HTTP requests.
