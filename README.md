# Persistent To-Do API (FastAPI)

A lightweight backend service designed to manage a task list with permanent storage. This project demonstrates the transition from in-memory data structures to persistent file-based storage.

## 🚀 Key Features
* **Full CRUD**: Create, Read, Update, and Delete tasks.
* **Persistent Storage**: Data is saved to `task.json`, so it survives server restarts.
* **Smart ID Management**: Automatically generates unique IDs using `max() + 1` logic to prevent duplicates.
* **Robust Error Handling**: Uses defensive programming to handle missing IDs and malformed data.

## 🛠️ Tech Stack
* **Language**: Python 3.10+
* **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
* **Serialization**: JSON

## 🏃 How to Run
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/your-username/fastapi-persistent-todo.git](https://github.com/your-username/fastapi-persistent-todo.git)
   cd fastapi-persistent-todo
2. **Install dependencies:**
   ```bash
   pip install "fastapi[standard]"
3. **Start the server:**
   ```bash
   fastapi dev main.py
4. **Access Documentation:**
   Open http://127.0.0.1:8000/docs to interact with the API.




