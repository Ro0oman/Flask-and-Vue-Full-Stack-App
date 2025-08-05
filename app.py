from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from flask import redirect
from flask import url_for
from dotenv import load_dotenv
from config import Config
from flask_sqlalchemy import SQLAlchemy

# Carga las variables de entorno desde el archivo .flaskenv
load_dotenv('./.flaskenv')
# Crea la aplicación Flask
app = Flask(__name__)
# Carga la configuración desde la clase Config
app.config.from_object(Config)

db = SQLAlchemy(app)
import models  



from forms import TaskForm

# Define la ruta principal ("/")
@app.route("/")
def index():
    tasks = models.Task.query.all()

    # Si la petición es una petición AJAX
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(tasks)
    
    # Si no es una petición AJAX, renderiza la plantilla index.html
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create_task():
    user_input = request.get_json()

    form = TaskForm(data = user_input)

    if form.validate():
        task = models.Task(title = form.title.data)

        db.session.add(task)
        db.session.commit()
        # Returns task in JSON format
        return jsonify(task.to_dict())
    
    return redirect(url_for('index'))
# Define route to delete a task
# Define la ruta para borrar una tarea
@app.route('/delete', methods=['POST'])
def delete_task():
    task_id = request.get_json().get('id')
    task = models.Task.query.filter_by(id=task_id).first()

    db.session.delete(task)
    db.session.commit()
    return jsonify({'result': 'Ok'})

# Define route to complete a task
@app.route('/complete', methods=['POST'])
def complete_task():
    task_id = request.get_json().get('id')
    task = models.Task.query.filter_by(id=task_id).first()

    task.completed = True

    db.session.add(task)
    db.session.commit()
    return jsonify({'result': 'Record updated'})

# # Inicia la aplicación si se ejecuta el script directamente
# if __name__ == '__main__':
#     app.run()