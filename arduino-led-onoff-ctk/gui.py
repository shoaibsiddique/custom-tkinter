import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from myfunctions import SerialPort, get_ports, LEDControl, ConnectionControl

class App:
    def __init__(self, root):
        self.root = root
        self.serial_port = SerialPort()
        self.connection_frame = ctk.CTkFrame(self.root)
        self.connection_frame.pack()

        self.connection_combo = ctk.CTkComboBox(self.connection_frame, values=get_ports())
        self.connection_combo.pack(padx=5, pady=5)

        self.connect_button = ctk.CTkButton(self.connection_frame, text="Connect")
        self.connect_button.pack(padx=5, pady=5)

        self.connection_checkbox = ctk.CTkCheckBox(self.connection_frame)
        self.connection_checkbox.pack(padx=5, pady=5)

        self.connection_indicator = ctk.CTkCanvas(self.connection_frame, width=24, height=24)
        self.connection_indicator.pack(padx=5, pady=5)

        self.connection_control = ConnectionControl(self.serial_port, self.connect_button, self.connection_checkbox, self.connection_indicator)

        self.led_button = ctk.CTkButton(self.connection_frame, text="On")
        self.led_button.pack(padx=5, pady=5)

        self.led_indicator = ctk.CTkCanvas(self.connection_frame, width=24, height=24)
        self.led_indicator.pack(padx=5, pady=5)

        self.led_control = LEDControl(self.serial_port, self.led_button, self.led_indicator)
        self.led_button.configure(command=self.led_control.toggle_led)
        
        self.connect_button.configure(command=self.toggle_connection)
        
    def toggle_connection(self):
        port = self.connection_combo.get()
        if self.connect_button.cget('text') == "Connect":
            self.connection_control.connect(port)
        else:
            self.connection_control.disconnect()

root = tk.Tk()
app = App(root)
root.mainloop()

