import serial
import time

def main():
    dev = serial.Serial(
        port="/dev/ttyUSB0",
        baudrate=115200,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        rtscts=True,
        timeout=0.5)

    # rated voltage
    garb = dev.read(100)
    if garb:
        print("Got garbage", garb)
    while True:
        #dev.write(b"\x55")
        for i in range(200):
            #dev.write(b"\x01\x04\x30\x00\x00\x01\x3E\xCA")
            dev.write(b"\x01\x03\x90\x13\x00\x03\xD9\x0E")
        resp = dev.read(7)
        print("Got", resp)
        time.sleep(1)


if __name__ == '__main__':
    main()
