from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/generate', methods=['POST'])
def generate():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    skills = request.form['skills']
    education = request.form['education']

    return render_template('cv.html',
                           name=name,
                           email=email,
                           phone=phone,
                           skills=skills,
                           education=education)

@app.route('/premium')
def premium():
    return render_template('premium.html')

if __name__ == '__main__':
    app.run(debug=True)
