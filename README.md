# Biased Decision Maker

![Build Status](https://github.com/suparious/biased-decision-maker/actions/workflows/pylint.yml/badge.svg)

## Description

Biased Decision Maker is an application that helps users make decisions based on a list of options and user-defined biases.

## Features

- Add and remove options dynamically.
- Set biases for each option using sliders.
- Make a decision based on the set biases.
- Save and load configuration settings.

## How to Use

- Enter your options in the provided fields.
- Add options using the 'Add Option' button.
- Remove the last option using the 'Remove Last Option' button.
- Adjust the slider to set the bias for each option.
- Click 'Decide' to make a biased random decision.
- Use the 'Save Configuration' button to save your options and biases.
- Use the 'Load Configuration' button to load your previously saved options and biases.

## System Requirements

- Compatible with Windows, Mac, and Linux.

## Running the Application

- Download the executable for your operating system, from the [releases page](https://github.com/suparious/biased-decision-maker/releases).
- Run the executable file to start the application.

## Building and Packaging the Application

### Using spec files

#### Windows

```bash
pyinstaller specs/windows.spec
```

#### MacOS

```bash
pyinstaller specs/macos.spec
plutil -insert Copyright -string "Copyright © SolidRusT Networks 2024" dist/biased-decision-maker.app/Contents/Info.plist
/usr/libexec/PlistBuddy -c "Set :CFBundleShortVersionString 0.8.0" "dist/biased-decision-maker.app/Contents/Info.plist"
/usr/libexec/PlistBuddy -c "Set :CFBundleVersion 0.8.0.69" "dist/biased-decision-maker.app/Contents/Info.plist"
```

#### Linux

```bash
pyinstaller specs/linux.spec
```

### Using PyInstaller

If you wish to package this application yourself, follow these steps:

1. **Install PyInstaller and PyQt5:**

   - Ensure you have Python installed on your system.
   - Install PyInstaller using the command: `pip install pyinstaller PyQt5`.

2. **Package the Application:**

   - Navigate to the directory containing the `biased-decision-maker.py` script in your terminal or command prompt.
   - Run the command: `pyinstaller --onefile --windowed biased-decision-maker.py`.
   - Windows might flag this app as a trojan. To remedy this, you can try using the --onedir flag instead of --onefile.
   - This will create a standalone executable (or package folder) in the `dist` folder.

   Note: The `--windowed` flag is used to prevent a terminal window from opening alongside the GUI application on Mac and Linux.

3. **Executable File:**
   - Find the packaged executable in the `dist` directory.
   - This file can be distributed and run on compatible systems without needing to install Python or any dependencies.

### Windows build issues

Windows Defender flags the executable as a trojan. This is a false positive. You can try using the --onedir flag instead of --onefile to remedy this. If this does not work, you can try adding the executable to the Windows Defender exclusion list. The best way to resolve this, however, is to build pyinstaller on a Windows machine.

#### Building PyInstaller on Windows

1. Delete and re-create a fresh python `venv` environment.
2. Do not install any packages in this environment, repeat step 1 if you did.
3. Delete **pycache**, **build**, **dist** folders and the **.spec** file from your project folder.
4. Install a compiler, like the [C++ Compiler from Visual Studios](http://visualstudio.microsoft.com/vs/features/cplusplus/), Community Edition.
5. Download and extract the latest release of Pyinstaller from [Pyinstaller's GitHub Repository](http://github.com/pyinstaller/pyinstaller/releases).
6. Using a terminal, navigate to where you have extracted the pyinstaller source code and `cd` to the **\*bootloader** folder.
7. Compile the bootloader with `python.exe ./waf all --target-arch=64bit`. If you want 32bit, use `python.exe ./waf all --target-arch=32bit`.
8. Using an administrator terminal, install the compiled pyinstaller with `python.exe setup.py install`. You may need `wheel` installed for this to work.
9. Navigate to your project folder and run `pyinstaller --onefile --windowed biased-decision-maker.py`.
10. Re-upload to VirusTotal and see if the false positive is gone.

## References

- [https://plainenglish.io/blog/pyinstaller-exe-false-positive-trojan-virus-resolved-b33842bd3184](https://plainenglish.io/blog/pyinstaller-exe-false-positive-trojan-virus-resolved-b33842bd3184)
