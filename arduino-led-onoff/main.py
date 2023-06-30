import tkinter as tk
from tkinter import ttk
import serial.tools.list_ports

# Create the tkinter application
root = tk.Tk()
root.title("Arduino Control")
root.geometry("300x300")

# Create a variable to store the selected port
selected_port = tk.StringVar()

# Create a variable to store the connection status
connected = False
arduino = None

# Create a variable to store the LED state
led_state = False

# Function to populate the dropdown menu with available COM ports
def populate_ports():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        port_name = port.device
        port_menu['menu'].add_command(label=port_name, command=tk._setit(selected_port, port_name))

# Function to establish a connection with the selected port
def connect():
    global connected
    global arduino

    selected_port_name = selected_port.get()
    if selected_port_name:
        if not connected:
            try:
                # Connect to Arduino
                arduino = serial.Serial(selected_port_name, 9600, timeout=1)
                # Do something with the connected Arduino
                print(f"Connected to Arduino on port: {selected_port_name}")
                connected = True
                connect_button.config(text="Disconnect")
                indicator_canvas.itemconfig(indicator_oval, fill="green")
            except serial.SerialException:
                print(f"Failed to establish connection with Arduino on port: {selected_port_name}")
        else:
            # Disconnect from Arduino
            # Replace the code below with your actual disconnection logic
            arduino.close()
            print("Disconnected from Arduino")
            connected = False
            connect_button.config(text="Connect")
            indicator_canvas.itemconfig(indicator_oval, fill="red")
    else:
        print("No port selected.")

# Function to send control packet to Arduino
def send_control_packet(state):
    packet = bytearray([0x1A, 0x10, state, 0xCF])
    arduino.write(packet)
    print(f"Control packet sent: {packet}")

# Function to handle feedback from Arduino
def handle_feedback():
    feedback = arduino.read_all()
    if feedback:
        print(f"Received feedback: {feedback}")
        if feedback == bytearray([0x2A, 0x10, led_state, 0xAF]):
            if led_state:
                led_state_label.config(text="ON")
            else:
                led_state_label.config(text="OFF")

# Function to handle feedback from Arduino
def handle_feedback():
    feedback = arduino.read_all()
    if feedback:
        print(f"Received feedback: {feedback}")
        if feedback == bytearray([0x2A, 0x10, led_state, 0xAF]):
            if led_state:
                led_state_label.config(text="ON")
                led_indicator_canvas.itemconfig(led_indicator_oval, fill="green")
            else:
                led_state_label.config(text="OFF")
                led_indicator_canvas.itemconfig(led_indicator_oval, fill="red")


# Function to toggle the LED state
def toggle_led_state():
    global led_state

    if connected:
        led_state = not led_state
        send_control_packet(int(led_state))
        handle_feedback()

# Create a dropdown menu to select the Arduino port
port_menu = ttk.OptionMenu(root, selected_port, "Select Port")
populate_ports()

# Create a Connect/Disconnect button
connect_button = ttk.Button(root, text="Connect", command=connect)

# Create a canvas for the circular indicator
indicator_canvas = tk.Canvas(root, width=30, height=30)
indicator_oval = indicator_canvas.create_oval(5, 5, 25, 25, fill="red")

# Create a canvas for the second LED indicator
led_indicator_canvas = tk.Canvas(root, width=30, height=30)
led_indicator_oval = led_indicator_canvas.create_oval(5, 5, 25, 25, fill="red")


# Create a LED state label
led_state_label = ttk.Label(root, text="OFF")

# Create a Toggle LED button
toggle_led_button = ttk.Button(root, text="Toggle LED", command=toggle_led_state)

# Pack the dropdown menu, Connect/Disconnect button, indicator canvas, LED state label, and Toggle LED button
port_menu.pack()
connect_button.pack(pady=5)
indicator_canvas.pack(pady=10)
led_indicator_canvas.pack(pady=10)
led_state_label.pack()
toggle_led_button.pack()

# Function to check for feedback periodically
def check_feedback():
    if connected:
        handle_feedback()
    root.after(100, check_feedback)

# Start checking for feedback
check_feedback()

# Start the tkinter event loop
root.mainloop()
