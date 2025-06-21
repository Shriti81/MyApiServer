# 🚀 MyApiServer

A backend API server built using **FastAPI**, offering full **CRUD** functionality for managing items. This project uses **SQLite** with **SQLAlchemy ORM** and includes auto-generated API documentation. It's designed to be lightweight and easy to extend or integrate with a frontend.

---

## 📌 Table of Contents

- [🔧 Features](#-features)
- [📦 APIs Created](#-apis-created)
- [🛠️ Tech Stack](#️-tech-stack)
- [🗄️ Database Used](#️-database-used)
- [▶️ How to Run the Server](#️-how-to-run-the-server)
- [💻 How to Run the Frontend (Optional)](#-how-to-run-the-frontend-optional)
- [📬 How to Interact with the API](#-how-to-interact-with-the-api)
- [📂 Project Structure](#-project-structure)
- [📜 License](#-license)

---

## 🔧 Features

- ✅ Full CRUD functionality (Create, Read, Update, Delete)
- 🧠 SQLite database integration using SQLAlchemy
- 🔄 RESTful API endpoints
- 🌐 CORS enabled for frontend interaction
- 📑 Swagger/OpenAPI auto documentation

---

## 📦 APIs Created

| Method | Endpoint           | Description                  |
|--------|--------------------|------------------------------|
| POST   | `/items/`          | Create a new item            |
| GET    | `/items/`          | Get all items                |
| GET    | `/items/{item_id}` | Get a single item by ID      |
| PUT    | `/items/{item_id}` | Update an existing item      |
| DELETE | `/items/{item_id}` | Delete an item by ID         |
| GET    | `/`                | Health check / welcome route |

---

## 🛠️ Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Server**: Uvicorn

---

## 🗄️ Database Used

- **Type**: SQLite (lightweight, file-based DB)
- **Integration**:
  - `SessionLocal` and `Base` are defined using SQLAlchemy.
  - A `models.py` file contains the `Item` model and `init_db()` setup.
  - SQLite DB file (`database.db`) is automatically created when the app runs.

---

## ▶️ How to Run the Server

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/MyApiServer.git
   cd MyApiServer
