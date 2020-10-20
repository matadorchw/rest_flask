from flask import Blueprint
from flask import request
from ..utils.responses import response_with
from ..utils import responses as resp
from ..models.books import Book, BookSchema
from ..utils.database import db

book_routes = Blueprint('book_routes', __name__)


@book_routes.route('/', methods=['POST'])
def create_book():
    try:
        data = request.get_json()
        book_schema = BookSchema()
        book = book_schema.load(data)
        result = book_schema.dump(book.create())
        return response_with(resp.SUCCESS_201, value={'book': result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)
