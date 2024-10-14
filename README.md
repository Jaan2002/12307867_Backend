# Waterdip AI Backend Assignment - New

> Notes: The submission needs to be written in python 3.7+ using any framework i,e Flask, Django, FastAPI
> 

## Summary

You will be building a server that can keep track of tasks. Your server must be able to do the following:

1. Create a new task with a title property and a boolean determining whether the task has been completed. A new unique id would be created for each new task
2. List all tasks created
3. Get a specific task
4. Delete a specified task
5. Edit the title or completion of a specific task
6. (Extra Credit) Bulk add multiple tasks in one request
7. (Extra Credit) Bulk delete multiple tasks in one request

Your application will accept JSON and/or URL parameters and will return JSON data. Your server would be ready to be automatically integrated in a web system.

## Database Configuration and Model Design

1. **Database Setup**
- **SQL Option**: Use [`SQLAlchemy`](https://pypi.org/project/SQLAlchemy/) to define your models and manage database connections. Choose a lightweight database like SQLite for simplicity or a more robust option like PostgreSQL for production readiness.
- **NoSQL Option**: Use a library like [`Motor](https://pypi.org/project/motor/) or [PyMongo](https://pypi.org/project/pymongo/)` for MongoDB to manage document-based data without a strict schema.
1. **Models**
    - **Task Model**: Define a Task model that includes properties for the task ID, title, and completion status. The model structure will vary based on the chosen database.
2. (Extra Credit) **Pydantic Schemas**: Create [`Pydantic`](https://pypi.org/project/pydantic/) schemas for validating input data and structuring output data. Define schemas for creating a task, updating a task, listing tasks, deleting task/s etc.
