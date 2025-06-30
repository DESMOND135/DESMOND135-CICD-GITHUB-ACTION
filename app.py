from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    age = int(request.form['age'])
    sex = request.form['sex']
    bmi = float(request.form['bmi'])
    smoker = request.form['smoker']
    region = request.form['region']
    children = int(request.form['children'])

    # Dummy logic: You can replace this with a real ML model
    charges = 5000 + (age * 100) + (bmi * 200) + (children * 300)
    if smoker.lower() == 'yes':
        charges += 10000
    if sex.lower() == 'male':
        charges += 500

    result = {
        'age': age,
        'sex': sex,
        'bmi': bmi,
        'smoker': smoker,
        'region': region,
        'children': children,
        'charges': round(charges, 2)
    }

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
