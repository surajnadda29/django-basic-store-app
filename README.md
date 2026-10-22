# Django Basic Store App 🚀

A robust and scalable Python web application built using the **Django framework**. This repository serves as a foundational e-commerce/store management template, demonstrating clean Model-View-Template (MVT) architecture, dynamic backend context passing, and structured database handling.

---

## 📋 Project Overview & Architecture
The project is structured to maintain a clean separation of concerns:
* **Project Root (`PythonProject141/myprj/`)**: Acts as the central container for configurations, global routing, andWSGI/ASGI settings.
* **App Module (`store/`)**: Encapsulates the specific business logic, models, views, and templates dedicated to store management.
* **Virtual Environment (`.venv/`)**: Ensures an isolated, dependency-controlled execution environment for Python packages.

---

## ✨ Key Features & Technical Highlights
* **MVT Architecture:** Implements Django's robust Model-View-Template pattern ensuring modularity and maintainability.
* **Database Management:** Uses SQLite3 out-of-the-box with Django ORM for seamless data migration, database schema management, and model querying (`models.py`).
* **Dynamic Routing:** Configured with root-level and app-level URL dispatchers (`urls.py`) to handle clean request endpoints.
* **Context Rendering:** Processes backend Python data dictionaries and securely passes context variables to frontend HTML templates (`views.py`).
* **Admin Panel Integration:** Leverages Django's built-in administrative dashboard for effortless database administration and record management.

---

## 🛠️ Tech Stack & Prerequisites
* **Language:** Python 3.x
* **Framework:** Django 
* **Database:** SQLite3
* **Environment Control:** venv (Python Virtual Environment)
* **Version Control:** Git & GitHub

---

## ⚙️ Getting Started & Local Setup

To run this project locally on your machine, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/surajnadda29/django-basic-store-app.git](https://github.com/surajnadda29/django-basic-store-app.git)
   cd django-basic-store-app/myprj
