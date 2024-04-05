import streamlit as st

class BookDetails:
    def __init__(self, title, authors, published_year, isbn_str, thumbnail):
        """
        Initialize the BookDetails object with book information.

        Parameters:
        - title (str): The title of the book.
        - authors (list): A list of authors of the book.
        - published_year (str): The year the book was published.
        - isbn_str (str): The ISBN number of the book.
        - thumbnail (str): URL of the book cover image.
        """
        self.title = title
        self.authors = authors
        self.published_year = published_year
        self.isbn_str = isbn_str
        self.thumbnail = thumbnail

    def show_details(self):
        """
        Display book details using Streamlit.
        """
        st.title("Book Details")
        st.image(self.thumbnail, caption="Book Cover" if self.thumbnail else "No Cover Available", width=150)
        st.write(f"Title: {self.title}")
        st.write(f"Authors: {', '.join(self.authors)}")
        st.write(f"Published Year: {self.published_year}")
        st.write(f"ISBN: {self.isbn_str}")
