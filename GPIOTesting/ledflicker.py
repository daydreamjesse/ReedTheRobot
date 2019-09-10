import RPi.GPIO as GPIO
from time import sleep, time
import random as rand

def flicker(sec):
	led = 8
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(led, GPIO.OUT, initial=0)
	pwm = GPIO.PWM(led, 100)
	pwm.start(0)
	max_time = sec
	start_time = time()
	while((time() - start_time) < max_time):
		try:
			pwm.ChangeDutyCycle(rand.randint(0, 100))
			sleep(0.05)
		except KeyboardInterrupt:
			pwm.stop()
			GPIO.cleanup()
			print("Exiting...")
	pwm.stop()
	GPIO.cleanup()
	print("Finished cleanup.")
