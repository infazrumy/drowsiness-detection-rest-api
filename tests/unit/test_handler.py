from flask_lambda import FlaskLambda
from handlers.app import prediction_result


def test_base_route():

    app = FlaskLambda(__name__)
    prediction_result()
    client = app.test_client()
    response = client.get('/student')
    assert 200
    print(response)
