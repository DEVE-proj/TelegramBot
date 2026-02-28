FROM python:latest

WORKDIR /app
COPY . /app

RUN pip install -r req.txt

ENTRYPOINT [ "python", "src/main.py" ]