import requests
import pandas as pd

# Make the GET request to the REST API
response = requests.get('https://api.publicapis.org/entries')

# Check if the request was successful
if response.status_code == 200:
    # Load the data into a pandas DataFrame
    data = pd.DataFrame(response.json())
    
    # Save the DataFrame to a CSV file
    data.to_csv('output.csv', index=False)
else:
    print(f"Request failed with status code {response.status_code}")