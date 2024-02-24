"""Peewee database models for ORM."""

from peewee import (
    SqliteDatabase,
    Model,
    CharField,
    AutoField,
    DateField,
    IntegerField,
    ForeignKeyField,
)

db = SqliteDatabase("demo.db")


class Todo(Model):
    """Todo item model."""
    id = AutoField()
    description = CharField()
    frequency = IntegerField()
    last_completed = DateField(null=True)
    last_delayed = DateField(null=True)

    class Meta:
        """Table metadata."""
        database = db


class Tag(Model):
    """User created tags."""
    id = AutoField()
    name = CharField(unique=True)

    class Meta:
        """Table metadata."""
        database = db


class TagTodoMap(Model):
    """Mapping table to connect Todo items with tags."""
    id = AutoField()
    todo_id = ForeignKeyField(Todo)
    tag_id = ForeignKeyField(Tag)

    class Meta:
        """Table metadata."""
        database = db
