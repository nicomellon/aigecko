FROM python:3.10-alpine

COPY app /app

WORKDIR /app

RUN apk add zlib-dev jpeg-dev gcc musl-dev
RUN pip3 install -r requirements.txt

EXPOSE 80
CMD ["python3", "app.py"]