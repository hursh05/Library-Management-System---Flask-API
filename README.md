# Library-Management-System---Flask-API

3. Set Up a Virtual Environment
Create and activate a virtual environment:

On Windows:
python -m venv venv
venv\Scripts\activate

4. Install Required Dependencies
Install all dependencies using pip:
pip install -r requirements.txt

5. Run the Application
Start the server:
python app.py
The server will run at:
http://127.0.0.1:5000
6. Test the Endpoints
The server exposes the following routes:

Authentication Routes
Register User: POST /auth/register
Login User: POST /auth/login
Books Routes
List Books: GET /books/list
Add a Book: POST /books/add
Search Books by Title or Author: GET /books/search
You can use tools like Postman or cURL to interact with these routes.

Design Choices Made
Framework Choice: Flask

Flask was chosen for its simplicity, ease of setup, and lightweight nature. It supports rapid development of REST APIs and microservices.
Blueprint Structure

Blueprints (auth_bp and books_bp) were created for better organization and maintainability. This modular approach ensures different functionality resides in separate modules.
Database Integration

SQLite is used with SQLAlchemy ORM for simplicity and ease of use in a small project context.
Future scalability will allow swapping SQLite with PostgreSQL or MySQL.
Token-based Authentication

JWT (JSON Web Token) is implemented for authentication. This ensures stateless, secure communication between users and the server.
Pagination for Book Listing

Pagination is implemented to avoid large responses for book listings and to optimize performance.


Assumptions & Limitations
Assumptions
Database is SQLite-based

The application uses SQLite for simplicity. For production, switching to a production-grade database like PostgreSQL or MySQL is recommended.
The server runs locally

The server is expected to run locally for development purposes. Deployment to production requires additional configuration.
The user authentication is simplified

Only the email and password combination are considered for authentication without advanced edge case handling like brute-force attack prevention.
Limitations
Limited Data Persistence

SQLite will lose data when the server stops unless data persistence mechanisms are added.
Authentication Security

Token expiration and additional security features could be implemented for production.
Search is Simple

The search only allows querying by book title or author using simple LIKE operations. Advanced full-text search isn't implemented.
Edge Case Handling

Error handling is minimal. Additional error-handling mechanisms should be implemented in a real-world scenario.
