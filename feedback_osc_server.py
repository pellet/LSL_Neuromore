from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer


def print_handler(address, *args):
    print(f"{address}: {args}")


def default_handler(address, *args):
    print(f"DEFAULT {address}: {args}")


dispatcher = Dispatcher()
dispatcher.map("/feedback/*", print_handler)
dispatcher.set_default_handler(default_handler)

ip = "0.0.0.0"
port = 32767

server = BlockingOSCUDPServer((ip, port), dispatcher)
print("serving")
server.serve_forever()  # Blocks forever