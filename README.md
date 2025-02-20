# Djangautomate

**Djangautomate** is a Python package that automates Django app, model, serializer, and view generation from SQLAlchemy tables.

## 🚀 Features
- **Auto-generates Django models** from an SQLAlchemy database.
- **Creates Django REST Framework serializers & views**.
- **Updates `settings.py` and `urls.py` automatically**.
- **Easily integrates into existing Django projects**.

## 📦 Installation
```bash
pip install djangautomate
```

## 🛠️ Usage
```python
from sqlalchemy import create_engine
from djangautomate import Djangautomate

# Connect to the database
engine = create_engine("sqlite:///mydatabase.db")

# Initialize and generate Django code
generator = Djangautomate(engine, table_name="users", app_name="users_app")
generator.generate_code_files()
```


## 🔗 Links
