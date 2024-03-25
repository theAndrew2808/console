import time

import console
from colorama import Fore

class Console:
    """
    Console class for logging messages with colors.
    """

    def __init__(self):
        """
        Initialize the Console object.
        """
        self.version = "1.0"  # Default version
        self.message_order = []
        self.alive = False
        self.index = 0

    def init_standard(self, version):
        """
        Initialize the Console object for standard versions (0.8 and higher).
        """
        self.version = version
        self.alive = True
        self.print_message(f"Starting Console (Version {version})...", color=Fore.GREEN)
        time.sleep(1.5)
        self.print_message(f"---------------------------------", color=Fore.GREEN)
        self.print_message(f"[Console]: Version {version} is running", color=Fore.GREEN)
        if version <= "0.7":
            self.print_message(f"[Console]: Warning, you're using an old version ({version}). Colors in console aren't supported.", color=Fore.WHITE)

    def init_legacy(self, version):
        """
        Initialize the Console object for legacy versions (below 0.8).
        """
        self.version = version
        self.alive = True
        self.print_message(f"Starting Console (Version {version})...")
        time.sleep(1.5)
        self.print_message(f"[Console]: Warning, you're using an old version ({version}). Colors in console aren't supported. If you're using version above 0.5 method kill() is not implemented", color=Fore.WHITE)

    def init(self, version="1.0"):
        """
        Initialize the Console object based on the provided version.
        """
        if version >= "0.8":
            self.init_standard(version)
        else:
            self.init_legacy(version)

    def print_message(self, message, color=Fore.WHITE):
        """
        Print a message with the given color.
        """
        if self.alive:
            if self.version >= "0.8":
                self.message_order.append(color + message)
            else:
                self.message_order.append(message)
        else:
            raise RuntimeError("Console is not started. Use console.init()")

    def error(self, message):
        """
        Log an error message.
        """
        self.print_message("[Console Error]: " + message, Fore.RED)

    def warning(self, message):
        """
        Log a warning message.
        """
        self.print_message("[Console Warning]: " + message, Fore.YELLOW)

    def info(self, message):
        """
        Log an informational message.
        """
        self.print_message("[Console Info]: " + message, Fore.GREEN)

    def kill(self):
        """
        Stop the console.
        """
        if self.alive:
            self.alive = False
        else:
            raise RuntimeError("Console is already turned off")

    def log(self, hidden=False):
        """
        Print the logged messages.
        """
        for _ in self.message_order:
            if self.index < len(self.message_order):
                print(self.message_order[self.index])
                self.index += 1
            else:
                self.index = 0
                self.message_order.clear()

        if not hidden:
            if self.alive:
                print(Fore.GREEN + f"[-= Console log complete ↑↑↑ =-]")
            else:
                raise RuntimeError("Console is not started. Use console.init()")

    def export(self):
        """
        Export the logged messages as a string.
        """
        return '\n'.join(self.message_order)


# init console
console = Console()