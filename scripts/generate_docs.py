# scripts/generate_docs.py

import os
import subprocess
import sys

def generate_docs():
    """Generate documentation using Sphinx."""
    try:
        # Check if Sphinx is installed
        subprocess.check_call([sys.executable, '-m', 'sphinx', '-b', 'html', 'docs/source', 'docs/build'])
        print("Documentation generated successfully in 'docs/build'.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while generating documentation: {e}")
        sys.exit(1)

def main():
    """Main function to generate documentation."""
    generate_docs()

if __name__ == "__main__":
    main()
