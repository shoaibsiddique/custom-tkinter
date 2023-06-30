This code works with the arduino. It sends a packet to the arduino to turn ON and OFF the LED.

Packet is 4 byte, the arduino turns on the led or off's it based on the commanded packet.

Then it sends a 4 byte feedback packet based on which the GUI shows if the LED has been turned ON or not.