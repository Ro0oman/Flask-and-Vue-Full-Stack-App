from app import app, db
from models import Task  # importa tus modelos

with app.app_context():
    # db.create_all()

    # # Solo aquí puedes usar db.session correctamente
    # t2 =  Task(title='New Task 2')
    # db.session.add(t2)
    # db.session.commit()

    tasks = Task.query.all()
    print(tasks)
