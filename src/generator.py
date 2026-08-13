from rich.console import Console

console = Console()

class ReadmeGenerator:
    """Handles file writing and success feedback."""

    def generate(self, markdown):
        try:
            with open("GENERATED_README.md", "w", encoding="utf-8") as file:
                file.write(markdown)

            console.print("[bold green]README.md successfully generated![/bold green]")
        except Exception as e:
            console.print(f"[bold red]Error generating README.md: {e}[/bold red]")
