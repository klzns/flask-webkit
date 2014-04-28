# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify

# Import the database object from the main app module
from app import db

# Import module models (i.e. Task)
from resources.task.model import Task

# Define the blueprint: 'task', set its url prefix: app.url/task
mod_task = Blueprint('task', __name__, url_prefix='/task')

@mod_task.route('/', methods=['GET'])
def task_get_all():
    tasks = Task.query.all()
    form = request.form

    if request.get_json():
        return jsonify({'tasks': tasks})
    else:
        return render_template('task/list.html', todo=tasks, form=form)

@mod_task.route('/', methods=['POST'])
def task_post():
    if request.get_json():
        data = request.get_json()
        description = data.description
    else:
        data = request.form        
        description = data['description']
    
    task = Task(description=str(description))
    db.session.add(task)
    db.session.commit()

    if request.get_json():        
        return jsonify({'task': task.toJSON()}), 200
    else:        
        return redirect(url_for('.task_get_all'))

@mod_task.route('/<int:id>', methods=['GET'])
def task_get(id):
    task = Task.query.filter_by(id=id).first()    

    return jsonify({'task': task.toJSON()}), 200

@mod_task.route('/<int:id>', methods=['PUT'])
def task_update(id):
    task = Task.query.filter_by(id=id).first()
    data = request.get_json()

    if 'complete' in data:
        task.complete = data['complete']
    if 'description' in data:
        task.description = data['description']

    db.session.add(task)
    db.session.commit()

    return jsonify({'task': task.toJSON()}), 200

@mod_task.route('/<int:id>', methods=['DELETE'])
def task_delete(id):
    task = Task.query.filter_by(id=id).first()
    
    db.session.delete(task)
    db.session.commit()

    return jsonify({'result': True}), 200