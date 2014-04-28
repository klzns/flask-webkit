# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

# Define a Task model
class Task(Base):

    __tablename__ = 'task'

    # Task description
    description    = db.Column(db.String(192),  nullable=False)
    # Task complete
    complete       = db.Column(db.Boolean,  nullable=False)

    # New instance instantiation procedure
    def __init__(self, description):

        self.description = description
        self.complete = False

    def __repr__(self):
        return '<Task Id: %r, Description: %r, Complete: %r>' % (self.id, self.description, self.complete)

    def toJSON(self):
        return {
            'id': self.id,
            'description': self.description,
            'complete': self.complete
        }