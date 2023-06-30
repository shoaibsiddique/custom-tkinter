import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import serial.tools.list_ports

# Create the tkinter application
root = ctk.CTk()
root.title("Arduino Control")
root.geometry("300x100")

# Create a variable to store the selected port
selected_port = tk.StringVar()

# Create a variable to store the connection status
connected = False

# Function to populate the dropdown menu with available COM ports
def populate_ports():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        port_name = port.device
        port_menu['menu'].add_command(label=port_name, command=tk._setit(selected_port, port_name))

# Function to establish a connection with the selected port
def connect():
    global connected

    selected_port_name = selected_port.get()
    if selected_port_name:
        if not connected:
            try:
                arduino = serial.Serial(selected_port_name, 9600, timeout=1)
                # Do something with the connected Arduino
                print(f"Connected to Arduino on port: {selected_port_name}")
                connected = True
                connect_button.config(text="Disconnect")
            except serial.SerialException:
                print(f"Failed to establish connection with Arduino on port: {selected_port_name}")
        else:
            # Disconnect the Arduino
            # Add your code to perform any necessary cleanup or disconnection steps
            print("Disconnected from Arduino")
            connected = False
            connect_button.config(text="Connect")
    else:
        print("No port selected.")

# Create a dropdown menu to select the Arduino port
port_menu = ttk.OptionMenu(root, selected_port, "Select Port")
populate_ports()

# Create a Connect button
connect_button = ttk.Button(root, text="Connect", command=connect)

# Pack the dropdown menu and Connect button
port_menu.pack()
connect_button.pack()

# Start the tkinter event loop
root.mainloop()
