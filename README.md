# SCT_CS_04
# Keyboard Event Logger

## Project Overview

This project demonstrates keyboard event handling by recording only the keys typed inside the application's own window. It is designed for educational purposes and does not capture system-wide keyboard input.

## Features

- Records keyboard events within the application
- Stores key presses in a text file
- Includes timestamps
- Simple graphical interface using Tkinter

## Technologies Used

- Python 3
- Tkinter

## How to Run

1. Save the program as `keyboard_event_logger.py`.
2. Run the program:
   ```
   python keyboard_event_logger.py
   ```
3. Click inside the text box and start typing.
4. The logged keys are saved in `key_log.txt`.

## Output

The program creates a file named:

```
key_log.txt
```

Each key press is recorded along with the date and time.

## Learning Outcome

- Keyboard event handling
- File handling in Python
- GUI development with Tkinter
- Ethical logging within an application's own interface
