from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, Task
from schemas import TaskCreate, TaskUpdate, TaskResponse, TaskListResponse, BulkTaskCreate, BulkTaskDelete

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Moved table creation to app initialization
with app.app_context():
    db.create_all()

@app.route('/v1/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if 'tasks' in data:
        tasks = []
        for task_data in data['tasks']:
            task = Task(title=task_data['title'], is_completed=task_data.get('is_completed', False))
            db.session.add(task)
            tasks.append(TaskResponse.from_orm(task))
        db.session.commit()
        return jsonify({"tasks": [{"id": task.id} for task in tasks]}), 201
    else:
        task_create = TaskCreate(**data)
        task = Task(title=task_create.title, is_completed=task_create.is_completed)
        db.session.add(task)
        db.session.commit()
        return jsonify({"id": task.id}), 201

@app.route('/v1/tasks', methods=['GET'])
def list_tasks():
    tasks = Task.query.all()
    return TaskListResponse(tasks=[TaskResponse.from_orm(task) for task in tasks]).json(), 200

@app.route('/v1/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get(id)
    if task:
        return TaskResponse.from_orm(task).json(), 200
    return jsonify({"error": "There is no task at that id"}), 404

@app.route('/v1/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return '', 204

@app.route('/v1/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get(id)
    if not task:
        return jsonify({"error": "There is no task at that id"}), 404
    
    data = request.get_json()
    task_update = TaskUpdate(**data)
    
    if task_update.title is not None:
        task.title = task_update.title
    if task_update.is_completed is not None:
        task.is_completed = task_update.is_completed
    
    db.session.commit()
    return '', 204

@app.route('/v1/tasks', methods=['DELETE'])
def bulk_delete_tasks():
    data = request.get_json()
    ids = [task['id'] for task in data['tasks']]
    tasks = Task.query.filter(Task.id.in_(ids)).all()
    for task in tasks:
        db.session.delete(task)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables at the start of the app
    app.run(debug=True)

@app.route('/favicon.ico')
def favicon():
    return '', 204  
