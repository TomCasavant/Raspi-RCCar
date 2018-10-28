from gpiozero import OutputDevice
import pygame

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
    pygame.init()
    screen = pygame.display.set_mode((400,300))
    print ("You may now begin controlling your vehicle")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            turnOnPins(forward)
        elif pressed[pygame.K_DOWN]:
            turnOnPins(backward)
        else:
            turnOffPins(forward)
            turnOffPins(backward)
        if pressed[pygame.K_RIGHT]:
            turnOnPins(right)
        elif pressed[pygame.K_LEFT]:
            turnOnPins(left)
        else:
            turnOffPins(right)
            turnOffPins(left)
    
