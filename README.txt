Mix Programming Language
Mech is a simple, interpreted programming language designed for basic system operations, text processing, and automation tasks. It features an easy-to-learn syntax and built-in commands for common operations.

Features
Simple Syntax: Easy-to-read commands with minimal punctuation

Text-to-Speech: Built-in say command for audio output

System Control: Basic system operations like reboot

File Importing: Modular code organization with use command

Binary Conversion: Convert text to binary representation

Conditional Logic: Basic if statements for flow control

Cross-Platform: Works on Windows and Linux systems

Installation
Ensure you have Python 3.6+ installed

Install the required dependency:

bash
pip install pyttsx3
Download mech.py to your desired location

Usage
Run Mech files using the Python interpreter:

bash
python mech.py filename.mech
Language Syntax
Basic Commands
Print to Console

text
print Hello, World!
Text-to-Speech

text
say Hello, I am a Mech
Delay Execution

text
sleep 2.5
zzz 1.0
Binary Conversion

text
binary Hello
System Commands
Reboot System (Linux only)

text
reboot
Conditional Execution

text
if true: print This will execute
File Management
Import Other Mech Files

text
use library.mech
use utilities/helpers.mech
Comments

text
# This is a comment
Example Programs
Basic Hello World
text
# hello.mech
print Hello, World!
say Greetings from Mech
Interactive Script
text
# demo.mech
print Starting demonstration...
say Mech language demo
sleep 1
print Converting text to binary:
binary Mech
sleep 2
print Demo complete!
File Extension
Mech files use the .mech extension.

Requirements
Python 3.6+

pyttsx3 library (for TTS functionality)

Limitations
reboot command only works on Linux systems

Basic error handling

Limited conditional logic support

License
Open source - modify and use as needed. Apache 2.0 license as of Mech 1 (Before rebrand as Mix 1).
