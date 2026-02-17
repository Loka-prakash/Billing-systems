# Billing & Invoice Generation System (Django + MySQL)

##  Project Overview

This is a Django-based Billing and Invoice Generation System that allows users to:

- Generate bills
- Calculate total amount
- Calculate currency denominations
- Send invoice via email
- Maintain clean architecture using service layer (`service.py`)
- To view previous bill option 


The project follows separation of concerns by keeping business logic inside a dedicated `service.py` file.

---

#  Technology Stack

- Python 3.x
- Django
- MySQL
- HTML / CSS / Bootstrap
- Gmail SMTP (for Email)

---

#  Local Installation & Setup Guide

Follow the steps below to run this project on your local system.

---

## 1️⃣ Prerequirement

Make sure the following are installed:

- Python 3.10 or higher
- pip
- MySQL Server
- Git (optional)

Check Python version:

```bash
python --version
```

---

## 2️⃣ Clone or Download the Project

Using Git:

```bash
git clone <repository-url>
cd <project-folder>
```

Or download ZIP and extract it.

---

## 3️⃣ Create Virtual Environment (Recommended)

### Windows:

```bash
python -m venv venv .
venv\Scripts\activate
```

### macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4️⃣ Install Required Dependencies

If requirements.txt is available:

```bash
pip install -r requirements.txt
```

If not:

```bash
pip install django mysqlclient
```

If mysqlclient fails (Windows):

```bash
pip install PyMySQL
```

Then add inside project `__init__.py`:

```python
import pymysql
pymysql.install_as_MySQLdb()
```

---

#  MySQL Database Configuration

## 5️⃣ Create MySQL Database

Login to MySQL:

```bash
mysql -u root -p
```

Enter your password.

Create database:

```sql
CREATE DATABASE billing_project;
```

Exit:

```sql
exit;
```

---

## 6️⃣ Update settings.py Database Configuration

Replace DATABASES section with:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'billing_project',
        'USER': 'root',
        'PASSWORD': 'your-mysql-password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Replace `your-mysql-password` with your actual MySQL password.

---

## 7️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 8️⃣ Create Superuser (Optional – For Admin Panel)

```bash
python manage.py createsuperuser
```

Follow prompts and create admin credentials.

Admin panel URL:

```
http://127.0.0.1:8000/admin/
```

---

#  Email Configuration (Gmail SMTP Setup)

 For security reasons, email credentials are not included in this repository.

---

## Step 1: Enable 2-Step Verification

1. Go to: https://myaccount.google.com/security  
2. Enable **2-Step Verification**

---

## Step 2: Generate App Password

1. Visit: https://myaccount.google.com/apppasswords  
2. Select:
   - App → Mail  
   - Device → Windows Computer  
3. Click Generate  
4. Copy the 16-character password withoutspace

 Do NOT use your normal Gmail password.

---

## Step 3: Update settings.py

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

Replace with your Gmail and generated App Password.

---

## Alternative (Development Mode Only)

If email configuration is not required:

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

This prints email content in terminal instead of sending.

---

#  Run the Project

Start the development server:

```bash
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000/
```

---



#  Note

- Business logic is separated into `service.py`
- MySQL used as relational database
- Clean and maintainable project structure


#  Security Note

Sensitive credentials such as:
- Email passwords
- Database passwords

are intentionally excluded from this repository.

Please configure them locally before running the project.


 






