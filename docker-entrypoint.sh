echo "Create database migtations"
python manage.py makemigrations

echo "Apply database migrations"
python manage.py migrate

echo "Starting server"
gunicorn --bind 0.0.0.0:8080 access_service.wsgi