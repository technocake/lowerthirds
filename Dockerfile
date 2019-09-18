FROM python:3.7
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python manage.py migrate \
        && echo yes | python manage.py collectstatic
CMD ["sh", "start.sh"]
