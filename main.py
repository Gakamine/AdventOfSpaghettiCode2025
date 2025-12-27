import sys
import subprocess

if len(sys.argv) != 3:
    print("Usage: python main.py <day> <part>")
    print("Example: python main.py day1 part1")
    sys.exit(1)

day = sys.argv[1]
part = sys.argv[2]

script_path = f"{day}/{part}.py"

try:
    result = subprocess.run(["python", script_path], cwd="code", capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("Error:", result.stderr)
    print("Exit code:", result.returncode)
except FileNotFoundError:
    print(f"Script {script_path} not found.")
except Exception as e:
    print(f"Error running script: {e}")
