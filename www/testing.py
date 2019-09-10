from pynput import keyboard
from time import sleep

def onPress(key):
	if key == keyboard.Key.f11:
		print("Pressed F11. Waiting 5 seconds...")
		sleep(5)
		print("Done waiting.")
	if key == keyboard.Key.f12:
		print("Pressed F12, killing program.")
		return False


with keyboard.Listener(onPress=onPress) as listener:
	if __name__ == '__main__':
		for i in range(10):
			sleep(1)
			if not listener.running:
				break
