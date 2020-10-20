import logging
import os
from flask import Flask
from flask import jsonify
from api.config.config import ProductionConfig, TestingConfig, DevelopmentConfig

from api.utils.database import db
from api.utils.responses import response_with
from api.utils import responses as resp

from api.routes.authors import author_routes


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


app = Flask(__name__)

if os.environ.get('WORK_ENV') == 'PROD':
    app_config = ProductionConfig
elif os.environ.get('WORK_ENV') == 'TEST':
    app_config = TestingConfig
else:
    app_config = DevelopmentConfig

app.config.from_object(app_config)

app.register_blueprint(author_routes, url_prefix='/api/authors')


@app.after_request
def add_header(response):
    return response


@app.errorhandler(400)
def bad_request(e):
    logging.error(e)
    return response_with(resp.BAD_REQUEST_400)


@app.errorhandler(500)
def server_error(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_500)


@app.errorhandler(404)
def not_found(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_404)


db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', use_reloader=True)
