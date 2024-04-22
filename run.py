from taskmanager import app, db
from taskmanager.templates.models import Category, Task
import os

if __name__ == "__main__":
    with app.app_context():
        # Create the database tables
        db.create_all()

        # Start the Flask application
        app.run(
            host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG")
        )
