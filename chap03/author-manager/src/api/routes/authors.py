from flask import Blueprint
from flask import request
from flask_jwt_extended import jwt_required
from ..utils.responses import response_with
from ..utils import responses as resp
from ..models.authors import Author, AuthorSchema
from ..utils.database import db

author_routes = Blueprint('author_routes', __name__)


@author_routes.route('/', methods=['POST'])
@jwt_required
def create_author():
    try:
        data = request.get_json()
        author_schema = AuthorSchema()
        author = author_schema.load(data)
        result = author_schema.dump(author.create())
        return response_with(resp.SUCCESS_201, value=({'author': result}))
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@author_routes.route('/', methods=['GET'])
def get_author_list():
    fetched = Author.query.all()
    author_schema = AuthorSchema(many=True, only=['first_name', 'last_name', 'id'])
    authors = author_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={'authors': authors})


@author_routes.route('/<int:author_id>', methods=['GET'])
def get_author_detail(author_id):
    fetched = Author.query.get_or_404(author_id)
    author_schema = AuthorSchema()
    author = author_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={'author': author})


@author_routes.route('/<int:id>', methods=['PUT'])
def update_author_detail(id):
    data = request.get_json()
    get_auth = Author.query.get_or_404(id)
    get_auth.first_name = data['first_name']
    get_auth.last_name = data['last_name']
    db.session.add(get_auth)
    db.session.commit()
    author_schema = AuthorSchema()
    author = author_schema.dump(get_auth)
    return response_with(resp.SUCCESS_200, value={'author': author})


@author_routes.route('/<int:id>', methods=['PATCH'])
def modify_author_detail(id):
    data = request.get_json()
    get_auth = Author.query.get_or_404(id)
    if data.get('first_name'):
        get_auth.first_name = data['first_name']
    if data.get('last_name'):
        get_auth.last_name = data['last_name']
    db.session.add(get_auth)
    db.session.commit()
    author_schema = AuthorSchema()
    author = author_schema.dump(get_auth)
    return response_with(resp.SUCCESS_200, value={'author': author})


@author_routes.route('/<int:id>', methods=['DELETE'])
def delete_author(id):
    get_author = Author.query.get_or_404(id)
    db.session.delete(get_author)
    db.session.commit()
    return response_with(resp.SUCCESS_204)
