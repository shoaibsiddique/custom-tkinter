import serial.tools.list_ports
import serial
import tkinter.messagebox as messagebox

# Packet definitions
LED_ON_SEND = b'\x1A\x10\x01\xCF'
LED_ON_RECEIVE = b'\x2A\x10\x01\xAF'
LED_OFF_SEND = b'\x1A\x10\x00\xCF'
LED_OFF_RECEIVE = b'\x2A\x10\x00\xAF'

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

    def send_packet(self, packet):
        if self.ser:
            self.ser.write(packet)

    def receive_packet(self):
        if self.ser:
            packet = self.ser.read(4)
            hex_str = ' '.join([f'{i:02X}' for i in packet])
            print(f"Received packet: {hex_str}")
            return packet

class LEDControl:
    def __init__(self, serial_port, led_button, led_indicator):
        self.serial_port = serial_port
        self.led_button = led_button
        self.led_indicator = led_indicator
        self.led_indicator_rect = led_indicator.create_oval(2, 2, 22, 22, fill="red")

    def toggle_led(self):
        if self.led_button.cget('text') == "On":
            self.serial_port.send_packet(LED_ON_SEND)
            if self.serial_port.receive_packet() == LED_ON_RECEIVE:
                self.led_button.configure(text="Off")
                self.led_indicator.itemconfig(self.led_indicator_rect, fill="green")
                messagebox.showinfo("LED Status", "LED is now ON")
        else:
            self.serial_port.send_packet(LED_OFF_SEND)
            if self.serial_port.receive_packet() == LED_OFF_RECEIVE:
                self.led_button.configure(text="On")
                self.led_indicator.itemconfig(self.led_indicator_rect, fill="red")
                messagebox.showinfo("LED Status", "LED is now OFF")

class ConnectionControl:
    def __init__(self, serial_port, connect_button, connection_checkbox, connection_indicator):
        self.serial_port = serial_port
        self.connect_button = connect_button
        self.connection_checkbox = connection_checkbox
        self.connection_indicator = connection_indicator
        self.indicator_rect = connection_indicator.create_oval(2, 2, 22, 22, fill="red")

    def connect(self, port):
        if self.connect_button.cget('text') == "Connect":
            if self.serial_port.connect(port):
                self.connect_button.configure(text="Disconnect")
                self.connection_checkbox.configure(text="1")
                self.connection_indicator.itemconfig(self.indicator_rect, fill="green")

    def disconnect(self):
        if self.connect_button.cget('text') == "Disconnect":
            if self.serial_port.disconnect():
                self.connect_button.configure(text="Connect")
                self.connection_checkbox.configure(text="0")
                self.connection_indicator.itemconfig(self.indicator_rect, fill="red")


def get_ports():
    ports = serial.tools.list_ports.comports()
    return [port.device for port in ports]
