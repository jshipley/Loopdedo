"""Peewee database models for ORM."""

from peewee import (
    AutoField,
    CharField,
    DateField,
    ForeignKeyField,
    IntegerField,
    Model,
    SqliteDatabase,
    TimestampField,
)

db = SqliteDatabase("demo.db")


class Todo(Model):
    """Todo item model."""
    id = AutoField()
    description = CharField()
    frequency = IntegerField()
    due_date = DateField(null=True)
    last_completed = TimestampField(null=True, default=None)
    last_delayed = TimestampField(null=True, default=None)

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
