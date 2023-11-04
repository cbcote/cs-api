import json
from typing import Any, Dict, List, Optional

class BaseModel:
    """
    A base model to define common behavior among all models.
    Provides basic serilization and deserialization functionality
    which other models can inherit.
    """
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the model to a dictionary.
        
        Returns:
            Dict[str, Any]: The dictionary representing the model.
        """
        return self.__dict__

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """
        Creates an instance of the model from a dictionary.
        
        Args:
            data (Dict[str, Any]): The dictionary to deserialize.
        """
        return cls(**data)

    def to_json(self) -> str:
        """
        Converts the model to a JSON string.
        
        Returns:
            str: The JSON string representing the model.
        """
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, data: str):
        """
        Creates an instance of the model from a JSON string.
        
        Args:
            data (str): The JSON string to deserialize.
        """
        return cls.from_dict(json.loads(data))


class Resource(BaseModel):
    """A model representing a resource."""
    
    def __init__(self, id: int, name: str, description: Optional[str] = None, tags: Optional[List[str]] = None):
        """
        Initializes a new instance of the Resource class.
        
        Args:
            id (int): The unique identifier of the resource.
            name (str): The name of the resource.
            description (Optional[str]): The description of the resource.
            tags (Optional[List[str]]): A list of tags associated with the resource.
        """
        self.id = id
        self.name = name
        self.description = description
        self.tags = tags or []


class User(BaseModel):
    """A model representing a user."""
    
    def __init__(self, username: str, email: str, full_name: Optional[str] = None):
        """
        Initializes a new instance of the User class.
        
        Args:
            username (str): The username of the user.
            email (str): The email of the user.
            full_name (Optional[str]): The full name of the user.
        """
        self.username = username
        self.email = email
        self.full_name = full_name

# More models can be added following the same pattern
