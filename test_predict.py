from routes import predict
from app import app


## first positive test case for '/hello' route
# def test_hello_route_success():
#     tester = app.test_client()
#     response = tester.get('/hello')

#     assert response.status_code==200


# def test_hello_route_failure():
#     tester = app.test_client()
#     response = tester.get('/hello')

#     assert response.status_code==500



## positive test case for '/predict' route

def test_predict_route_success():
    tester = app.test_client()

    data = {
        "gestation": "279",
        "parity": "0",
        "age": "27",
        "height": "70",
        "weight": "100",
        "smoke": "0"
    }
    response = tester.post("/predict", data=data)  # form data, no json

    assert response.status_code == 200


def test_predict_route_invalid_data():
    tester = app.test_client()

    # Send empty data to trigger 400
    response = tester.post("/predict", data={})

    assert response.status_code == 400


def test_predict_route_wrong_url():
    tester = app.test_client()

    data = {
        "gestation": "279",
        "parity": "0",
        "age": "27",
        "height": "70",
        "weight": "100",
        "smoke": "0"
    }
    response = tester.post("/oredict", data=data)  # wrong url, form data

    assert response.status_code == 404


def test_predict_route_wrong_method():
    tester = app.test_client()

    data = {
        "gestation": "279",
        "parity": "0",
        "age": "27",
        "height": "70",
        "weight": "100",
        "smoke": "0"
    }
    response = tester.get("/predict", data=data)  # GET not allowed

    assert response.status_code == 405