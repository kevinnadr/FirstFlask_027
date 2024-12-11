from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Data universitas
universitas = [
    {"name": "Universitas A", "program": "Mandiri", "location": "Jakarta", "registration_open": True, "quota": 50},
    {"name": "Universitas B", "program": "Prestasi", "location": "Bandung", "registration_open": False, "quota": 30},
    {"name": "Universitas C", "program": "Mandiri", "location": "Surabaya", "registration_open": True, "quota": 40},
    {"name": "Universitas D", "program": "Prestasi", "location": "Yogyakarta", "registration_open": True, "quota": 20},
    {"name": "Universitas E", "program": "Mandiri", "location": "Medan", "registration_open": False, "quota": 60},
    {"name": "Universitas F", "program": "Prestasi", "location": "Malang", "registration_open": True, "quota": 25}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    program = request.form.get('program')
    result = [
        uni for uni in universitas
        if uni['program'].lower() == program.lower() and uni['registration_open']
    ]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
