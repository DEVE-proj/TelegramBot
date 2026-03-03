FROM python:3.14-alpine

WORKDIR /app
COPY . /app

RUN pip install --no-cache -r req.txt

ENTRYPOINT [ "python", "src/main.py" ]