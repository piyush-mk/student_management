# Student Management System

A backend API for managing student records, built using **FastAPI** and **MongoDB Atlas**, designed for handling CRUD operations efficiently.

## Features

- Create, read, update, and delete (CRUD) student records.
- MongoDB Atlas integration for secure, scalable database storage.
- Deployed on [Render](https://render.com) for public accessibility.
- API documentation generated with Swagger UI for easy testing and exploration.

## Base URL

The app is deployed at:  
[https://student-management-kpwr.onrender.com](https://student-management-kpwr.onrender.com)

---

## API Endpoints

### Base Path: `/students`

1. **Create a Student**  
   **POST** `/students`  
   Request body:
   ```json
   {
     "name": "John Doe",
     "age": 20,
     "address": {
       "city": "New York",
       "country": "USA"
     }
   }
   ```
   Response:
   ```json
   {
     "id": "1234567890abcdef"
   }
   ```

2. **List Students**  
   **GET** `/students`  
   Query parameters:
   ```text
   country (optional): Filter by country.
   age (optional): Filter students older than or equal to the given age.
   ```
   Response:
   ```json
   [
     {
       "id": "1234567890abcdef",
       "name": "John Doe",
       "age": 20,
       "address": {
         "city": "New York",
         "country": "USA"
       }
     }
   ]
   ```

3. **Get a Student by ID**  
   **GET** `/students/{id}`  
   Response:
   ```json
   {
     "id": "1234567890abcdef",
     "name": "John Doe",
     "age": 20,
     "address": {
       "city": "New York",
       "country": "USA"
     }
   }
   ```

4. **Update a Student by ID**  
   **PATCH** `/students/{id}`  
   Request body:
   ```json
   {
     "name": "Jane Doe"
   }
   ```
   Response:
   ```json
   {
     "message": "Update successful"
   }
   ```

5. **Delete a Student by ID**  
   **DELETE** `/students/{id}`  
   Response:
   ```json
   {
     "message": "Student deleted successfully"
   }
   ```

---

## Installation and Setup

### Prerequisites
- Python 3.9+
- MongoDB Atlas account with a free M0 cluster.

### Clone the Repository
```bash
git clone https://github.com/piyush-mk/student_management.git
cd student_management
```

### Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Configure Environment Variables
1. Create a `.env` file in the root directory.
2. Add the following variables:
   ```text
   MONGO_URI=mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/<database-name>?retryWrites=true&w=majority
   ```

### Run the Application Locally
```bash
uvicorn app.main:app --reload
```

Access the API documentation at:  
[https://student-management-kpwr.onrender.com/docs](https://student-management-kpwr.onrender.com/docs)

---

## Deployment

This app is deployed on Render and accessible publicly at:  
[https://student-management-kpwr.onrender.com](https://student-management-kpwr.onrender.com)

To deploy:
1. Push your code to a GitHub repository.
2. Link your repository to Render and set up the `MONGO_URI` environment variable in Render's settings.
3. Use the following build and start commands:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app.main:app --host=0.0.0.0 --port=8000`

---

## Tech Stack

- **Backend Framework:** FastAPI
- **Database:** MongoDB Atlas
- **Deployment:** Render
- **Language:** Python
- **Dependency Management:** `pip`

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature/bugfix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your forked repository and create a pull request.

---

