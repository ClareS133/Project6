class MarkdownBuilder:
    def __init__(self, title, description, installation, usage, license, author):
        self.title = title
        self.description = description
        self.installation = installation
        self.usage = usage
        self.license = license
        self.author = author

    def build(self):
        return f"""# {self.title}

## Description
{self.description}

## Installation
{self.installation}

## Usage
{self.usage}

## License
{self.license}

## Author
{self.author}
"""
