import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from myfunctions import SerialPort, get_ports

class App:
    def __init__(self, root):
        self.root = root
        self.serial_port = SerialPort()
        self.connection_frame = tk.Frame(self.root)
        self.connection_frame.pack()

        self.connection_combo = ttk.Combobox(self.connection_frame, values=get_ports())
        self.connection_combo.pack(padx=5, pady=5)

        self.connect_button = ctk.CTkButton(self.connection_frame, text="Connect", command=self.toggle_connection)
        self.connect_button.pack(padx=5, pady=5)

        self.connection_checkbox = ctk.CTkCheckBox(self.connection_frame)
        self.connection_checkbox.pack(padx=5, pady=5)

        self.connection_indicator = tk.Canvas(self.connection_frame, width=24, height=24)
        self.connection_indicator.pack(padx=5, pady=5)
        self.indicator_rect = self.connection_indicator.create_oval(2, 2, 22, 22, fill="red")  # padding of 2 units

    def toggle_connection(self):
        if self.connect_button.cget('text') == "Connect":
            if self.serial_port.connect(self.connection_combo.get()):
                self.connect_button.configure(text="Disconnect")
                self.connection_checkbox.configure(text="1")
                self.connection_indicator.itemconfig(self.indicator_rect, fill="green")
        else:
            if self.serial_port.disconnect():
                self.connect_button.configure(text="Connect")
                self.connection_checkbox.configure(text="0")
                self.connection_indicator.itemconfig(self.indicator_rect, fill="red")

root = tk.Tk()
app = App(root)
root.mainloop()
