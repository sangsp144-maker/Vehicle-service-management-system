from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data ko yahan store karenge (Database ki jagah list use kar rahe hain simple ke liye)
vehicle_list = []

@app.route('/')
def index():
    return render_template('index.html', vehicles=vehicle_list)

@app.route('/add', methods=['POST'])
def add_vehicle():
    vehicle_no = request.form['vehicle_no']
    owner_name = request.form['owner_name']
    service = request.form['service']
    status = request.form['status']

    vehicle_list.append({
        'vehicle_no': vehicle_no,
        'owner_name': owner_name,
        'service': service,
        'status': status
    })
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_vehicle(id):
    if 0 <= id < len(vehicle_list):
        vehicle_list.pop(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)