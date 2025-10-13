import subprocess
import time
def run_allo_script(filename):
    if not filename.endswith(".mech"):
        print("Error: not a .mech file.")
        return

    try:
        with open(filename, "r") as file:
            for line in file:
                code = line.strip()
                if not code:
                    continue

                # Exit command
                if code == "exit":
                    break

                # --- ALLOCATION COMMAND (stubbed) ---
                elif code.startswith("sleep "):
                    text = code[6:]  # 'allo ' = 5 chars
                    time.sleep(text)
                elif code.startswith("zzz "):
                    text = code[4:]  # 'allo ' = 5 chars
                    time.sleep(text)

                # --- PRINT COMMAND ---
                elif code.startswith("print "):
                    text = code[6:]  # 'print ' = 6 chars
                    print(text)
                elif code.startswith("reboot"):
                    text = code[5:]
                    subprocess.run(["reboot", "now"])
                elif code.startswith("restart"):
                    text = code[7:]
                    print("'restart' is the Windows equivelant of the Mech 'reboot' command (Linux-only)")
                    time.sleep(2)
                elif code.startswith("define "):
                    text = code[7:]
                    code.startswith(text)
                    savedfunc = mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ)
                    text = savedfunc
                elif code.startswith("if "):
                    text = code[3:]
                    
                # --- USE COMMAND (import or read another file) ---
                elif code.startswith("use "):
                    lib = code[4:]  # 'use ' = 4 chars
                    try:
                        with open(lib, "r") as f:
                            content = f.read()
                            print(content)
                    except FileNotFoundError:
                        print(f"Library not found: {lib}")

                # --- BINARY COMMAND ---
                elif code.startswith("binary "):
                    text = code[7:]  # 'binary ' = 7 chars
                    binary_output = ' '.join(format(ord(char), '08b') for char in text)
                    print(binary_output)

                # --- COMMENT SYNTAX ---
                elif code.startswith("# "):
                    continue  # Mech comment, ignore line

                elif code.startswith("// "):
                    print("Info: The comment syntax you are using is non-Mech (C# style).")
                    continue

                # --- UNKNOWN COMMAND ---
                else:
                    print(f"Unknown command: {code}")

    except FileNotFoundError:
        print(f"File not found: {filename}")
