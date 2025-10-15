import subprocess
import time
import pyttsx3
import sys
import os

def run_mech_code(code_string, filename=None):
    """
    Execute Mech code from a string
    """
    lines = code_string.split('\n')
    for line_num, line in enumerate(lines, 1):
        code = line.strip()
        if not code or code.startswith("#"):
            continue

        # Exit command
        if code == "exit":
            break

        # --- SLEEP COMMANDS ---
        elif code.startswith("sleep "):
            try:
                seconds = float(code[6:])
                time.sleep(seconds)
            except ValueError:
                print(f"Error: Invalid sleep duration at line {line_num}")
                
        elif code.startswith("zzz "):
            try:
                seconds = float(code[4:])
                time.sleep(seconds)
            except ValueError:
                print(f"Error: Invalid zzz duration at line {line_num}")

        # --- PRINT COMMAND ---
        elif code.startswith("print "):
            text = code[6:]
            print(text)
            
        elif code.startswith("say "):
            text = code[4:]  # Fixed: 'say ' is 4 characters, not 6
            try:
                engine = pyttsx3.init()
                engine.say(text)
                engine.runAndWait()
            except Exception as e:
                print(f"Error with text-to-speech: {e}")

        # --- SYSTEM COMMANDS ---
        elif code == "reboot":
            try:
                if os.name == 'posix':  # Linux/Unix
                    subprocess.run(["sudo", "reboot"])
                else:
                    print("Reboot command only available on Linux systems")
            except Exception as e:
                print(f"Error with reboot: {e}")
                
        elif code == "restart":
            print("'restart' is the Windows equivalent of the Mech 'reboot' command (Linux-only)")
            time.sleep(2)

        # --- CONDITIONAL COMMANDS ---
        elif code.startswith("if "):
            parts = code[3:].split(":", 1)
            if len(parts) == 2:
                condition = parts[0].strip()
                commands = parts[1].strip()
                
                if condition == "true":
                    run_mech_code(commands, filename)
            else:
                print(f"Error: Invalid if statement at line {line_num}")

        # --- USE COMMAND (import or read another file) ---
        elif code.startswith("use "):
            lib = code[4:]
            # Add .mech extension if not present
            if not lib.endswith(".mech"):
                lib += ".mech"
                
            # Handle relative paths if we have a filename context
            if filename and not os.path.isabs(lib):
                lib_path = os.path.join(os.path.dirname(filename), lib)
            else:
                lib_path = lib
                
            try:
                with open(lib_path, "r") as f:
                    lib_content = f.read()
                    run_mech_code(lib_content, lib_path)
            except FileNotFoundError:
                print(f"Library not found: {lib_path}")
            except Exception as e:
                print(f"Error reading library {lib_path}: {e}")

        # --- BINARY COMMAND ---
        elif code.startswith("binary "):
            text = code[7:]
            binary_output = ' '.join(format(ord(char), '08b') for char in text)
            print(binary_output)

        # --- COMMENT SYNTAX ---
        elif code.startswith("//"):
            print("Info: The comment syntax you are using is non-Mech (C# style).")
            continue

        # --- UNKNOWN COMMAND ---
        else:
            print(f"Unknown command at line {line_num}: {code}")

def run_mech_file(filename):
    """
    Run a .mech file
    """
    if not filename.endswith(".mech"):
        print("Error: not a .mech file.")
        return False

    try:
        with open(filename, "r") as file:
            content = file.read()
            run_mech_code(content, filename)
        return True
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return False
    except Exception as e:
        print(f"Error running mech file: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("MECH")
        print("MECHanical robots language")
        print("------------------------------------------")
        print("Usage: python mech.py <file.mech>")
        print("Example: python mech.py example.mech")
    else:
        filename = sys.argv[1]
        run_mech_file(filename)
