from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
import osascript

def set_volume(target_volume):
    vol = "set volume output volume " + str(target_volume)
    osascript.osascript(vol)

def print_handler(address, *args):
    print(f"{address}: {args}")
    target_volume = args
    set_volume(50)


def default_handler(address, *args):
    print(f"DEFAULT {address}: {args}")


dispatcher = Dispatcher()
dispatcher.map("/feedback/*", print_handler)
dispatcher.set_default_handler(default_handler)

ip = "0.0.0.0"
port = 4546

server = BlockingOSCUDPServer((ip, port), dispatcher)
print("serving")
server.serve_forever()  # Blocks forever