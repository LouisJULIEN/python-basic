from flask import request

from misc.payload_validation import validate_payload_or_400, ForbidExtraKey
from server import app


class HealthCheckPayload(ForbidExtraKey):
    works: bool


@app.route("/check", methods=['POST'])
def payload_check():
    data_json = request.json
    validate_payload_or_400(data_json, HealthCheckPayload)

    return {"message": 'ok'}
