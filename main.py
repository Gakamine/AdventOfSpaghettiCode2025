import sys
import subprocess
import os

if len(sys.argv) < 3 or len(sys.argv) > 4:
    print("Usage: python main.py <day> <part> [ex]")
    print("Example: python main.py day1 part1 ex")
    sys.exit(1)

day = sys.argv[1]
part = sys.argv[2]
use_example = len(sys.argv) == 4 and sys.argv[3] == '-ex'

input_file = f'../inputs/{day}/example.txt' if use_example else f'../inputs/{day}/puzzle.txt'

script_path = f"{day}/{part}.py"

env = os.environ.copy()
env['INPUT_FILE'] = input_file

try:
    result = subprocess.run(["python", script_path], cwd="code", capture_output=True, text=True, env=env)
    print(result.stdout)
    if result.stderr:
        print("Error:", result.stderr)
    print("Exit code:", result.returncode)
except FileNotFoundError:
    print(f"Script {script_path} not found.")
except Exception as e:
    print(f"Error running script: {e}")
