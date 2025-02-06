import json
import traceback

from flask import Flask
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

from misc.environment import is_local
from misc.logger import logger

app = Flask(__name__)
cors = CORS(app, supports_credentials=True)

from modules.health.route import *
from modules.check_payload.route import *

app.config['BUNDLE_ERRORS'] = True
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

enable_debug = is_local()


@app.errorhandler(HTTPException)
def handle_http_exception(http_error):
    """Return JSON instead of HTML for HTTP errors."""
    error_as_str = ''.join(traceback.format_exception(http_error))
    if is_local():
        print(error_as_str)

    response = http_error.get_response()

    if hasattr(http_error, 'data') and 'message' in http_error.data:
        errors = http_error.data['message']
    else:
        errors = [{'message': http_error.description}]

    response.data = json.dumps({
        "code": http_error.code,
        "name": http_error.name,
        "errors": errors,
    })
    response.content_type = "application/json"
    return response


@app.errorhandler(Exception)
def handle_python_exception(error):
    """Return JSON for Python exceptions."""
    error_as_str = ''.join(traceback.format_exception(error))
    if is_local():
        print(error_as_str)
    logger.error(error_as_str)

    response_content = json.dumps({
        "code": 500,
        "name": "InternalServerError",
        "errors": [{'message': str(error)}],
    })
    response = app.response_class(
        response=response_content,
        status=500,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(debug=enable_debug, host='0.0.0.0')
