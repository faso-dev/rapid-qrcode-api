import traceback
from pathlib import Path

from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from flask_migrate import Migrate
from sqlalchemy.exc import SQLAlchemyError

from database import db
from shared import ma


def create_app():
    app = Flask(__name__, static_folder='uploads', static_url_path='/')
    app.config.from_object('config')
    db.init_app(app)
    ma.init_app(app)
    Migrate(app, db)
    CORS(app)
    CORS(app, resources={r"/api/*": {
        "origins": "*",
    }})

    with app.app_context():
        from .users import user_api
        from .qrcode import qrcode_api

        @app.after_request
        def after_request(response):
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
            response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response

        @app.errorhandler(500)
        def handle_exception(err):
            """Return JSON instead of HTML for any other server error"""
            app.logger.error(f"Unknown Exception: {str(err)}")
            app.logger.debug(''.join(traceback.format_exception(etype=type(err), value=err, tb=err.__traceback__)))
            response = {"error": "Sorry, that error is on us, please contact support if this wasn't an accident"}
            return jsonify(response), 500

        @app.errorhandler(404)
        def handle_not_found(err):
            """Return JSON instead of HTML for any other server error"""
            app.logger.error(f"Unknown Exception: {str(err)}")
            app.logger.debug(''.join(traceback.format_exception(etype=type(err), value=err, tb=err.__traceback__)))
            response = {"error": "Sorry, it looks like that the requested resource doesn't exist"}
            return jsonify(response), 404

        @app.errorhandler(400)
        def handle_bad_request(err):
            """Return JSON instead of HTML for any other server error"""
            app.logger.error(f"Unknown Exception: {str(err)}")
            app.logger.debug(''.join(traceback.format_exception(etype=type(err), value=err, tb=err.__traceback__)))
            response = {"error": "Sorry, it looks like that is a bad request"}
            return jsonify(response), 400

        @app.errorhandler(405)
        def handle_method_not_allowed(err):
            """Return JSON instead of HTML for any other server error"""
            app.logger.error(f"Unknown Exception: {str(err)}")
            app.logger.debug(''.join(traceback.format_exception(etype=type(err), value=err, tb=err.__traceback__)))
            response = {"error": "Sorry, it looks like that method is not allowed"}
            return jsonify(response), 405

        @app.errorhandler(403)
        def handle_forbidden(err):
            """Return JSON instead of HTML for any other server error"""
            app.logger.error(f"Unknown Exception: {str(err)}")
            app.logger.debug(''.join(traceback.format_exception(etype=type(err), value=err, tb=err.__traceback__)))
            response = {"error": "Sorry, it looks like that you don't have permission to access this resource"}
            return jsonify(response), 403

        @app.errorhandler(401)
        def handle_unauthorized(err):
            """Return JSON instead of HTML for any other server error"""
            app.logger.error(f"Unknown Exception: {str(err)}")
            app.logger.debug(''.join(traceback.format_exception(etype=type(err), value=err, tb=err.__traceback__)))
            response = {
                "error": "Sorry, it looks like that you are not authorized to access this resource",
                "description": "Vous devez vous connecter pour accéder à cette ressource",
                "code": "unauthorized"
            }
            return jsonify(response), 401

        # error handler for SQLAlchemyError
        @app.errorhandler(SQLAlchemyError)
        def handle_sqlalchemy_error(err):
            """Return JSON instead of HTML for any other server error"""
            app.logger.error(f"Unknown Exception: {str(err)}")
            app.logger.debug(''.join(traceback.format_exception(etype=type(err), value=err, tb=err.__traceback__)))
            response = {
                "error": "Sorry, it looks like that there was an internal server error",
                "message": "Une erreur interne est survenue, veuillez contacter le support si ce n'est pas un accident",
                "code": "internal_server_error"
            }
            return jsonify(response), 500

        # Python Exceptions
        @app.errorhandler(Exception)
        def handle_exception(err):
            """Return JSON instead of HTML for any other server error"""
            app.logger.error(f"Unknown Exception: {str(err)}")
            app.logger.debug(''.join(traceback.format_exception(etype=type(err), value=err, tb=err.__traceback__)))
            response = {
                "error": "Sorry, that error is on us, please contact support if this wasn't an accident",
                "message": "Une erreur inconnue est survenue, veuillez contacter le support si ce n'était pas un "
                           "accident",
                "code": "internal_server_error"
            }
            return jsonify(response), 500

        # ----------------------------------------
        # GET /uploads/<path:filename>
        # ----------------------------------------
        @app.route('/api/v1/assets/<path:filename>')
        def get_file(filename):
            return send_from_directory(Path('../../') / app.config['UPLOAD_FOLDER'], filename)

        app.register_blueprint(user_api)
        app.register_blueprint(qrcode_api)

    return app
