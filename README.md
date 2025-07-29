### <img width="50" height="50" alt="clapperboard" src="https://github.com/user-attachments/assets/5a148c5e-8507-4ed5-83db-597e03cb00fc" />  Movie Explorer API

♨️ A Back-End application to manage and explore movies, directors, actors, and genres using **FastAPI** (backend) and **MongoDB**.

---

## 📙 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [API Documentation](#api-documentation)
- [Folder Structure](#folder-structure)

---

## 🏷️ Features

- Create Movies, Actors, Genres, and Directors with pydantic validation
- MongoDB document database integration
- Dockerized setup
- Swagger and Redoc documentation

---


## 🧰 Tech Stack

- **Backend:** FastAPI, Motor (MongoDB async driver), Pydantic v2
- **Database:** MongoDB
- **DevOps:** Docker, Docker Compose

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.10+
- MongoDB (local or Docker)
- Docker & Docker Compose (for containerized setup)


###  🎟️ Setup Locally

```bash
git clone https://github.com/opula1234/Movie_Explorer_Platform.git
cd Movie_Explorer_Platform
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt --no-cache-dir # to avoid cache issues
uvicorn app.main:app --reload
```

## 🐋 Run with Docker

docker-compose up --build

## 📋 API Documentation

- Swagger UI: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc


## 🗃️ Folder Structure
```txt
Movie_Explorer_Platform/
│
├── app/
│   ├── database/
│   ├── logger/
│   ├── routers/
│   ├── schemas/
│   ├── main.py
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
```
