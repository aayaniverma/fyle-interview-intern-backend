from datetime import datetime
from core import db

class Assignment(db.Model):
    __tablename__ = 'assignments'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Assignment(title={self.title}, due_date={self.due_date})>"

    def is_due(self):
        """Check if the assignment is due."""
        return datetime.now() > self.due_date

    def update_description(self, new_description):
        """Update the description of the assignment."""
        self.description = new_description

    def to_dict(self):
        """Convert the assignment to a dictionary."""
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date.isoformat()  # Assuming due_date is a datetime object
        }
