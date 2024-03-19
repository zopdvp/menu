import art
from random import choice
from rich.console import Console
from rich.prompt import Prompt

from my_utils import clear_screen
from my_utils import screen_pause
from my_utils import menu_banner

console = Console()

def splash():
    fonts = ['univers', 'tarty1', 'e_fist']
    random_font = choice(fonts)
    text_art = art.text2art("MWS", font=random_font)
    print(text_art)


def display_main_menu():
    clear_screen()
    splash()
    console.print("[bold blue]1.[/bold blue] Ear Patching Menu")
    console.print("[bold blue]2.[/bold blue] Non-Ear Patching Menu")
    console.print("[bold blue]3.[/bold blue] Ear Deployment Menu")
    console.print("[bold blue]4.[/bold blue] Non-Ear Deployment Menu")
    console.print("[bold blue]9.[/bold blue] Exit")
    return Prompt.ask("Enter your choice", default="9")

def display_ear_patch_menu():
    clear_screen()
    menu_banner("EAR Patching Menu", "~", show_time=True)
    console.print("[bold blue]1.[/bold blue] Create Quote")
    console.print("[bold blue]2.[/bold blue] View Quotes")
    console.print("[bold blue]3.[/bold blue] Search Quotes")
    console.print("[bold blue]9.[/bold blue] Back to Main Menu")
    return Prompt.ask("Enter your choice", default="9")


# lines = my_art.split('\n')
# max_width = max(len(line) for line in lines)
# print("Approximate width:", max_width)
def display_nonear_patch_menu():
    clear_screen()
    menu_banner("Non-EAR Patching Menu", "~", show_time=True)
    console.print("[bold blue]1.[/bold blue] Create Invoice")
    console.print("[bold blue]2.[/bold blue] View Invoices")
    console.print("[bold blue]3.[/bold blue] Search Invoices")
    console.print("[bold blue]9.[/bold blue] Back to Main Menu")
    return Prompt.ask("Enter your choice", default="9")


def display_ear_deployment_menu():
    clear_screen()
    menu_banner("EAR Deployment Menu", "~", show_time=True)
    console.print("[bold blue]1.[/bold blue] Create Customer")
    console.print("[bold blue]2.[/bold blue] Update Customer")
    console.print("[bold blue]3.[/bold blue] Search Customer")
    console.print("[bold blue]9.[/bold blue] Back to Main Menu")
    return Prompt.ask("Enter your choice", default="9")


def display_nonear_deployment_menu():
    clear_screen()
    menu_banner("Non-EAR Deployment Menu", "~", show_time=True)
    console.print("[bold blue]1.[/bold blue] Create Property Record")
    console.print("[bold blue]2.[/bold blue] View Properties")
    console.print("[bold blue]3.[/bold blue] Search Properties")
    console.print("[bold blue]9.[/bold blue] Back to Main Menu")
    return Prompt.ask("Enter your choice", default="9")
