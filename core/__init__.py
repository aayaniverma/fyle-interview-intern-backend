from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlite3 import Connection as SQLite3Connection

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./store.sqlite3'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # this is to enforce fk (not done by default in sqlite3)
    @event.listens_for(Engine, "connect")
    def _set_sqlite_pragma(dbapi_connection, connection_record):
        if isinstance(dbapi_connection, SQLite3Connection):
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON;")
            cursor.close()

    # Import and register blueprints/routes here
    from core.apis.assignments.principal import principal_assignments_resources
    app.register_blueprint(principal_assignments_resources)

    # Import models here to avoid circular imports
    with app.app_context():
        from core.models import Assignment  # Ensure the import is here

        db.create_all()

    return app

# Create the Flask app instance
app = create_app()

if __name__ == '__main__':
    app.run()
