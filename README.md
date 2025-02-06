# Basic Python

A basic Python web server:
- Flask server
- Payload check with pydantic
- Docker image

# Start

```bash
pip3 install -r requirements.txt
python3 server.py
```

# Test

Make sure that your working directory is this repository's root

```bash
pytest
```

# Docker

```bash
docker build -t python-basic/build . 

docker run -p 5000:5000 python-basic/build:latest
```
