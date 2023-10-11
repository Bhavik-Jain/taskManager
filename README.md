# Instructions to run the project
1. Take the clone of this Repository
2. Create a virtual environment outside the project using the below command
```python -m venv env```
3. Activate the virtual environment
4. Change the directory to tasklist
5. Install the dependencies from the requirements.txt file
```pip install -r requirements.txt ```
6. Run migrations
```
    python manage.py makemigrations
    python manage.py migrate
```
7. Start Server using
```python manage.py runserver ```
8. Import Postman collection and run the APIs
