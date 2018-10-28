from gpiozero import OutputDevice
from time import sleep


if __name__ == "__main__":
	PIN = 4
	PIN2 = 5
	PIN3 = 6
	PIN4 = 13
	pin = OutputDevice(PIN)
	pin2 = OutputDevice(PIN2)
	pin3 = OutputDevice(PIN3)
	pin4 = OutputDevice(PIN4)

	pin.on()
	pin2.on()
	pin3.on()
	pin4.on()
	sleep(5)
	pin.off()
	pin2.off()
	pin3.off()
	pin4.off()
