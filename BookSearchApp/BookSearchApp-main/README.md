# BookSearchApp

# Objective
The BookSearchApp aims to provide users with an intuitive and efficient way to search for books and retrieve detailed information using the Google Books API. The app offers a streamlined user experience to find books by title or author and displays comprehensive details about each book, including the cover image, authors, publication year, ISBN, and more.

# Process
Setup and Configuration:

The app uses the streamlit library for creating the user interface.
Environment variables are configured using dotenv to securely manage the Google Books API key.
User Interaction:

Users enter a book title or author name in a text input field.
Upon entering a query, the app fetches relevant book data from the Google Books API.
Results are displayed with pagination, showing book covers and brief details.
Displaying Book Details:

Users can click on a button to view more details about a specific book.
Detailed information includes the book's title, authors, publication year, ISBN, cover image, description, publisher, page count, language, and more.
The app also provides links for book previews and purchase options if available.
Outcome
The BookSearchApp offers a user-friendly interface to search for books and view detailed information. It efficiently integrates with the Google Books API to provide accurate and comprehensive book details, enhancing the book discovery experience for users.

# Key Features:
Search Functionality: Users can search for books by title or author.
Pagination: Results are displayed with pagination for easy navigation.
Detailed Book Information: Comprehensive details are shown for each book, including cover image, description, and links for preview and purchase.
Interactive UI: The app uses streamlit to create an interactive and responsive user interface.

# How to Use:
Clone the repository.
Install the required dependencies.
Configure the environment variables with your Google Books API key.
Run the app using streamlit run booksearchapp.py.

git clone https://github.com/yourusername/BookSearchApp.git

cd BookSearchApp

pip install -r requirements.txt

streamlit run booksearchapp.py

Feel free to reach out if you have any questions or suggestions!

