# Import flask dependency
from flask import Flask

# Create a new flask app instance
app = Flask(__name__)

# Create a flask route
# First define the starting point (root)
@app.route('/')

# Create a function called hello_world()
@app.route('/')
def hello_world():
    return 'Hello world'