from flask import Flask, request

# Create an instance of the Flask application
app = Flask(__name__)

# Define a route for the root URL '/'
@app.route('/')
def index():
    # Get the value of the 'user' query parameter from the URL
    user = request.args.get('user')

    # Return a greeting including the user's name
    return f"Hello {user}!"

# Run the app when this script is executed directly
if __name__ == '__main__':
    # Run the Flask app on host 0.0.0.0 and port 8000
    app.run(host='0.0.0.0', port=8000)

