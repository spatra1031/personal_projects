# 📸 Instagram Media Fetcher - Django API

## 🎯 Overview
The Instagram Media Fetcher is a Django-based web application that interacts with the Instagram Graph API to fetch and display media content from a user's Instagram account. This project showcases how to integrate third-party APIs into a Django web framework, making it an excellent reference for developers looking to work with social media APIs, authentication, and data retrieval.

This application provides an interface to fetch, process, and display Instagram media items, including images, videos, and captions.

## 🛠️ Tech Stack
Python – Core programming language
Django – Web framework for backend logic
Instagram Graph API – Fetches Instagram media content
Requests Library – Handles API requests
SQLite – Default database for Django

## 📌 Key Features
✅ Fetch Instagram Media – Retrieve media content (images, videos) with captions
✅ User Authentication – Uses an access token for secure API access
✅ Data Processing – Extracts media type, media URL, username, and timestamp
✅ Django Template Rendering – Displays media dynamically on a web page
✅ Modular Structure – Cleanly separated views, URLs, and settings

## 🌍 How It Works
🔗 API Integration
The application uses Instagram’s Graph API to fetch user media.
A valid access token is required for authentication.
The request retrieves media IDs, captions, and URLs for display.
📌 API Endpoint
https://graph.instagram.com/me/media?fields=id,caption&access_token=<YOUR_ACCESS_TOKEN>

🖥️ User Flow
1️⃣ User visits the application.
2️⃣ Django sends a request to the Instagram API.
3️⃣ The response includes media details (images/videos, captions, timestamps).
4️⃣ Django renders the content in a clean UI.

## 🚀 Future Enhancements
🔹 OAuth 2.0 Authentication – Implement a secure login system
🔹 Database Storage – Save media metadata in a database
🔹 UI Improvements – Better styling and dynamic interactions
🔹 Error Handling – Graceful handling of API failures

