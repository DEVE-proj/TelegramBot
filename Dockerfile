FROM python:latest

WORKDIR /app
COPY . .

RUN pip install -r req.txt

ENTRYPOINT [ "python src/main.py" ]