# 📝 Profile & Message Service - RESTful API

## 🎯 Overview
The Profile & Message Service API is a RESTful web service designed to manage user profiles and messages efficiently. Built using Java (JAX-RS), this project enables users to create, retrieve, update, and delete both profiles and messages. It follows a modular structure to separate concerns, ensuring clean API design and maintainability.

This project serves as a foundational backend system for applications requiring user management and messaging functionality, making it an excellent demonstration of REST API design, resource handling, and JSON-based communication.

## 🛠️ Tech Stack
Java – Core programming language
JAX-RS (Java API for RESTful Web Services) – API framework
JSON – Data format for request/response
HashMap (Java Collections) – In-memory data storage
Simulated Database – Temporary storage for profiles and messages

## 📌 Key Features
### 📂 Profile Service
✅ Retrieve All Profiles – Fetches a list of all registered user profiles
✅ Get a Specific Profile – Retrieves user details based on profile name
✅ Create a New Profile – Allows users to register new profiles
✅ Update an Existing Profile – Modifies profile details
✅ Delete a Profile – Removes a user profile

### 📩 Message Service
✅ Retrieve All Messages – Fetch all stored messages
✅ Get a Specific Message – Retrieve a message by ID
✅ Add a New Message – Create and store a message
✅ Update an Existing Message – Modify a message's content
✅ Delete a Message – Remove a message by ID

## 🏗️ Project Structure
This project is structured using the MVC (Model-View-Controller) pattern, ensuring separation between data, business logic, and API endpoints:

## Model (Data Layer)

Defines the structure for Profile (ID, name, first name, last name, creation date)
Defines the structure for Message (ID, message content, author, creation date)
Service (Business Logic Layer)

Manages profile operations such as creation, update, deletion
Manages message operations including CRUD functionality
Resource (Controller Layer)

Handles API requests and maps them to corresponding service methods
Implements HTTP methods (GET, POST, PUT, DELETE)
Database (Simulated Storage Layer)

Stores profile and message data in an in-memory HashMap
Provides a simple way to persist data temporarily
## 🌍 How It Works
🌟 Profile API Endpoints
GET /profiles → Fetch all profiles
GET /profiles/{profileName} → Retrieve a specific profile
POST /profiles → Create a new profile
PUT /profiles/{profileName} → Update an existing profile
DELETE /profiles/{profileName} → Remove a profile
📨 Message API Endpoints
GET /messages → Fetch all messages
GET /messages/{id} → Retrieve a specific message
POST /messages → Add a new message
PUT /messages/{id} → Update an existing message
DELETE /messages/{id} → Remove a message
Each endpoint follows RESTful principles, ensuring a structured and efficient API for user management and messaging.

## 🚀 Future Enhancements
🔹 Database Integration – Implementing a relational database like MySQL or PostgreSQL for persistent storage
🔹 User Authentication – Adding security layers for profile-based access control
🔹 Enhanced Messaging Features – Implementing features like message threading, attachments, and real-time updates
🔹 Frontend Integration – Developing a web or mobile interface for user-friendly interaction

