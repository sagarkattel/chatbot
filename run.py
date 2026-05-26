import os
import sys
import subprocess

def run():
    # Detect appropriate paths based on OS
    if os.name == "nt":
        venv_streamlit = os.path.join("venv", "Scripts", "streamlit.exe")
    else:
        # Use venv_wsl for WSL/Linux if it exists, otherwise fallback to venv
        if os.path.exists("venv_wsl"):
            venv_streamlit = os.path.join("venv_wsl", "bin", "streamlit")
        else:
            venv_streamlit = os.path.join("venv", "bin", "streamlit")
    
    # Check if streamlit is setup
    if not os.path.exists(venv_streamlit):
        print(f"Error: Streamlit executable not found at '{venv_streamlit}'.")
        print("Please ensure setup is complete.")
        sys.exit(1)
            
    print("=== Launching Streamlit GUI Dashboard ===")
    try:
        subprocess.run([venv_streamlit, "run", "src/app.py"])
    except KeyboardInterrupt:
        print("\nMedibot App stopped.")

if __name__ == "__main__":
    run()

