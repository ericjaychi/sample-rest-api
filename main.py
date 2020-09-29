#main.py

# Import the Flask module that has been installed.
from flask import Flask, jsonify

# Creating a "books" JSON / dict to emulate data coming from a database.
books = [
	{
		"id": 1,
		"title": "Harry Potter and the Goblet of Fire",
		"author": "J.K. Rowling",
		"isbn": "1512379298"
	},
	{
		"id": 2,
		"title": "Lord of the Flies",
		"author": "William Golding",
		"isbn": "0399501487"
	}
]

# Creating a new "app" by using the Flask constructor. Passes __name__ as a parameter.
app = Flask(__name__)

# Annotation that allows the function to be hit at the specific URL.
@app.route("/")
# Generic Python function that returns "Hello world!"
def index():
	return "Hello world!"

# Annotation that allows the function to be hit at the specific URL. Indicates a GET HTTP method.
@app.route("/library/v1.0/books", methods=["GET"])
# Function that will run when the endpoint is hit.
def get_books():
	# Returns a JSON of the books defined above. jsonify is a Flask function that serializes the object for us.
	return jsonify({"books": books})

# Annotation that allows the function to be hit at the specific URL with a parameter. Indicates a GET HTTP method.
@app.route("/library/v1.0/books/<int:book_id>", methods=["GET"])
# This function requires a parameter from the URL.
def get_book(book_id):
	# Create an empty dictionary.
	result = {}

	# Loops through all the different books to find the one with the id that was entered.
	for book in books:
		# Checks if the id is the same as the parameter.
		if book["id"] == book_id:
			# Sets the result to the book and makes it a JSON.
			result = jsonify({"book": book})

	# Returns the book in JSON form or an empty dictionary. Should handle the error like 404, but will not cover here.
	return result

# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
	# Runs the Flask application only if the main.py file is being run.
	app.run()
