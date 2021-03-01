from flask_lambda import FlaskLambda
import json

app = FlaskLambda(__name__)


@app.route('/')
def index():
    message = {
        'message': 'Drowsiness Prediction REST API'
    }
    return (
        json.dumps(message),
        200,
        {'Content-Type': 'application/json'}
    )


@app.route('/student')
def prediction_result():
    message = {
        'message': 'Student Drowsiness Result'
    }
    return (
        json.dumps(message),
        200,
        {'Content-Type': 'application/json'}
    )


"""
if __name__ == '__main__':
    app.run(debug=True)
"""