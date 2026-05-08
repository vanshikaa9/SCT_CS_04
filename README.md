# Keyboard Event Logger

A Python-based keyboard event logging tool built for educational and cybersecurity learning purposes.

This project captures keyboard input events and stores them locally in a text file for analysis. 

## Important Note

This project is intended strictly for educational and authorized testing environments.

The program should only be used with user awareness and consent. It is not designed for stealth usage, credential theft, persistence, or unauthorized monitoring.

## Features

* Captures keyboard input events
* Logs keystrokes to a local text file
* Handles common keys like:

  * Space
  * Enter
  * Control keys
* Stops safely using the ESC key
* Simple command-line implementation

## Technologies Used

* Python
* pynput

## Installation

Install the required dependency:

```bash
pip install pynput
```

## Run

```bash
python keylogger.py
```

The captured keystrokes will be stored in:

```text
log.txt
```

Press `ESC` to stop the logger.


## Learning Outcomes

* Understanding keyboard event listeners
* Working with file handling in Python
* Capturing and processing system input events
* Implementing basic logging mechanisms
* Understanding ethical considerations in cybersecurity projects

## Disclaimer

This project is created solely for educational purposes and should only be used in controlled environments with proper authorization.
