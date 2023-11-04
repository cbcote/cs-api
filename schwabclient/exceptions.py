class APIClientError(Exception):
    """Base exception class for API Client errors."""
    pass

class APIConnectionError(APIClientError):
    """Exception raised when there is a network connection error."""
    pass

class APIRequestError(APIClientError):
    """Exception raised for errors that occur during API request (excluding network problems)."""
    def __init__(self, status_code, message=None):
        super().__init__(message)
        self.status_code = status_code
        self.message = message

class AuthenticationError(APIRequestError):
    """Exception raised when there is an authentication issue with the API."""
    pass

class PermissionDeniedError(APIRequestError):
    """Exception raised when permissions are insufficient."""
    pass

class NotFoundError(APIRequestError):
    """Exception raised when a resource is not found."""
    pass

class RateLimitExceededError(APIRequestError):
    """Exception raised when API rate limits have been exceeded."""
    pass

class InvalidResponseError(APIRequestError):
    """Exception raised when the API response is malformed or unexpected."""
    pass

# Other specific exception classes can be added here
