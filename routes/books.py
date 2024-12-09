from flask import Blueprint, request, jsonify
from extensions import db
from models import Book
from flask_jwt_extended import jwt_required


books_bp = Blueprint('books_bp', __name__)


@books_bp.route('/add', methods=['POST'])
@jwt_required()
def add_book():
    data = request.get_json()
    new_book = Book(
        title=data['title'],
        author=data['author'],
        year=data['year']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Book added successfully!"}), 201

@books_bp.route('/list', methods=['GET'])
def list_books():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)
    search_query = request.args.get('search', '')

    query = Book.query
    if search_query:
        query = query.filter(
            (Book.title.ilike(f"%{search_query}%")) |
            (Book.author.ilike(f"%{search_query}%"))
        )

    paginated_books = query.paginate(page=page, per_page=per_page, error_out=False)
    books_data = [
        {"id": book.id, "title": book.title, "author": book.author, "year": book.year}
        for book in paginated_books.items
    ]
    return jsonify({
        "books": books_data,
        "total": paginated_books.total,
        "page": paginated_books.page,
        "pages": paginated_books.pages
    }), 200


@books_bp.route('/update/<int:id>', methods=['PUT'])
@jwt_required()
def update_book(id):
    data = request.get_json()
    book = Book.query.get_or_404(id)
    book.title = data.get("title", book.title)
    book.author = data.get("author", book.author)
    book.year = data.get("year", book.year)

    db.session.commit()
    return jsonify({"message": "Book updated successfully!"}), 200


@books_bp.route('/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted successfully!"}), 200
