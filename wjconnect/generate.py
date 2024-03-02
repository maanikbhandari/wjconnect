import subprocess

def run_scripts():
    # Path list for the 7 scripts
    script_paths = [
        "activate-dom2dom.py",
        "activate-dom2lac.py",
        "activate-dom2tatltpac.py",
        "activate-dom2tb.py",
        "activate-lac2dom.py",
        "activate-tatltpac2dom.py",
        "activate-tb2dom.py"
    ]

    for script_path in script_paths:
        print(f"Running script: {script_path}")
        
        # Run the Python script using subprocess
        subprocess.run(["python", script_path])

if __name__ == "__main__":
    run_scripts()