    import os
    from flask import Flask
    from configs.settings import DEBUG

    app = Flask(__name__)
    app.config['DEBUG'] = DEBUG

    @app.route('/')
    def home():
        return 'Welcome to the Payment Processor App!'

    if __name__ == '__main__':
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port)
    DEBUG = True
    app.run(host='0.0.0.0', port=5000, debug=True)

# Import necessary modules for the application
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payment_processor.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models to ensure they are known to Flask-Migrate
from models import *



