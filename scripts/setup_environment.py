# scripts/setup_environment.py

import os
import subprocess
import sys

def install_packages():
    """Install required packages from requirements.txt."""
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("All required packages have been installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while installing packages: {e}")
        sys.exit(1)

def create_virtual_environment(env_name='venv'):
    """Create a virtual environment."""
    try:
        subprocess.check_call([sys.executable, '-m', 'venv', env_name])
        print(f"Virtual environment '{env_name}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while creating virtual environment: {e}")
        sys.exit(1)

def main():
    """Main function to set up the development environment."""
    create_virtual_environment()
    install_packages()

if __name__ == "__main__":
    main()
