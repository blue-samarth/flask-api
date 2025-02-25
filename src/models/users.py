from pydantic import BaseModel, Field, validator, EmailStr
from bson import ObjectId

from src.utils.handle_passwords import PasswordHandle

class User(BaseModel):
    """Its a model for user"""
    id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    name: str
    email: EmailStr
    password: str

    
    @validator('password')
    def validate_and_hash_password(cls, password: str) -> str:
        """
        Validates the password and hashes it if not already hashed

        Requirements for password:
            - At least 6 characters long
            - At least one digit
            - At least one uppercase letter
            - At least one lowercase letter
            - At least one special character        
        """
        if len(password) < 6:
            raise ValueError("Password must be at least 6 characters long")
        if not any(char.isdigit() for char in password):
            raise ValueError("Password must contain at least one digit")
        if not any(char.isupper() for char in password):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(char.islower() for char in password):
            raise ValueError("Password must contain at least one lowercase letter")
        if not any(char in "!@#$%^&*()-+" for char in password):
            raise ValueError("Password must contain at least one special character")

        if PasswordHandle().is_password_hashed(password):
            return password
        return PasswordHandle().hashpassword(password)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            ObjectId: lambda x: str(x)
        }

    def dict(self, *args, **kwargs):
        """Overrides the dict method to remove the password field"""
        user_dict = super().dict(*args, **kwargs)
        if "_id" not in user_dict and "id" in user_dict:
            user_dict["_id"] = user_dict.pop("id")
        return user_dict
