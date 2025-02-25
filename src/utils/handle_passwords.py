import secrets

from passlib.context import CryptContext

class PasswordHandle:
    def __init__(self):
        self.pwd_context = CryptContext(
            schemes=["argon2", "bcrypt"],
            default="argon2",
            deprecated="auto"
        )
    
    def hashpassword(self, password: str) -> str:
        return self.pwd_context.hash(password)
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)
    
    def is_password_hashed(self, password: str) -> bool:
        if not password:    return False
        try:
            return self.pwd_context.identify(password) is not None
        except Exception:
            return False
    
    def generate_jwt_secret(self) -> str:
        return secrets.token_urlsafe(32)
