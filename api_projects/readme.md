#🚀 REST API & FastAPI Projects

## 🎯 Overview
This repository contains two powerful API-based projects that showcase both traditional RESTful APIs (Java) and modern FastAPI implementations (Python). These projects demonstrate how to build scalable, efficient, and high-performance APIs using different frameworks.

## 🛠️ Tech Stack
✅ FastAPI Instagram API (Python, FastAPI, Django)
FastAPI – High-performance backend framework
Django – Web framework for authentication & admin panel
Instagram Graph API – Fetches user media
SQLite – Lightweight database for storing media metadata
Requests Library – API calls & data retrieval
✅ REST API (Java-based Message/Profile Service)
Java – Core programming language
JAX-RS (Java API for RESTful Web Services) – REST API framework
Jersey – Java framework for building RESTful APIs
HashMap (In-memory Database) – Stores message & profile data
## 📌 Projects Breakdown
📸 1. FastAPI Instagram API (Python - FastAPI & Django)
This project integrates FastAPI with Instagram’s Graph API to fetch and display user media.

## 🔗 Key Features
✅ Fetches user media (images, videos) from Instagram
✅ Implements authentication using API tokens
✅ Uses FastAPI for high-speed API requests
✅ Uses Django for additional backend features

## 🏗️ How It Works
1️⃣ User makes an API request to fetch Instagram media
2️⃣ FastAPI fetches the data using the Instagram Graph API
3️⃣ The response contains media details (IDs, captions, URLs)
4️⃣ Data is rendered dynamically in the frontend

## 📌 API Endpoint

GET /instagram/media
Returns a list of media posts with captions, timestamps, and media URLs.

💬 2. REST API - Message & Profile Service (Java - JAX-RS, Jersey)
This project implements a Java-based RESTful API for managing messages and user profiles.

## 🔗 Key Features
✅ CRUD operations for messages (Create, Read, Update, Delete)
✅ CRUD operations for user profiles
✅ Uses JAX-RS & Jersey for RESTful services
✅ In-memory database using HashMap

## 🏗️ How It Works
1️⃣ Users interact with the API to manage messages & profiles
2️⃣ Data is stored in an in-memory HashMap
3️⃣ Each resource has endpoints to create, update, delete records

## 📌 API Endpoints
Message Service:
GET /messages   
GET /messages/{id}       
POST /messages 
PUT /messages/{id}  
DELETE /messages/{id}  

Profile Service:
GET /profiles     
GET /profiles/{username} 
POST /profiles 
PUT /profiles/{username} 
DELETE /profiles/{username}

## 🚀 Future Enhancements
🔹 Migrate Java API to Spring Boot for better scalability
🔹 Implement OAuth authentication in FastAPI
🔹 Add a frontend dashboard to visualize API data
🔹 Use a proper SQL/NoSQL database instead of in-memory storage

