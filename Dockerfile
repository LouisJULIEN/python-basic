FROM python:3.12.8-bookworm

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 8000/tcp
HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1
CMD ["fastapi", "run", "server.py"]
