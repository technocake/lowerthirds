python manage.py migrate
python manage.py collectstatic --noinput

gunicorn lowerthirds.wsgi:application --bind 0.0.0.0:8000 --workers 3 --reload
