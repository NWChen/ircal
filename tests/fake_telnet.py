import socket
import threading

class daemon(threading.Thread):
    """A fake telnet server emulating a blackbody emitter controller."""

    def __init__(self, (socket, addr)):
        threading.Thread.__init__(self)
        self.socket = socket
        self.addr = addr
        self.device_values = {
            'temp': '25.0'
        }
        self.language = {
            'DA(\d+[.]*\d*)\r\n': (lambda settings: self.device_values.update({'setpoint': settings.group(1)})),
            'M2\r\n': (lambda settings: self.device_values['temp'])
        }

    def handle(self, data):
        for command, response in self.language.items():
            settings = re.match(command, data)
            if settings:
                res = response(settings)
                if res:
                    return res + '\r\n'
        return ''

    def run(self):
        self.socket.send("SUCCESSFULLY CONNECTED.\n")
        while(True):
            data = self.socket.recv(1024)
            response = handle(data)
            self.socket.send(response)
        self.socket.close()

def start():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 9999))
    sock.listen(1)
    lock = threading.Lock()
    daemon(sock.accept()).start()
