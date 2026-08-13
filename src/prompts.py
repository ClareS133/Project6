from InquirerPy import inquirer

class PromptService:
    """Handles all user prompts using InquirerPy."""

    LICENSES = [
        "MIT License",
        "Apache License 2.0",
        "GNU GPL v3",
        "GNU LGPL v3",
        "Mozilla Public License 2.0",
        "Creative Commons (CC0, CC BY)",
        "Unlicense"
    ]

    def get_project_title(self):
        return inquirer.text(message="Project Title:").execute()

    def get_description(self):
        return inquirer.text(message="Project Description:").execute()

    def get_installation(self):
        return inquirer.text(message="Installation Instructions:").execute()

    def get_usage(self):
        return inquirer.text(message="Usage Instructions:").execute()

    def get_license(self):
        return inquirer.select(
            message="Choose a license:",
            choices=self.LICENSES
        ).execute()

    def get_author(self):
        return inquirer.text(message="Author / Contact Info:").execute()
