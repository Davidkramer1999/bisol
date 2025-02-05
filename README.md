# FastAPI-PostgreSQL-Docker

A FastAPI application integrated with PostgreSQL, structured to be deployed using Docker and Docker Compose.

---

## 🚀 How to Run the Project

### **1. Prerequisites**
Ensure you have **Docker** and **Docker Compose** installed.

### **2. Clone the Repository**
```sh
git clone https://github.com/Davidkramer1999/bisol.git
cd bisol
```

### **3. Setup Environment Variables**
Create a `.env` file inside the `backend/` directory and fill in your database credentials:

```sh
POSTGRES_USER=username
POSTGRES_PASSWORD=password
POSTGRES_DB=consumerData
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

### **4. Start the Project**
Navigate to the backend directory and run:
```sh
cd backend
docker-compose up --build
```

This will:
- Start **PostgreSQL**
- Start **FastAPI backend**
- Initialize the database schema

### **5. Verify Running Containers**
Check if the containers are running:
```sh
docker ps
```
You should see:
```
CONTAINER ID   IMAGE                                   COMMAND                  STATUS         PORTS                NAMES
xxxxxx         fastapi-postgresql-docker-backend       "uvicorn app.main:ap…"   Up X hours     0.0.0.0:80->80/tcp   fastapi-postgresql-docker-backend-1
xxxxxx         postgres:12.0-alpine                    "docker-entrypoint.s…"   Up X days      5432/tcp             fastapi-postgresql-docker-db-1
```

---

## 📂 Project Structure

```
FastAPI-PostgreSQL-Docker/
│── backend/                  # Backend (FastAPI Application)
│   │── app/                   # Main FastAPI app
│   │   │── __init__.py
│   │   │── main.py            # Entry point for FastAPI
│   │   │── database.py        # DB Connection (SQLAlchemy)
│   │   │── models.py          # SQLAlchemy Models
│   │   │── schema.py          # Pydantic Schemas
│   │   │── crud.py            # Database logic
│   │   │── dependencies.py    # DB Dependency Injection
│   │   │── routers/           # API Routers
│   │   │   │── __init__.py
│   │   │   │── energy.py      # Energy API Endpoints
│   │── tests/                 # Unit & API tests
│   │   │── test_energy.py
│   │── Dockerfile             # Backend Dockerfile
│   │── requirements.txt       # Python dependencies
│   │── initdb.sql             # Database Initialization
│   │── transformed_energy_data.csv # Processed CSV
│── client/                   # API Client (for Testing)
│   │── client.py
│── data/                     # Data & Processing Scripts
│   │── original.csv           # Raw CSV Data
│   │── modify.py              # Script to transform data
│── docker-compose.yml         # Docker Compose File
│── README.md                  # Documentation
```

