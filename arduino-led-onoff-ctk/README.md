This code is baed on CTK, it selects the port and connects to that port.

It communicates with the arduino and turns ON and OFF the LED. Below are the packet definitions

- Packet Definition
LED_ON_SEND = b'\x1A\x10\x01\xCF'
LED_ON_RECEIVE = b'\x2A\x10\x01\xAF'
LED_OFF_SEND = b'\x1A\x10\x00\xCF'
LED_OFF_RECEIVE = b'\x2A\x10\x00\xAF'