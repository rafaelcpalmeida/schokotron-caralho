import RPi.GPIO as GPIO
from time import sleep

class Candy:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    def __init__(self):
        print("Starting the Mighty Schokotron, caralho")
        GPIO.setup(3, GPIO.OUT)
        self.pwm = GPIO.PWM(3, 50)
        self.pwm.start(0)

    def set_duty_cycle(self, duty):
        GPIO.output(3, True)
        self.pwm.ChangeDutyCycle(duty)
        sleep(0.15)
        GPIO.output(3, False)
        self.pwm.ChangeDutyCycle(0)

