# 📦 Full Stack Items App

A full-stack web application built with **FastAPI** (Python) backend and **HTML/CSS/JS** frontend, connected to a **SQLite** database via **SQLAlchemy ORM**.

---

## 🚀 Live Demo

- **Public API (ngrok):** https://digraphic-akilah-nonfluidly.ngrok-free.dev
- **API Docs (Swagger):** https://digraphic-akilah-nonfluidly.ngrok-free.dev/docs

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI (Python) |
| Database | SQLite |
| ORM | SQLAlchemy |
| Frontend | HTML / CSS / JavaScript |
| Public URL | ngrok |
| Version Control | Git + GitHub |

---

## 📁 Project Structure

```
fullstack-app/
├── backend/
│   ├── main.py            # FastAPI app with all endpoints
│   ├── requirements.txt   # Python dependencies
│   └── items.db           # SQLite database (auto-created)
└── frontend/
    └── index.html         # Web UI (HTML/CSS/JS)
```

---

## ⚙️ Setup & Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Karibandibaba/fullstack-app.git
cd fullstack-app
```

### 2. Install dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 3. Run the backend
```bash
python -m uvicorn main:app --reload
```
Backend runs at: `http://127.0.0.1:8000`

### 4. Open the frontend
Open `frontend/index.html` using Live Server in VS Code.

---

## 📦 Dependencies

```
fastapi
uvicorn[standard]
sqlalchemy
pydantic
```

---

## 📡 API Endpoints

### GET /items
Returns all items from the database.

**Request:**
```
GET http://127.0.0.1:8000/items
```

**Response:**
```json
[
  {
    "id": 1,
    "name": "Laptop",
    "description": "My work laptop",
    "created_at": "2026-03-09T10:00:00"
  }
]
```

---

### POST /items
Adds a new item to the database.

**Request:**
```
POST http://127.0.0.1:8000/items
Content-Type: application/json
```

**Body:**
```json
{
  "name": "Laptop",
  "description": "My work laptop"
}
```

**Response:**
```json
{
  "id": 1,
  "name": "Laptop",
  "description": "My work laptop",
  "created_at": "2026-03-09T10:00:00"
}
```

---

### PUT /items/{id}
Updates an existing item.

**Body:**
```json
{
  "name": "Updated Name",
  "description": "Updated description"
}
```

---

### DELETE /items/{id}
Deletes an item by ID.

**Response:**
```json
{
  "message": "Item 1 deleted"
}
```

---

## 🧪 Testing with Postman

| Step | Method | URL | Details |
|---|---|---|---|
| 1 | GET | `/items` | Returns empty array initially |
| 2 | POST | `/items` | Add item with JSON body |
| 3 | GET | `/items` | Now shows added item |
| 4 | PUT | `/items/1` | Update item by id |
| 5 | DELETE | `/items/1` | Delete item by id |

---

## 🌍 Making Backend Public (ngrok)

```bash
ngrok http 8000
```

Copy the generated URL and update `frontend/index.html`:
```js
const API = "https://your-ngrok-url.ngrok-free.app";
```

---

## ✅ Features

- ✅ View all items (GET)
- ✅ Add new items (POST)
- ✅ Update existing items (PUT)
- ✅ Delete items (DELETE)
- ✅ Data persists in SQLite database
- ✅ CORS enabled for frontend-backend communication
- ✅ Auto-generated Swagger API docs at `/docs`
- ✅ Publicly accessible via ngrok
- ✅ Frontend dynamically fetches and displays items

---

## 👨‍💻 Author

**Karibandibaba**
GitHub: [@Karibandibaba](https://github.com/Karibandibaba)
