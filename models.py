from dataclasses import dataclass
from datetime import datetime
import app

# Defines a data class for tasks
@dataclass
class Task(app.db.Model):

    id:int
    title:str
    date:datetime
    completed: bool

    # Defines the 'id' column: integer, primary key
    id = app.db.Column(app.db.Integer(), primary_key=True)
    # Defines the 'title' column: string, maximum length of 140 characters
    title = app.db.Column(app.db.String(140))
    # Defines the 'date' column: datetime, default is the current time
    date = app.db.Column(app.db.DateTime(), default=datetime.utcnow)
    # Defines the 'completed' column: boolean, default is False
    completed = app.db.Column(app.db.Boolean(), default=False)

    # Initializes a new Task object
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Returns a string representation of the Task object
    def __repr__(self):
        return f'<Task id: {self.id} - {self.title}'
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'date': self.date.isoformat(),
            'completed': self.completed
        }