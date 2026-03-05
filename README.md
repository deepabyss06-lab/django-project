# Django Project

A simple Django project setup guide.

## 🚀 Getting Started

Follow the steps below to set up and run the project locally.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/deepabyss06-lab/django-project.git
cd django-project
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

* **Windows:**

  ```bash
  venv\Scripts\activate
  ```
* **macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```

### 3️⃣ Install Django

```bash
pip install django
```

> If a `requirements.txt` file is available, use:
>
> ```bash
> pip install -r requirements.txt
> ```

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run the Development Server

```bash
python manage.py runserver
```

Now open your browser and go to:

```
http://127.0.0.1:8000/
```

The project should now be running locally 🎉

---

## 📌 Requirements

* Python 3.x
* Django

---

## 📄 License

This project is for learning and development purposes.
