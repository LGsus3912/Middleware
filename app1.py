import Pyro4
from flask import Flask, render_template, request

app = Flask(__name__)
ns = Pyro4.locateNS(host='192.168.0.188')  # IP del servidor Pyro4 buscar la ip en ipconfig

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        print(f"Name: {name}")
        greeting_service = Pyro4.Proxy("PYRONAME:greeting_service")
        greeting = greeting_service.get_greeting(name)
        
        return render_template('greeting.html', name=name, greeting=greeting)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=5001)



