const { exec } = require('child_process');
const fs = require('fs');
const path = require('path');

function runMechCode(codeString, filename = null) {
    /**
     * Execute Mech code from a string
     */
    const lines = codeString.split('\n');
    for (let lineNum = 0; lineNum < lines.length; lineNum++) {
        const line = lines[lineNum].trim();
        if (!line || line.startsWith("#")) {
            continue;
        }

        // Exit command
        if (line === "exit") {
            break;
        }

        // --- SLEEP COMMANDS ---
        else if (line.startsWith("sleep ")) {
            try {
                const seconds = parseFloat(line.slice(6));
                setTimeout(() => {}, seconds * 1000);
            } catch (error) {
                console.error(`Error: Invalid sleep duration at line ${lineNum + 1}`);
            }
        } else if (line.startsWith("zzz ")) {
            try {
                const seconds = parseFloat(line.slice(4));
                setTimeout(() => {}, seconds * 1000);
            } catch (error) {
                console.error(`Error: Invalid zzz duration at line ${lineNum + 1}`);
            }
        }

        // --- PRINT COMMAND ---
        else if (line.startsWith("print ")) {
            const text = line.slice(6);
            console.log(text);
        } else if (line.startsWith("say ")) {
            const text = line.slice(4);
            // Text-to-speech functionality can be implemented using a library like say.js
            console.log(`Say: ${text}`); // Placeholder for actual TTS implementation
        }

        // --- SYSTEM COMMANDS ---
        else if (line === "reboot") {
            try {
                exec('sudo reboot', (error) => {
                    if (error) {
                        console.error(`Error with reboot: ${error}, Common issues are running in chrome, firefox, etc`);
                    }
                });
            } catch (error) {
                console.error(`Error with reboot: ${error}`);
            }
        } else if (line === "restart") {
            console.log("'restart' is the Windows equivalent of the Mech 'reboot' command (Linux-only)");
            exec('shutdown /s', (error) => {
                if (error) {
                    console.error(`Error with restart: ${error}, Common issues are running in chrome, firefox, etc`);
                }
            });
        }

        // --- CONDITIONAL COMMANDS ---
        else if (line.startsWith("if ")) {
            const parts = line.slice(3).split(":", 2);
            if (parts.length === 2) {
                const condition = parts[0].trim();
                const commands = parts[1].trim();

                if (condition === "true") {
                    runMechCode(commands, filename);
                }
            } else {
                console.error(`Error: Invalid if statement at line ${lineNum + 1}`);
            }
        }

        // --- USE COMMAND (import or read another file) ---
        else if (line.startsWith("use ")) {
            let lib = line.slice(4);
            // Add .mech extension if not present
            if (!lib.endsWith(".mech")) {
                lib += ".mech";
            }

            // Handle relative paths if we have a filename context
            let libPath;
            if (filename && !path.isAbsolute(lib)) {
                libPath = path.join(path.dirname(filename), lib);
            } else {
                libPath = lib;
            }

            try {
                const libContent = fs.readFileSync(libPath, 'utf8');
                runMechCode(libContent, libPath);
            } catch (error) {
                console.error(`Library not found: ${libPath}`);
            }
        }

        // --- BINARY COMMAND ---
        else if (line.startsWith("binary ")) {
            const text = line.slice(7);
            const binaryOutput = text.split('').map(char => char.charCodeAt(0).toString(2).padStart(8, '0')).join(' ');
            console.log(binaryOutput);
        }

        // --- COMMENT SYNTAX ---
        else if (line.startsWith("//")) {
            console.log("Info: The comment syntax you are using is non-Mech (C# style).");
            continue;
        }

        // --- UNKNOWN COMMAND ---
        else {
            console.error(`Unknown command at line ${lineNum + 1}: ${line}`);
        }
    }
}

function runMechFile(filename) {
    /**
     * Run a .mech file
     */
    if (!filename.endsWith(".webrobot")) {
        console.error("Error: not a .webrobot file.");
        return false;
    }

    try {
        const content = fs.readFileSync(filename, 'utf8');
        runMechCode(content, filename);
        return true;
    } catch (error) {
        console.error(`File not found: ${filename}`);
        return false;
    }
}

if (require.main === module) {
    const args = process.argv.slice(2);
    if (args.length < 1) {
        console.log("MECH");
        console.log("Web MECHanical robots language");
        console.log("------------------------------------------");
        console.log("Usage: node webmech.js <file.webrobot>");
        console.log("Example: node webmech.js example.webrobot");
    } else {
        const filename = args[0];
        runMechFile(filename);
    }
}
