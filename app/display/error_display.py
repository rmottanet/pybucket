#!/usr/local/bin/python3.9
#-*- coding: UTF-8 -*-

import json


def display_error(error):
    """Displays the error that occurred."""
    print("An error occurred during execution:")
    print(error)

def handle_adapter_response(response):
    """
    Extracts and returns the error message from the API response.
    
    Args:
      response: The response object from the adapter.
    
    Returns:
      A string containing the error message, or None if the response
      is successful (status code 200) or the message cannot be extracted.
    """
    
    if response.status_code == 200:
        # Successful response, no error message to extract
        return None
    
    try:
        # Parse JSON response
        data = json.loads(response.text)
        # Access the message nested within the error object
        error_message = data.get('error', {}).get('message')
        return f'Failure: {response.status_code} - {error_message}'
    except (json.JSONDecodeError, KeyError):
        # Handle potential errors during JSON parsing or key access
        return f'Failure: {response.status_code} - Could not parse error message'
