import os
from secrets import token_urlsafe

class SecretKeyConfig:
    """
    This class will help to generate a secret key for the application.
    """
    def __init__(self):
        """Constructor for the class"""
        self.secret_key: str = os.getenv("SECRET_KEY", token_urlsafe(32))

    def get_secret_key(self) -> str:
        """Return the secret key"""
        return self.secret_key
    
    def add_in_env(self) -> None:
        """Add the secret key in the environment variable"""
        # first check if the secret key is already present in the environment variable
        if not os.getenv("SECRET_KEY"):
            os.environ["SECRET_KEY"] = self.secret_key
        else:
            self.secret_key = os.getenv("SECRET_KEY", "")
        

if __name__ == "__main__":
    secret_key = SecretKeyConfig()
    secret_key.add_in_env()
    print(secret_key.get_secret_key())
