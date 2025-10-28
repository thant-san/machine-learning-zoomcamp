import requests

    # The URL of your running Flask server
url = "http://localhost:9696/predict"

    # The client data you want to score
    # Note: I fixed the indentation from your pasted code
client = {
        "job": "student", 
        "duration": 280, 
        "poutcome": "failure"
    }

    # Send the POST request
try:
        response = requests.post(url, json=client)
        
        # Print the JSON response from the server
        print(response.json())

except requests.exceptions.ConnectionError:
        print(f"Error: Could not connect to the server at {url}.")
        print("Is your Flask app running?")

    
