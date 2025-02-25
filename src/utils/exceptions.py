
class FlaskException(Exception):
    def __init__(self, message: str = "An ERROR OCCURRED", status_code: int = 400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

    @property
    def to_dict(self):
        return {
            "message": self.message,
            "status_code": self.status_code
        }
