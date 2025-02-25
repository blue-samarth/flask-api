# here we will describe the standard responses of an api call
from flask import jsonify

class APIResponse:
    """
    This is a standard API response model
    """
    def __init__(self, status_code, data=None, message=None):
        self.data: any = data
        self.message: str = message
        self.status_code: int = status_code
        self.success: bool = True if 200 <= status_code < 300 else False

    def to_response(self) -> tuple:
        """
        Will return a response object
        """

        return jsonify(
            {
                "data": self.data,
                "message": self.message,
                "success": self.success
            }), self.status_code
        