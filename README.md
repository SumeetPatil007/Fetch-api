# FastAPI Machine Test

## Technologies Used
- FastAPI
- SQLAlchemy
- SQLite
- Python

---

## Installation

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows
```bash
venv\Scripts\activate
```

#### Mac/Linux
```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Server

```bash
uvicorn main:app --reload
```

---

## Swagger Documentation

Open in browser:

```bash
http://127.0.0.1:8000/docs
```

---

## Database Design

### Category Table
- id
- name

### Product Table
- id
- name
- price
- category_id

Relationship:
One Category -> Multiple Products
