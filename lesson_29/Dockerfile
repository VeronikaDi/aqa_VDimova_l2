FROM python:3.9-slim

RUN apt-get update && apt-get install -y libpq-dev

WORKDIR /app

COPY ./app /app

RUN pip install -r /app/requirements.txt

CMD ["pytest", "test_my_first_docker.py"]
