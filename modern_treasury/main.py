# Import necessary libraries
import requests
from modern_treasury_helpers import create_modern_treasury_account

# Define API key for Modern Treasury
modern_treasury_api_key = 'modern_treasury_api_key'

# Define parameters for account creation
account_params = {
    'name': 'Account Name',
    'type': 'checking',
    # Add other required parameters
}

# Create the Modern Treasury account
response = create_modern_treasury_account(modern_treasury_api_key, account_params)

# Print the response
print(response.json())