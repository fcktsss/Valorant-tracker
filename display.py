import colorsys
from rich.console import Console

PATH = "display.py"
print(f"Loading {PATH}...")
from colorsys import rgb_to_hsv, hsv_to_rgb



console = Console()

def afficher_titre():
    console.print("VALORANT TRACKER", style="bold red")