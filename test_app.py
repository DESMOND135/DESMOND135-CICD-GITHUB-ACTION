from app import app

def test_home_page():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b'Cost of Insurance' in response.data

def test_prediction_post():
    tester = app.test_client()
    response = tester.post('/predict', data=dict(
        age=30,
        sex="male",
        bmi=25.5,
        smoker="no",
        region="northeast",
        children=2
    ), follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Predicted Charges' in response.data
