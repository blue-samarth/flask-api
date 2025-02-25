import pymongo
from src import mongo
from src.models.users import User
from src.utils.exceptions import FlaskException

class UserDataAccessObject:

    @staticmethod
    def find_user_by_email(email: str) -> User|None:
        """
        Finds a user by email
        Args:
            email (str): Email of the user
        Returns:
            User|None: Returns a user if found else None
        Raises:
            FlaskException: If any error occurs while fetching user
        """
        try:
            user = mongo.db.users.find_one({"email": email})
            if user:
                return User(**user)
            return None
        except Exception as e:
            raise FlaskException(str(e))
        
    @staticmethod
    def create_user(user: User) -> User:
        """
        Creates a user
        Args:
            user (User): User object
        Returns:
            User: Returns the created user
        Raises:
            FlaskException: If any error occurs while creating user
        """
        try:
            res = mongo.db.users.insert_one(user.dict(by_alias=True))
            if not res.acknowledged:
                raise FlaskException("User not created", status_code=500)
            created_user = mongo.db.users.find_one({"email": user.email})
            return User(**created_user)
        except Exception as e:
            raise FlaskException(str(e))
        
    @staticmethod
    def get_all_user() -> list[User]:
        """
        Gets all users
        Returns:
            list[User]: Returns a list of all users
        Raises:
            FlaskException: If any error occurs while fetching users
        """
        try:
            users: list[dict] = []
            cursor:pymongo.cursor.Cursor = mongo.db.users.find()
            for user in cursor:
                user['_id'] = str(user['_id'])
                users.append(User(**user))
            return users
        except Exception as e:
            raise FlaskException(str(e))
        
    @staticmethod
    def update_user(user: User) -> User:
        """
        Updates a user
        Args:
            user (User): User object
        Returns:
            User: Returns the updated user
        Raises:
            FlaskException: If any error occurs while updating user
        """
        try:
            if mongo.db.users.find_one({"email": user.email}):
                res = mongo.db.users.update_one({"email": user.email}, {"$set": user.dict(by_alias=True)})
                if not res.acknowledged:
                    raise FlaskException("User not updated", status_code=500)
                updated_user = mongo.db.users.find_one({"email": user.email})
                return User(**updated_user)
            raise FlaskException("User not found", status_code=404)
        except Exception as e:
            raise FlaskException(str(e))
        
    @staticmethod
    def delete_user(email: str) -> None:
        """
        Deletes a user
        Args:
            email (str): Email of the user
        Raises:
            FlaskException: If any error occurs while deleting user
        """
        try:
            res = mongo.db.users.delete_one({"email": email})
            if not res.acknowledged:
                raise FlaskException("User not deleted", status_code=500)
        except Exception as e:
            raise FlaskException(str(e))
