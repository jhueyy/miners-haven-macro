# Auto Robot - Click & Keyboard Macro

A Python application that automates mouse clicks and keyboard actions with a user-friendly GUI interface.

## Features

- **GUI Interface**: Easy-to-use graphical interface with start/stop controls
- **Configurable Countdown**: Set a countdown timer before the macro starts
- **Real-time Status**: See what action is currently being performed
- **Safety Features**: Move mouse to screen corner to stop the macro (failsafe)
- **Looping**: Automatically repeats the entire macro sequence

## Installation

1. **Install Python** (3.7 or higher) if you haven't already
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**:
   ```bash
   python auto_robot.py
   ```

2. **Set the countdown time** (default is 5 seconds)

3. **Click "Start Macro"**

4. **Switch to your target application** during the countdown

5. **The macro will automatically execute** the following sequence:
   - Press 'M' key
   - Click at coordinates (1214, 366)
   - Click at coordinates (1000, 379)
   - Press 'L' key
   - Click at coordinates (1333, 280)
   - Wait 2 seconds
   - Press 'L' key again
   - Wait 25 seconds
   - Repeat the entire process

## Safety Features

- **Failsafe**: Move your mouse to any screen corner to stop the macro
- **Stop Button**: Click the "Stop Macro" button to halt execution
- **Threading**: The GUI remains responsive during macro execution

## Requirements

- Python 3.7+
- pyautogui
- tkinter (usually comes with Python)

## Notes

- Make sure your target application is in the correct position before starting
- The macro uses absolute screen coordinates, so ensure your screen resolution matches
- Test the macro on a safe application first to verify coordinates
- The application includes small delays between actions to ensure reliability

## Troubleshooting

- If the macro doesn't work as expected, check that your screen resolution matches the coordinates
- Ensure the target application is active and visible
- Try running with administrator privileges if needed
- Check that pyautogui is properly installed: `pip install pyautogui` 