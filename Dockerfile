# Dockerfile
FROM python:3.11
WORKDIR /app
COPY requirement.txt requirement.txt
RUN pip install -r requirement.txt

COPY ./app /app
# CMD [ "python", "app/run.py" ]
ENV PYTHONDONTWRITEBYTECODE=1
ENV FLASK_APP=app/run.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

CMD ["flask", "run"]

