from flask import Flask, render_template

app = Flask(__name__)

# Home route - serves the colorful animated homepage
@app.route('/')
def home():
    return render_template('index.html')

# Admin panel route (optional: remove if not used now)
@app.route('/admin')
def admin_panel():
    # Example data — replace with real menu/orders if needed
    orders = []
    menu = [
        {"name": "Chapati", "price": 30},
        {"name": "Pulao", "price": 60},
        {"name": "Paneer Curry", "price": 90}
    ]
    return render_template('admin.html', orders=orders, menu=menu)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5002)


