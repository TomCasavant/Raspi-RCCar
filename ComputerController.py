from gpiozero import OutputDevice
import curses

#Initialize pin numbers
turnLeftPins = [4, 5]
turnRightPins = [24, 25]
moveForwardPins = [17, 27]
moveBackwardPins = [22, 23]

def turnOnPins(pins):
    for pin in pins:
        pin.on()

def turnOffPins(pins):
    for pin in pins:
        pin.off()
    
def setupPins(num):
    return [OutputDevice(num[0]), OutputDevice(num[1])]


if __name__ == "__main__":
    #Setup Pins
    print("Setting up pins...\n")
    left = setupPins(turnLeftPins)
    right = setupPins(turnRightPins)
    forward = setupPins(moveForwardPins)
    backward = setupPins(moveBackwardPins)

    #Setup Key Inputs
    print ("Setting up controller\n")
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)
    print ("You may now begin controlling your vehicle")
    try:
        #Handle user input
        while True:
            c = screen.getch() #Gets current key presses
	    screen.addstr("Test: " + str(c))
            c2 = 0
            #Control Left/Right movements
            if (c == curses.KEY_RIGHT or c2 == curses.KEY_RIGHT):
                turnOnPins(right)

#		screen.addstr("right")
            elif (c == curses.KEY_LEFT or c2 == curses.KEY_LEFT):
                turnOnPins(left)

            else:
                #Turn off unused pins
                turnOffPins(left)
                turnOffPins(right)
            #Control Forward/Backward movements
            if (c == curses.KEY_DOWN or c2 == curses.KEY_DOWN):
		screen.erase()
		
		screen.addstr("down")
                turnOnPins(backward)

            elif (c == curses.KEY_UP or c2 == curses.KEY_UP):
                turnOnPins(forward)

            else:
                #Turn off unused pins
                turnOffPins(forward)
                turnOffPins(backward)
    finally:
        #Shutdown curses
        print("Exiting program")
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()
    
