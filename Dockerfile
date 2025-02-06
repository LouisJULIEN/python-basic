FROM python:3.12.8-bookworm

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 5000/tcp
HEALTHCHECK CMD curl --fail http://localhost:5000 || exit 1
CMD ["python3", "server.py"]
