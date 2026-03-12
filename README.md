# Hex, Memory and Stack Calculator

This project implements a menu-driven Python program for CMP5361 – Computer Mathematics and Declarative Programming. The program demonstrates several key low-level computing concepts that occur inside computer systems, including:

- Decimal to hexadecimal conversion
- Fixed-width 16-bit binary representation
- Two’s complement signed interpretation
- Little-endian packing and unpacking
- ASCII memory storage with a null terminator
- Array address calculation using offsets
 - A simplified stack frame model with a register-style view.

 All required menu options (1–5) are implemented within a single integrated program.

# Program Structure

The system is structured using small, reusable functions that follow ideas from declarative programming. Core computational logic is separated from input and output handling so that each function performs a clear transformation from input to output.

This makes the program:

- easier to understand
- easier to test
- easier to maintain

 The menu interface controls user interaction by repeatedly displaying the available options and calling the relevant functions based on the user's selection. This structure ensures clarity, predictability, and ease of verification.

# Python Version

The project was developed using:

 Python 3.11+

Only the Python Standard Library is required to run the program.
No external packages are needed.

# Running the Program

From the project root directory, run:

```
python -m src.programA
```

This command launches the menu-driven interface and displays the available program options. 

The user can then select an option between 0 and 5 to perform the corresponding operation:

1) Convert (decimal to hexadecimal and 16-bit binary)
2) Little-endian pack/unpack (16-bit)
3) ASCII memory dump
4) Array addressing
5) Stack frame
0) Exit

 After completing an operation, the program returns to the main menu until the user selects 0 to exit.

# Running the Tests

Automated unit tests are included to verify the program behaves correctly. These tests cover boundary cases, binary formatting, signed interpretation, memory write/read behaviour, array addressing, ASCII dumping, and stack frame output.

To run the tests from the project root directory, use:

```
python -m unittest
```

For more detailed test output you can run:

```
python -m unittest -v
```

The tests check several important parts of the program including:

- correct 16-bit binary formatting
- two's complement signed interpretation
- little-endian packing and unpacking
- memory write and read behaviour
- ASCII memory dumping
- array address calculation
- stack frame output

These tests help ensure that each component of the program behaves as expected.

# Included Files

The final project submission contains:

- `programA.py` - main menu-driven program
- src/ - modules implementing each menu option
- tests/ - automated unit tests
- Task1_report.pdf - written report explaining the program
- Task1_DemoVideo.mp4 (or link) - demonstration of the program and tests
- README.md -  instructions for running the program and tests














