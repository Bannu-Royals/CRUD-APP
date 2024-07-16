from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import random

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Use pymysql as the MySQL connector
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI').replace('mysql://', 'mysql+pymysql://')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.environ.get('SECRET_KEY')

db = SQLAlchemy(app)

# Define your model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

# Ensure database tables are created or migrated
with app.app_context():
    db.create_all()

def generate_unique_id():
    while True:
        new_id = random.randint(1000, 9999)
        if not Item.query.get(new_id):
            return new_id

# Routes for CRUD operations
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view')
def view_items():
    try:
        items = Item.query.all()
        return render_template('view.html', items=items)
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        try:
            name = request.form['name']
            description = request.form['description']
            if name:
                new_item_id = generate_unique_id()
                new_item = Item(id=new_item_id, name=name, description=description)
                db.session.add(new_item)
                db.session.commit()
                return redirect(url_for('view_items'))
            # Handle validation errors here
        except Exception as e:
            return f"An error occurred: {str(e)}", 500
    return render_template('add_item.html')

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    try:
        item = Item.query.get_or_404(item_id)
        if request.method == 'POST':
            item.name = request.form['name']
            item.description = request.form['description']
            db.session.commit()
            return redirect(url_for('update_items'))
        return render_template('edit_item.html', item=item)
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

@app.route('/delete/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    try:
        item = Item.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return redirect(url_for('update_items'))
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

@app.route('/update', methods=['GET'])
def update_items():
    try:
        items = Item.query.all()
        return render_template('update_item.html', items=items)
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

# Export the app as a serverless function
def handler(event, context):
    from flask import request
    from werkzeug.datastructures import Headers

    # Convert the AWS Lambda event object to Flask's WSGI environment
    headers = Headers(event["headers"])
    environ = {
        "REQUEST_METHOD": event["httpMethod"],
        "SCRIPT_NAME": "",
        "PATH_INFO": event["path"],
        "QUERY_STRING": event["queryStringParameters"] or "",
        "SERVER_NAME": "lambda",
        "SERVER_PORT": "5000",
        "SERVER_PROTOCOL": "HTTP/1.1",
        "wsgi.version": (1, 0),
        "wsgi.url_scheme": "http",
        "wsgi.input": event["body"],
        "wsgi.errors": "",
        "wsgi.multithread": False,
        "wsgi.multiprocess": False,
        "wsgi.run_once": True,
        "wsgi.headers": headers,
    }

    # Call the Flask application with the WSGI environment
    with app.app_context():
        try:
            response = app(environ, start_response)
        except Exception as e:
            return {
                "statusCode": 500,
                "body": f"An error occurred: {str(e)}"
            }

    return {
        "statusCode": response.status_code,
        "headers": dict(response.headers),
        "body": response.data.decode("utf-8"),
    }
