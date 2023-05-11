from pyfirmata import Arduino

comport='COM3'

board = Arduino(comport)

led_1 = board.get_pin('d:2:o')

def led(total):
    if total == 0:
        led_1.write(0)
    if total == 1:
        led_1.write(1)