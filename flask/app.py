from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Data universitas
data_universitas = [
    {"name": "Universitas Indonesia", "program": "Mandiri", "location": "Jakarta", "registration_open": True, "quota": 50},
    {"name": "Universitas Teknologi Bandung", "program": "Prestasi", "location": "Bandung", "registration_open": False, "quota": 30},
    {"name": "Universitas Brawijaya", "program": "Mandiri", "location": "Surabaya", "registration_open": True, "quota": 40},
    {"name": "Universitas Gajah Mada", "program": "Prestasi", "location": "Yogyakarta", "registration_open": True, "quota": 20},
    {"name": "Universitas Negeri Semarang", "program": "Mandiri", "location": "Semarang", "registration_open": False, "quota": 60},
    {"name": "Universitas Negeri Malang", "program": "Prestasi", "location": "Malang", "registration_open": True, "quota": 25},
    {"name": "Universitas Airlangga", "program": "Mandiri", "location": "Surabaya", "registration_open": True, "quota": 35},
    {"name": "Institut Pertanian Bogor", "program": "Prestasi", "location": "Bogor", "registration_open": True, "quota": 40},
    {"name": "Universitas Padjadjaran", "program": "Mandiri", "location": "Bandung", "registration_open": True, "quota": 50},
    {"name": "Universitas Sebelas Maret", "program": "Prestasi", "location": "Solo", "registration_open": True, "quota": 30},
    {"name": "Universitas Diponegoro", "program": "Mandiri", "location": "Semarang", "registration_open": True, "quota": 45},
    {"name": "Universitas Sriwijaya", "program": "Mandiri", "location": "Palembang", "registration_open": True, "quota": 50},
    {"name": "Universitas Negeri Jakarta", "program": "Mandiri", "location": "Jakarta", "registration_open": True, "quota": 30},
    {"name": "Institut Teknologi Sepuluh Nopember", "program": "Mandiri", "location": "Surabaya", "registration_open": True, "quota": 50},
    {"name": "Universitas Negeri Makassar", "program": "Prestasi", "location": "Makassar", "registration_open": True, "quota": 20},
    {"name": "Universitas Jenderal Soedirman", "program": "Mandiri", "location": "Purwokerto", "registration_open": True, "quota": 40},
    {"name": "Universitas Trisakti", "program": "Prestasi", "location": "Jakarta", "registration_open": False, "quota": 30}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    program = request.form.get('program')
    result = [
        uni for uni in data_universitas
        if uni['program'].lower() == program.lower() and uni['registration_open']
    ]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
