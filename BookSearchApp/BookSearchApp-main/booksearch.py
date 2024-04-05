import streamlit as st
import requests
import logging
from dotenv import load_dotenv
import os

# Function to configure environment variables
def configure():
    load_dotenv()

# Import the CSS styles.css file
with open("styles.css") as style:
    st.markdown(f"<style>{style.read()}</style>", unsafe_allow_html=True)

    # Function to fetch book data from Google Books APIs
    def fetch_books(query,max_results = 20):
        url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults={max_results}&key={os.getenv('books_key')}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()
            return data
        except Exception as e:
            st.write(f"Error fetching books")
            return None    

    # Main function to run the app
    def main():
        st.title("Book Search App")

        # Initialize session state variables
        if 'last_query' not in st.session_state:
            st.session_state.last_query = ""
            st.session_state.results_displayed = False  # Initialize results display flag
            st.session_state.current_page = 1  # Initialize current page number

        # Input field for user to enter query
        query = st.text_input("Enter Book or Author Name", "", key="search_query", help="Type your search query and press Enter to search")

        # Event listener for "ENTER" key press
        if query:
            query = query.strip()  # Remove leading/trailing whitespaces
            if st.session_state.last_query != query:
                st.session_state.last_query = query
                st.session_state.results_displayed = False  # Reset results display flag
                st.session_state.current_page = 1  # Reset current page number to 1
        
        # Button to trigger book search
        if st.button("Search", key="search_button") or st.session_state.last_query:
            if st.session_state.last_query:
                query = st.session_state.last_query
                st.write(f"_Searching for books with query: {query}..._")
                logging.debug(f"Searching for books with query: {query}")
                books_data = fetch_books(query)
                if books_data and 'items' in books_data:
                    items_per_page = 5  # Number of items to display per page
                    total_items = len(books_data['items'])
                    total_pages = (total_items + items_per_page - 1) // items_per_page
                    start_index = (st.session_state.current_page - 1) * items_per_page

                    # Update current page before rendering UI
                    if st.session_state.current_page > total_pages:
                        st.session_state.current_page = total_pages
                    elif st.session_state.current_page < 1:
                        st.session_state.current_page = 1
                    start_index = (st.session_state.current_page - 1) * items_per_page
                    end_index = min(start_index + items_per_page, total_items)

                    for i, item in enumerate(books_data['items'][start_index:end_index], start=start_index):
                        volume_info = item.get('volumeInfo', {})
                        title = volume_info.get('title', 'No title available')
                        authors = volume_info.get('authors', ['No authors available'])
                        published_year = volume_info.get('publishedDate', 'Unknown')
                        preview_link = volume_info.get('previewLink', '')
                        description = volume_info.get('description', 'Unknown')
                        isbn = volume_info.get('industryIdentifiers', [])
                        isbn_str = ', '.join([f"{i['type']}: {i['identifier']}" for i in isbn]) if isbn else 'N/A'
                        book_link = item.get('selfLink', '')
                        page_count = volume_info.get('pageCount', 'Unknown')
                        published_date = volume_info.get('publishedDate', 'Unknown')
                        publisher = volume_info.get('publisher', 'Unknown')
                        language = volume_info.get('language', 'Unknown')
                        image_links = volume_info.get('imageLinks', {})
                        # Extracting buy link from saleInfo
                        sale_info = item.get('saleInfo', {})
                        buy_link = sale_info.get('buyLink', '')
                        ebook = sale_info.get('isEbook')
                        prices = sale_info.get('retailPrice', {})
                        amount = prices.get('amount', 'Unknown')
                        currency_code = prices.get('currencyCode', 'Unknown')
                        saleability_x = sale_info.get('saleability')
                        
                        try:
                            thumbnail = image_links.get('thumbnail', None)
                            thumbnail = thumbnail or "/Users/anandavii/ITM/SEM2/ITMD566/BookSearchApp/default_image.jpeg"  # Assign default value if thumbnail is None
                        except Exception as e:
                            st.warning("Error loading thumbnail image.")

                        st.image(thumbnail, caption="Book Cover" if thumbnail else "No Cover Available", width=100)
                        st.write(f"**Title:** {title}")
                        st.write(f"**Authors:** {', '.join(authors)}")
                        st.write(f"**Published Year:** {published_year}")

                        # Display "Click to Know More" button with a unique key
                        # Write a function for toggle functionality
                        if "button" not in st.session_state:
                            st.session_state.button = False
                        def toggle():
                            if st.session_state.button:
                                st.session_state.button = False
                            else:
                                st.session_state.button = True
                        if st.button("Click to Know More", on_click=toggle, key=f"know_more_button_{i}"): 
                            show_book_details(title, authors, isbn_str, thumbnail, description, publisher, page_count, language, published_date, preview_link, buy_link, ebook, amount, currency_code, saleability_x)
                        st.write("---")
                    # Pagination
                if total_pages > 1:
                    st.write(f"Page {st.session_state.current_page}/{total_pages}")
                    if st.button("Previous Page"):
                        st.session_state.current_page -= 1
                    if st.button("Next Page"):
                        st.session_state.current_page += 1
                elif books_data and 'error' in books_data:
                    st.write(f"Error: {books_data['error']['message']}")
                else:
                    st.write("No books found.")
            else:
                st.write("Please enter a search query.")
                
    # Function to display book details on new page
    def show_book_details(title, authors, isbn_str, thumbnail, description, publisher, page_count, language, published_date, preview_link, buy_link, ebook, amount, currency_code, saleability_x):
        preview_title = title.split(':')[0] if ':' in title else title  # Extracting the title part before ":"
        preview_text = f"{preview_title} - Book Preview"
        ebook_text = "Yes" if ebook else "No"
        saleability_text = "For Sale" if saleability_x == "FOR_SALE" else "Not For Sale"
        with st.expander("**About this edition**"):
            col1, col2 = st.columns(2)
            #st.image(thumbnail, caption="Book Cover" if thumbnail "" else "No Cover Available", width=200)
            if thumbnail is not None:
                st.image(thumbnail, caption="Book Cover", width=100)
            else:
                st.write("No Cover Available")
            col1.write(f"**Title:** {title}")
            col1.write(f"**Author(s):** {', '.join(authors)}")
            col1.write(f"**Publisher:** {publisher}")
            col1.write(f"**ISBN:** {isbn_str}")
            col2.write(f"**Page Count:** {page_count}")
            col2.write(f"**Language:** {language}")
            col2.write(f"**Ebook:** {ebook_text}")
            col2.write(f"**Pubished Date:** {published_date}")
            col1.write(f"**Preview:** [{preview_text}]({preview_link})")
            col2.write(f"**Available For Sale:** {saleability_text}")
            if saleability_x == "FOR_SALE":
                col2.write(f"**Buy This Book:** [Buy Now]({buy_link})")
                col1.write(f"**Price:** {amount} {currency_code}")
            st.write(f"**Description:** {description}")

# Main function to run the app
if __name__ == "__main__":
    main()
    configure()
