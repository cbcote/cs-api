import json
from urllib.parse import urljoin

def build_url(base_url, path, query_params=None):
    """
    Construct a full URL from base URL, path, and optional query parameters.
    
    Args:
        base_url (str): The base URL.
        path (str): The path.
        query_params (dict): The query parameters.
    
    Returns:
        str: The full URL.
    """
    url = urljoin(base_url, path)
    if query_params:
        url += "?" + "&".join([f"{key}={value}" for key, value in query_params.items()])
    return url

def pretty_print_json(data):
    """
    Pretty print a dictionary as JSON.
    
    Args:
        data (dict): The data to print.
    """
    print(json.dumps(data, indent=4, sort_keys=True))

def enforce_required_keys(data, required_keys):
    """
    Ensure that the given data has the required keys.
    
    Args:
        data (dict): The data to check.
        required_keys (list): The list of required keys.
    
    Raises:
        ValueError: If the data is missing any of the required keys.
    
    """
    missing_keys = [key for key in required_keys if key not in data]
    if missing_keys:
        raise ValueError(f"Missing required keys: {', '.join(missing_keys)}")

# Other utility functions and classes
