from flask import Blueprint, request
from ..utils.responses import response_with
from ..utils import responses as resp
from ..models.users import User, UserSchema
from ..utils.database import db
from flask_jwt_extended import create_access_token

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        data['password'] = User.generate_hash(data['password'])
        user_schema = UserSchema()
        user = user_schema.load(data)
        result = user_schema.dump(user.create())
        return response_with(resp.SUCCESS_201, value={'user': result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@user_routes.route('/login', methods=['POST'])
def authenticate_user():
    try:
        data = request.get_json()
        current_user = User.find_by_username(data['username'])
        if not current_user:
            return response_with(resp.SERVER_ERROR_404)
        if User.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity=data['username'])
            return response_with(resp.SUCCESS_201,
                                 value={'message': 'Logged in as {}'.format(current_user.username),
                                        'access_token': access_token})
        else:
            return response_with(resp.UNAUTHORIZED_403)
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)
