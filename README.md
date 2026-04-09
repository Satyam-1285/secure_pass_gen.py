# secure_pass_gen.py# Secure Password Generator 🔒

A lightweight, command-line password generator written in Python. It uses cryptographically secure random generation to create strong passwords on the fly. 

## Features
* Generate secure passwords of any length (default is 16 characters).
* Customize output by explicitly excluding uppercase letters, numbers, or symbols.
* No external dependencies required—built entirely with standard Python libraries.

## How to Run

Open your terminal, navigate to the folder containing the script, and run:

```bash
# Generate a standard 16-character password
python secure_pass_gen.py

# Generate a 24-character password
python secure_pass_gen.py -l 24

# Generate a password with only lowercase letters and numbers
python secure_pass_gen.py --no-symbols --no-upper
