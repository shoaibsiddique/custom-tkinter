import tkinter as tk
from tkinter import ttk
import serial.tools.list_ports

def get_com_ports():
    com_ports = serial.tools.list_ports.comports()
    return list(com_ports)

def get_port_info(port):
    return f"Device: {port.device}\nDescription: {port.description}\n"

def get_vendor_info(port):
    vid = port.vid
    pid = port.pid
    manufacturer = port.manufacturer

    if vid is not None and pid is not None:
        return f"Vendor ID: {vid}\nProduct ID: {pid}\nManufacturer: {manufacturer}\n"
    else:
        return "Vendor information not available."

def display_com_ports():
    com_ports = get_com_ports()
    for port in com_ports:
        port_info = get_port_info(port)
        vendor_info = get_vendor_info(port)
        separator = "-" * 50
        print(f"{port_info}\n{vendor_info}\n{separator}")

    # Create a new window
    window = tk.Tk()
    window.title("COM Port Information")

    # Create a text widget to display the information
    text_widget = tk.Text(window, height=20, width=50)
    text_widget.pack()

    # Insert the COM port information into the text widget
    for port in com_ports:
        port_info = get_port_info(port)
        vendor_info = get_vendor_info(port)
        separator = "-" * 50
        text_widget.insert(tk.END, f"{port_info}\n{vendor_info}\n{separator}\n")

    # Start the main event loop
    window.mainloop()

# Call the function to display COM port information
display_com_ports()
