# ⚡ FastAPI Blog API (Learning to Production)

## 📌 What is this?

A REST API built using FastAPI that demonstrates:

* Routing
* Data validation
* Request handling
* Basic CRUD patterns

This project simulates a **blog backend system**, which is a common real-world API use case.

---

## 🚀 Why this matters

FastAPI is widely used for:

* Backend services
* AI model deployment
* Microservices

This project shows **practical API development skills**, not just theory.

---

## ⚙️ Tech Stack

* Python
* FastAPI
* Pydantic
* SQLite (local DB)

---

## 🧠 Features

* Dynamic routes (`/blog/{id}`)
* POST & GET endpoints
* Request validation using Pydantic models
* Simple database integration

---

## 📡 Example Endpoints

### GET `/blog/{id}`

Fetch blog by ID

### POST `/blog`

Create a new blog entry

---

## 🛠️ Setup

```bash
git clone https://github.com/WaseefUllahh/fast-api-learning
cd fast-api-learning

pip install -r requirements.txt
uvicorn main:app --reload
```

---

## 💡 Improvements (Important)

* Add full CRUD (PUT, DELETE)
* Add authentication (JWT)
* Use PostgreSQL instead of SQLite
* Add Swagger customization

---

## 🎯 Real Use Cases

* Backend for mobile/web apps
* AI model APIs
* SaaS products

---

## 👨‍💻 Author

Waseef Ullah
