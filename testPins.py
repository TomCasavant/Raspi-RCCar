from gpiozero import DigitalOutputDevice
from time import sleep


if __name__ == "__main__":
	PIN = 11
	pin = DigitalOutputDevice(PIN)

	pin.on()
	sleep(2)
	pin.off()
