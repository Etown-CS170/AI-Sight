import subprocess
import sys
from pathlib import Path

def install_requirements(requirements_file: str):
    """Installs packages listed in the given requirements file."""
    file_path = Path(requirements_file)

    if not file_path.exists():
        print(f"Error: {requirements_file} not found.")
        sys.exit(1)

    print(f"Installing packages from {requirements_file}...")

    try:
        # Run pip to install requirements
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(file_path)])
        print("All packages installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error: An error occurred while installing packages. {e}")
        sys.exit(1)

if __name__ == "__main__":
    requirements_file = "requirements.txt"  # Adjust this if your file has a different name
    install_requirements(requirements_file)
