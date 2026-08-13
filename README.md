# smurfs

## Description
blue people crafter

## Installation
42 of this and that

## Usage
once a day

## License
MIT License

## Author
tel no




Project 6

GitHub README Generator
A Python-based command-line application that interactively generates a professional README.md file for any GitHub project.
Built using InquirerPy for prompts and Rich for styled console output. 
A simple, interactive command-line tool that helps you quickly generate clean, professional README files for your GitHub projects.  
Built with Python, InquirerPy for prompts, and Rich for styled console output.

*Features*
Interactive prompts for:
Project Title
Description
Installation Instructions
Usage Instructions
License Selection (dropdown)
Author / Contact Information
License selection using InquirerPy
Styled CLI feedback using Rich
Generates a fully formatted GitHub‑standard README.md
Modular, PEP8‑compliant code
Virtual environment + dependency management
Error handling for invalid input


Installation

Clone the repository and install dependencies inside a virtual environment:

```bash
git clone <your-repo-url>
cd Project_6

# Create and activate virtual environment
python -m venv .venv
. .venv/Scripts/Activate.ps1   # Windows PowerShell

# Install required packages
python -m pip install -r requirements.txt


Usage
Run the CLI tool:

bash
python src/cli.py
You will be prompted for:

Project Title

Description

Installation Instructions

Usage Information

License
Author / Contact Info

After completing the prompts, a fully formatted README.md file will be created in your project folder.


Example Output
markdown
# My Awesome Project

## Description
A short description of what the project does.

## Installation
Steps to install and set up the project.

## Usage
Instructions on how to use the project.

## License
MIT License

## Author
Your Name


License Options
The generator supports:
MIT
Apache 2.0
GPL v3
LGPL v3
MPL 2.0
Creative Commons
Unlicense



Technologies Used
Python 3.10+
InquirerPy — interactive CLI prompts
Rich — styled console output
Markdown — README formatting

Author
Clare Spencer
Doncaster, England