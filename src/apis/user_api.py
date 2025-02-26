from logging import Logger

from flask import Blueprint, request, jsonify

from src.repositories.user_repository import UserDataAccessObject
from src.models.users import User
from src.utils.exceptions import FlaskException

user_api = Blueprint('user_api', __name__)
logger: Logger = Logger(__name__)


@user_api.route('/user', methods=['POST'])
def create_user():
    """
    Creates a user
    curl -X POST http://127.0.0.1:8000/user -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john_doe@gmail.com, "password": "Password@123"}'
    Args:
        user (User): User object
    Returns:
        User: Returns the created user
    Raises:
        FlaskException: If any error occurs while creating user
    """
    try:
        payload = request.get_json()
        if not payload:
            raise FlaskException("Invalid request", status_code=400)
        
        payload.pop('id', None)
        payload.pop('_id', None)
        
        user = User(**payload)
        createduser = UserDataAccessObject.create_user(user)
        print(createduser)
        created_user = createduser.dict()
        print(type(created_user))
        
        created_user.pop('password')
        return jsonify(
            data=created_user,
            message= "User created successfully",
            status_code= 201
        )
    except ValueError as e:
        raise FlaskException(data=str(e), status_code=400)
    # We need to return a status messgae instead of the actual error message
    except FlaskException as e:
        logger.error(str(e))
        return jsonify(
            data=None,
            message= "User not created",
            status_code= 500
        )
    
@user_api.route('/user', methods=['GET'])
def get_all_user():
    """
    Gets all users
    Returns:
        list[User]: Returns a list of all users
    Raises:
        FlaskException: If any error occurs while fetching users
    """
    try:
        users = UserDataAccessObject.get_all_users()
        print(users)
        res: list[dict] = []
        for user in users:
            user = user.dict()
            user.pop('password')
            res.append(user)
        return jsonify(
            data=res,
            message= "Users fetched successfully",
            status_code= 200
        )
    except FlaskException as e:
        raise e
    

@user_api.route('/user/<id>', methods=['GET'])
def get_user_by_id(id: str):
    """
    Gets a user by id
    Args:
        id (str): Id of the user
    Returns:
        User: Returns the user
    Raises:
        FlaskException: If any error occurs while fetching user
    """
    try:
        user = UserDataAccessObject.get_user_by_id(id)
        print(user)
        # if not user:
        #     raise FlaskException("User not found", status_code=404)
        got_user = user.dict()
        got_user.pop('password')
        return jsonify(
            data=got_user,
            message= "User fetched successfully",
            status_code= 200
        )
    except FlaskException as e:
        return jsonify(
            data=None,
            message= "User not found",
            status_code= 404
        )

    
@user_api.route('/user/<id>', methods=['PUT'])
def update_user(id: str):
    """
    Updates a user
    Args:
        id (str): Id of the user
    Returns:
        User: Returns the updated user
    Raises:
        FlaskException: If any error occurs while updating user
    """
    try:
        payload = request.get_json()
        if not payload:
            raise FlaskException("Invalid request", status_code=400)
        
        payload.pop('id', None)
        payload.pop('_id', None)
        
        user = User(**payload)
        updated_user = UserDataAccessObject.update_user_by_id(id, user)
        updated_user = updated_user.dict()
        updated_user.pop('password')

        return jsonify(
            data=updated_user,
            message= "User updated successfully",
            status_code= 200
        )
    except ValueError as e:
        raise FlaskException(data=str(e), status_code=400)
    except FlaskException as e:
        return jsonify(
            data=None,
            message= "User not updated",
            status_code= 500
        )
    
@user_api.route('/user/<id>', methods=['DELETE'])
def delete_user(id: str):
    """
    Deletes a user
    Args:
        id (str): Id of the user
    Returns:
        User: Returns the deleted user
    Raises:
        FlaskException: If any error occurs while deleting user
    """
    try:
        UserDataAccessObject.delete_user_by_id(id)
        return jsonify(
            data=None,
            message= "User deleted successfully",
            status_code= 200
        )
    except FlaskException as e:
        raise e
