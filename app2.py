import Pyro4
from flask import Flask, render_template, request

#Antes de correr el servidor Flask, se debe correr el servidor Pyro4 con el siguiente comando: pyro4-ns -n 192.168.129.72 buscar la ip en ipconfig

app = Flask(__name__)
ns = Pyro4.locateNS(host='192.168.0.188')  # IP del servidor Pyro4 buscar la ip en ipconfig

@Pyro4.expose
class GreetingService:
    def get_greeting(self, name):
        print(f"get_greeting({name})")  # Imprimir el nombre recibido
        return f"Hola, {name}!"

def main():
    daemon = Pyro4.Daemon(host='192.168.0.188') # IP del servidor Pyro4 buscar la ip en ipconfig
    uri = daemon.register(GreetingService)
    ns.register("greeting_service", uri)
    print("Ready.")
    daemon.requestLoop()

if __name__ == "__main__":
    main()

