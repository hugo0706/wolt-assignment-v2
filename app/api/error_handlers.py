import werkzeug

class WrongJSON(werkzeug.exceptions.HTTPException):
    code = 400
    description = 'Invalid JSON format.'

    