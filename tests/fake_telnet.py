import re
import socket
import threading
from time import sleep

class Daemon(threading.Thread):
    """A fake telnet server emulating a blackbody emitter controller."""

    def __init__(self, (socket, addr)):
        threading.Thread.__init__(self)
        self.socket = socket
        self.addr = addr
        self.device_values = {
            'old_setpoint': '25.0',
            'setpoint': '25.0',
            'temp': '25.0'
        }
        self.language = {
            'DA(\d+[.]*\d*)\r\n': (lambda settings: self.begin_updating(settings)),
            'M1\r\n': (lambda settings: self.device_values['setpoint']),
            'M2\r\n': (lambda settings: self.device_values['temp'])
        }
        self._timeout = 0.2

    def update(self):
        temp = float(self.device_values.get('temp'))
        setpoint = float(self.device_values.get('setpoint'))
        while temp < setpoint - 0.1 or temp > setpoint + 0.1:
            temp = float(self.device_values.get('temp'))
            old_setpoint = float(self.device_values.get('old_setpoint', '0.0'))
            setpoint = float(self.device_values.get('setpoint', old_setpoint))
            temp += (setpoint - old_setpoint) / temp
            self.device_values.update({'temp': str(temp)})
            sleep(self._timeout)
        return

    def begin_updating(self, settings):
        self.device_values.update({'setpoint': settings.group(1)})
        threading.Thread(target=self.update).start() 

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
            response = self.handle(data)
            self.socket.send(response)
        self.socket.close()

def start():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 9999))
    sock.listen(1)
    lock = threading.Lock()
    daemon = Daemon(sock.accept())
    daemon.start()

if __name__ == '__main__':
    start()
