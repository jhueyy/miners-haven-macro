# Miner's Haven Rebirth Macro

A Python application that automates mouse clicks and keyboard actions for Miner's Haven Rebirth with a user-friendly GUI interface.

## Features

- **GUI Interface**: Easy-to-use graphical interface with start/stop/reset controls
- **Configurable Countdown**: Set a countdown timer before the macro starts
- **Real-time Status**: See what action is currently being performed
- **Looping**: Automatically repeats the entire macro sequence
- **Reset Functionality**: Reset the macro to start fresh from the beginning

## Installation

1. **Install Python** (3.7 or higher) if you haven't already
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Setup Requirements

**Important**: This macro is configured for:
- **14-inch Mac** screen resolution
- **Roblox window minimized** as much as possible
- **Roblox window positioned** in the top right of the screen

If your setup differs, you may need to adjust the coordinates in the code.

## In-Game Setup

**Before running the macro, ensure:**
- You have **enough money** in-game to rebirth
- You are **ready to rebirth** (all conditions met)
- Your game setup takes approximately **24 seconds** to complete

**Timing Notes:**
- The macro waits 24 seconds between cycles
- You can adjust this timing in the code if your setup takes longer or shorter
- The timing assumes your rebirth process completes within 24 seconds

## Usage

1. **Run the application**:
   ```bash
   python auto_robot.py
   ```

2. **Set the countdown time** (default is 5 seconds)

3. **Click "Start Macro"**

4. **Switch to Roblox** during the countdown

5. **The macro will automatically execute** the following sequence:
   - Press 'm' key
   - Click at coordinates (1214, 366)
   - Click at coordinates (1000, 379)
   - Press 'l' key
   - Click at coordinates (1333, 280)
   - Wait 2 seconds
   - Press 'l' key again
   - Wait 24 seconds
   - Repeat the entire process

## Requirements

- Python 3.7+
- pyautogui
- tkinter (usually comes with Python) 