import sys
import requests
from pathlib import Path
import pandas as pd
import json

# Import secrets from a separate configuration file or environment variables
from config import email, api_token, subdomain

def main(): 
    # Load the Excel file into a DataFrame
    file_path = 'path/to/your/ticket-field.xlsx'
    oddf = pd.read_excel(file_path, usecols=['value', 'tag'])

    # Fetch the data from the API
    api_endpoint = f'https://{subdomain}.zendesk.com/api/v2/ticket_fields/{YOUR_CUSTOM_FIELD_ID}'
    auth = (email + "/token", api_token)
    response = requests.get(api_endpoint + ".json", auth=auth, timeout=60)
    data = response.json()

    # Create the zddf DataFrame
    zddf_columns = ['name', 'value']
    zddf = pd.DataFrame(data['ticket_field']['custom_field_options'])
    zddf = zddf[zddf_columns]

    # Rename the columns of oddf
    oddf.columns = ['name', 'value']

    # Early exit if nothing new
    if oddf.shape == zddf.shape:
        print("No new fields")
        sys.exit()

    all_fields = oddf.to_dict(orient='records')

    data = {
        "ticket_field": {
            "custom_field_options": all_fields
        }
    }

    put_response = requests.put(api_endpoint + '.json', json=data, headers={'Content-Type': 'application/json'}, auth=auth, timeout=60)

    if put_response.status_code == 200:
        print("Custom field options updated successfully")
    else:
        print(f"Failed to update custom field options. Status code: {put_response.status_code}, Response: {put_response.text}")

if __name__ == "__main__":
    main()
