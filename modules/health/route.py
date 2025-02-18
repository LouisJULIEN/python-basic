from server import app


@app.get("/health")
def health_check():
    return {"message": 'ok'}
