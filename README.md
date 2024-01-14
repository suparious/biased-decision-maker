# Biased Decision Maker

## Description

Biased Decision Maker is an application that helps users make decisions based on a list of options and user-defined biases.

## How to Use

- Enter your options in the provided fields.
- Adjust the slider to set the bias for each option.
- Click 'Decide' to make a biased random decision.
- Use the 'Save Configuration' button to save your options and biases.
- Use the 'Load Configuration' button to load your previously saved options and biases.

## System Requirements

- Compatible with Windows, Mac, and Linux.

## Running the Application

- Download the executable for your operating system.
- Run the executable file to start the application.

## Packaging the Application

If you wish to package this application yourself, follow these steps:

1. **Install PyInstaller:**
   - Ensure you have Python installed on your system.
   - Install PyInstaller using the command: `pip install pyinstaller`.

2. **Package the Application:**
   - Navigate to the directory containing the `biased_decision_maker.py` script in your terminal or command prompt.
   - Run the command: `pyinstaller --onefile --windowed biased_decision_maker.py`.
   - This will create a standalone executable in the `dist` folder.

   Note: The `--windowed` flag is used to prevent a terminal window from opening alongside the GUI application on Mac and Linux.

3. **Executable File:**
   - Find the packaged executable in the `dist` directory.
   - This file can be distributed and run on compatible systems without needing to install Python or any dependencies.
