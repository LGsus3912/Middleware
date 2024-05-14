import Pyro4
from flask import Flask, render_template, request

app = Flask(__name__)
ns = Pyro4.locateNS()

@Pyro4.expose
class GreetingService:
    def get_greeting(self, name):
        print(f"get_greeting({name})")  # Imprimir el nombre recibido
        return f"Hola, {name}!"

def main():
    daemon = Pyro4.Daemon()
    uri = daemon.register(GreetingService)
    ns.register("greeting_service", uri)
    print("Ready.")
    daemon.requestLoop()

if __name__ == "__main__":
    main()

