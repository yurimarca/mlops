import requests

def call_prediction_api():
    try:
        # Define the API endpoint
        url = 'http://127.0.0.1:5000/prediction'
        
        # Make a GET request to the endpoint
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            predictions = response.json()
            print("Predictions:", predictions)
        else:
            print("Error:", response.status_code, response.json())
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == '__main__':
    call_prediction_api()