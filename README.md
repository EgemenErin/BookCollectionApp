
# Book Collection App

A simple Flask web application to manage a collection of books. This app allows you to add books with their title, author, and rating, which are stored in a SQLite database.
![image](https://github.com/user-attachments/assets/b5f86c4f-2d4b-4b1b-97b8-7715db137495)



## Features
- View a list of all books in the collection on the homepage.
- Add a new book with its title, author, and rating through a form.
- Remove a book from the database
- Change Book's rating by accessing and editing the database
- Data is stored persistently in a SQLite database.
- <img width="1430" alt="image" src="https://github.com/user-attachments/assets/f8a8d1a1-3351-454d-a63a-13c27f631737">
- <img width="1425" alt="image" src="https://github.com/user-attachments/assets/0908af78-1bdd-4e94-9ea9-bb8ebd34c509">
![image](https://github.com/user-attachments/assets/3b476324-0317-46d3-b043-d2c149217ff1)




## Technologies Used
- Python
- Flask
- SQLite
- Flask-WTF (for forms)
- Bootstrap (for styling)

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/book-collection-app.git
   cd book-collection-app
   ```

2. **Create a Virtual Environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # On Windows use `.venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python main.py
   ```
   Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser to view the app.

## Usage
- Go to the homepage to view the list of books. If there are no books, it will show a message: "Library is empty."
- Click on "Add New Book" to add a new book to the collection.
- Enter the book title, author, and rating, then click "Submit".
- The app will redirect to the homepage, displaying the updated list of books.

## Project Structure
- **main.py**: The main application file with Flask routes and database setup.
- **templates/**: Folder containing HTML templates for rendering pages.
- **static/**: Folder for static files like CSS and images.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Author
This app was developed by [Your Name](https://github.com/yourusername).

