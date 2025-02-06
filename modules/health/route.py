from server import app


@app.route("/health")
def health_check():
    return {"message": 'ok'}
