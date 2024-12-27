import requests

# Replace these with your actual values
endpoint_id = "********"
api_key = "********"
url = f"https://api.runpod.ai/v2/{endpoint_id}/runsync"

# Define the payload
payload = {
  "input": {
    "file_url": "********"
  }
}

# Define the headers
headers = {
    "accept": "application/json",
    "authorization": api_key,
    "content-type": "application/json"
}

# Make the POST request
response = requests.post(url, json=payload, headers=headers)

# Check the response
if response.status_code == 200:
    print("Request successful!")
    print(response.json())  # Print the response JSON
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)  # Print the error response
