import serial.tools.list_ports
import serial

class SerialPort:
    def __init__(self):
        self.ser = None

    def connect(self, port):
        self.ser = serial.Serial(port, 9600, timeout=1)
        return self.ser.isOpen()

    def disconnect(self):
        if self.ser:
            self.ser.close()
            self.ser = None
        return not self.ser

def get_ports():
    ports = serial.tools.list_ports.comports()
    return [port.device for port in ports]
