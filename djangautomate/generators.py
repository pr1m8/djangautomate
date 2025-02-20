import sqlalchemy

class ModelGenerator:
    """Generates Django model code from an SQLAlchemy table."""

    def __init__(self, db_engine, table_name, index_cols):
        self.db_engine = db_engine
        self.table_name = table_name
        self.index_cols = index_cols

    def generate(self):
        model_code = "from django.db import models\n\n"
        model_code += f"class {self.table_name.capitalize()}(models.Model):\n"
        metadata = sqlalchemy.MetaData()
        table = sqlalchemy.Table(self.table_name, metadata, autoload_with=self.db_engine)
        
        for col in table.c:
            if col.name == 'index':
                continue
            model_code += f"    {col.name} = models.{self.get_field_type(col.type)}\n"

        model_code += f"    class Meta:\n"
        model_code += f"        db_table = '{self.table_name}'\n"
        return model_code

    def get_field_type(self, col_type):
        if isinstance(col_type, sqlalchemy.String):
            return "CharField(max_length=255)"
        elif isinstance(col_type, sqlalchemy.Integer):
            return "IntegerField()"
        elif isinstance(col_type, sqlalchemy.Float):
            return "FloatField()"
        elif isinstance(col_type, sqlalchemy.Boolean):
            return "BooleanField()"
        elif isinstance(col_type, sqlalchemy.DateTime):
            return "DateTimeField()"
        return "TextField()"


class ViewGenerator:
    """Generates Django ViewSet code for the model."""

    def __init__(self, app_name):
        self.app_name = app_name
        self.camelcased_app_name = app_name.capitalize()

    def generate(self):
        return f"""
from .models import {self.camelcased_app_name}
from .serializers import {self.camelcased_app_name}Serializer
from rest_framework import viewsets

class {self.camelcased_app_name}ViewSet(viewsets.ModelViewSet):
    queryset = {self.camelcased_app_name}.objects.all()
    serializer_class = {self.camelcased_app_name}Serializer
"""


class SerializerGenerator:
    """Generates Django REST Framework serializer code."""

    def __init__(self, db_engine, table_name):
        self.db_engine = db_engine
        self.table_name = table_name

    def generate(self):
        return f"""
from rest_framework import serializers
from .models import {self.table_name.capitalize()}

class {self.table_name.capitalize()}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {self.table_name.capitalize()}
        fields = '__all__'
"""


class AppConfigGenerator:
    """Generates Django app configuration."""

    def __init__(self, app_name):
        self.app_name = app_name.capitalize()

    def generate(self):
        return f"""
from django.apps import AppConfig

class {self.app_name}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'endpoints.{self.app_name.lower()}'
"""
