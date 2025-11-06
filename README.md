# 💰 Expense Tracking System  

A full-stack web application for managing and analyzing personal expenses — built with **Python**, **FastAPI**, **Streamlit**, **MySQL**, and **Postman** for API testing.

---

## 🚀 Features  

- **Expense Management:** Add, update, and delete daily expenses  
- **Category Tracking:** Organize expenses into categories (Rent, Food, Shopping, Entertainment, Other)  
- **Analytics Dashboard:** Visualize spending patterns with charts and percentage breakdowns  
- **RESTful API:** Fully documented API for expense operations  
- **Responsive UI:** Clean Streamlit interface with tab-based navigation  
- **API Testing:** Comprehensive Postman collection for backend testing  

---

## 🏗️ Architecture  

### 🔹 Backend (FastAPI)
- `server.py` – REST API server with endpoints for expense operations  
- `db_helper.py` – Database connection and CRUD operations  
- `logging_setup.py` – Centralized logging configuration  

### 🔹 Frontend (Streamlit)
- `app.py` – Main Streamlit application with tab navigation  
- `add_update_ui.py` – UI for adding/updating expenses  
- `analytics_ui.py` – Analytics and visualization dashboard  

### 🔹 API Testing (Postman)
- Complete API test collection  
- Environment configuration  
- Request examples and test scripts  

### 🔹 Database (MySQL)
- MySQL database with an `expenses` table  
- Supports date-based queries and category grouping  

---

## Project Structure

```
expense-tracker/
├── backend/
│   ├── server.py
│   ├── db_helper.py
│   └── logging_setup.py
├── frontend/
│   ├── app.py
│   ├── add_update_ui.py
│   └── analytics_ui.py
├── tests/
│   └── test_db_helper.py
├── requirements.txt
└── README.md
```

### File Descriptions
- **backend/server.py**: FastAPI server with all API endpoints
- **backend/db_helper.py**: Database connection and CRUD operations  
- **backend/logging_setup.py**: Logger configuration and setup
- **frontend/app.py**: Main Streamlit application with tab navigation
- **frontend/add_update_ui.py**: UI for adding and updating expenses
- **frontend/analytics_ui.py**: Analytics dashboard with charts
- **tests/test_db_helper.py**: Unit tests for database functions
- **requirements.txt**: Python package dependencies
- **README.md**: Project documentation (this file)


## ⚙️ Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/ahm-raihan/Expense-tracking-for-daily-life.git
cd Expense-tracking-for-daily-life
``` 
### 2️⃣ Create and Activate a Virtual Environment
```bash
python -m venv .venv
venv\Scripts\activate

```
### 3️⃣ Install Dependencies
```bash
    pip install -r requirements.txt
```
### 4️⃣ Configure MySQL
```bash
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',  # Change to your MySQL password
    database='expense_manager'
)

```
#### Start the Backend Server
```bash
   cd backend
uvicorn server:app --reload --port 8000 

```
#### Start the Frontend
```bash
    cd frontend
streamlit run app.py
```

### 5️⃣ Run the FastAPI Server
```bash
    uvicorn server:app --reload

```


### 6️⃣ Run the Streamlit Frontend
```bash
  streamlit run app.py
```


| Component     | Technology              |
| ------------- | ----------------------- |
| Backend       | FastAPI                 |
| Frontend      | Streamlit               |
| Database      | MySQL                   |
| API Testing   | Postman                 |
| Data Handling | Pandas                  |
| Logging       | Python `logging` module |
