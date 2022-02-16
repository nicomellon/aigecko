FROM python:3.10-alpine

RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/app/backend

COPY app /usr/src/app/backend/app

WORKDIR /usr/src/app/backend/app

RUN pip install -r requirements.txt

EXPOSE 80
CMD ["python", "app.py"]