import requests
from typing import Dict, Any, Optional

def make_post_request(
    url: str,
    data: Dict[str, Any],
    headers: Optional[Dict[str, str]] = None,
    timeout: int = 30
) -> requests.Response:
    """
    Make a POST request to the specified endpoint with the given data.
    
    Args:
        url (str): The endpoint URL to send the POST request to
        data (Dict[str, Any]): The data to send in the request body
        headers (Optional[Dict[str, str]]): Optional headers for the request
        timeout (int): Request timeout in seconds (default: 30)
    
    Returns:
        requests.Response: The response from the server
        
    Raises:
        requests.RequestException: If the request fails
    """
    try:
        response = requests.post(
            url=url,
            json=data,  # Using json parameter for automatic serialization
            headers=headers,
            timeout=timeout
        )
        response.raise_for_status()  # Raise an exception for bad status codes
        return response
    except requests.RequestException as e:
        raise requests.RequestException(f"Failed to make POST request: {str(e)}")
