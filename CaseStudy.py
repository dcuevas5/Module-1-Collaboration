from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

# Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_del_libro = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    editor = db.Column(db.String(100), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Welcome route
@app.route('/')
def home():
    return "Welcome to the Book API"

# Create a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(
        nombre_del_libro=data['nombre_del_libro'],
        autor=data['autor'],
        editor=data['editor']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully'})

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    result = []
    for book in books:
        result.append({
            'id': book.id,
            'nombre_del_libro': book.nombre_del_libro,
            'autor': book.autor,
            'editor': book.editor
        })
    return jsonify(result)

# Get a book by ID
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify({
        'id': book.id,
        'nombre_del_libro': book.nombre_del_libro,
        'autor': book.autor,
        'editor': book.editor
    })

# Update a book
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.get_json()
    book.nombre_del_libro = data['nombre_del_libro']
    book.autor = data['autor']
    book.editor = data['editor']
    db.session.commit()
    return jsonify({'message': 'Book updated successfully'})

# Delete a book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)


# GitHub https://github.com/dcuevas5/Module-1-Collaboration.git