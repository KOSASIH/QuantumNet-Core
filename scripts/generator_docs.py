#!/usr/bin/env python

import os
import subprocess
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_sphinx_config(docs_dir):
    """Create or update the Sphinx configuration file."""
    conf_file_path = os.path.join(docs_dir, 'conf.py')
    if not os.path.exists(conf_file_path):
        logging.info("Creating Sphinx configuration file...")
        with open(conf_file_path, 'w') as conf_file:
            conf_file.write('''# Sphinx configuration file for the project

import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

project = 'QuantumNet-Core'
author = 'KOSASIH'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = []
html_theme = 'alabaster'
html_static_path = ['_static']
''')
        logging.info("Sphinx configuration file created successfully.")
    else:
        logging.info("Sphinx configuration file already exists.")

def generate_docs(docs_dir, clean=False):
    """Generate documentation using Sphinx."""
    if clean:
        logging.info("Cleaning previous builds...")
        build_dir = os.path.join(docs_dir, '_build')
        if os.path.exists(build_dir):
            subprocess.run(['rm', '-rf', build_dir], check=True)
            logging.info("Previous builds cleaned.")

    logging.info("Generating documentation...")
    try:
        subprocess.run(['sphinx-build', '-b', 'html', docs_dir, os.path.join(docs_dir, '_build', 'html')], check=True)
        logging.info("Documentation generated successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error generating documentation: {e}")
        sys.exit(1)

def main():
    """Main function to run the documentation generation."""
    docs_dir = 'docs'
    clean = '--clean' in sys.argv

    create_sphinx_config(docs_dir)
    generate_docs(docs_dir, clean)

if __name__ == "__main__":
    main()
