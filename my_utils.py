from random import randint, uniform
from datetime import datetime
from rich.console import Console

console = Console()

def gen_random_number(low, high, random_float=False, decimal_places=2): # a function with parameters and return
    """
    Generates a random integer or float within a specified range.

    Args:
        low (int or float): The lower bound of the desired range.
        high (int or float): The upper bound of the desired range.
        random_float (bool, optional): If True, generates a random float. 
                                   Defaults to False (generates an integer).
        decimal_places (int, optional): Number of decimal places for the 
                                    random float. Only used if random_float
                                    is True. Defaults to 2.

    Returns:
        int: A random integer between low and high (inclusive) if random_float 
             is False.
        float: A random float between low and high (inclusive), rounded to the 
               specified decimal_places, if random_float is True.
        None: If the input values 'low' or 'high' cannot be cast to the 
              appropriate data type (int or float). 
    """
    if not random_float: # check if random_float is False
        try: # try casting the supplied low and high variables to integers
            low = int(low)
            high = int(high)
            return randint(low,high)
        except ValueError: # trap a ValueError if the cast was not successful and return None
            return None
    else: # random_float is True
        try: # try casting the supplied low and high variables to floats
            low = float(low)
            high = float(high)
            return round(uniform(low,high),decimal_places)
        except ValueError: # trap a ValueError if the cast was not successful and return None
            return None

def banner(text, box_char="=", show_time=False): # a function with parameters
    """
    Creates a simple text banner with customisable borders.

    Args:
        text (str): The text to be displayed within the banner.
        box_char (str, optional): The character used to form the banner's 
            border. Defaults to '='.

    Notes:
        * '=' creates a border with corners ('+').
        * '*' creates a border with asterisks on the text line.
        * Any other character creates a simple border without embellishments.
    """
    text_len = len(text) + 8
    match box_char:
        case "=": # check for '=' as the box character and add '+' for the corners and '|' for the end of text line
            print(f"+{text_len * box_char}+")
            print(f"|    {text}    |")
            print(f"+{text_len * box_char}+")
            if show_time:
                date_today = datetime.now().strftime("%d/%m/%y") # todays date in dd/mm/yy format
                time_now = datetime.now().strftime("%H:%M:%S") # time to the second
                print(f"{date_today:<{text_len - (len(time_now) - 1)}} {time_now}")  # Adjust padding if needed
                print()  # Extra newline
            print()
        case "*": # check for '*' as the box character and add '*' for the end of text line
            print(f"{text_len * box_char}")
            print(f"*   {text}   *")
            print(f"{text_len * box_char}")
            if show_time:
                date_today = datetime.now().strftime("%d/%m/%y") # todays date in dd/mm/yy format
                time_now = datetime.now().strftime("%H:%M:%S") # time to the second
                print(f"{date_today:<{text_len - (len(time_now) + 1)}} {time_now}")  # Adjust padding if needed
                print()  # Extra newline
            print()
        case _: # any other box_char is just used at the top and bottom
            # print("Using the catchall")
            print(f"{text_len * box_char}")
            print(f"    {text}    ")
            print(f"{text_len * box_char}")
            if show_time:
                date_today = datetime.now().strftime("%d/%m/%y") # todays date in dd/mm/yy format
                time_now = datetime.now().strftime("%H:%M:%S") # time to the second
                print(f"{date_today:<{text_len - (len(time_now) + 1)}} {time_now}")  # Adjust padding if needed
                print()  # Extra newline
            print()

def menu_banner(text, box_char="=", show_time=False): # a function with parameters
    """
    Creates a simple text banner with customisable borders.

    Args:
        text (str): The text to be displayed within the banner.
        box_char (str, optional): The character used to form the banner's 
            border. Defaults to '='.

    Notes:
        * '=' creates a border with corners ('+').
        * '*' creates a border with asterisks on the text line.
        * Any other character creates a simple border without embellishments.
    """
    text_len = len(text) + 8
    
    match box_char:
        case "=": # check for '=' as the box character and add '+' for the corners and '|' for the end of text line
            console.print(f"[bold green]+{text_len * box_char}+[/bold green]")
            console.print(f"[bold green]|[/bold green]    [bold]{text}[/bold]    [bold green]|[/bold green]")
            console.print(f"[bold green]+{text_len * box_char}+[/bold green]")
            if show_time:
                date_today = datetime.now().strftime("%d/%m/%y") # todays date in dd/mm/yy format
                time_now = datetime.now().strftime("%H:%M:%S") # time to the second
                console.print(f"[bold cyan]{date_today:<{text_len - (len(time_now) - 1)}} {time_now}[/bold cyan]")  # Adjust padding if needed
                console.print()  # Extra newline
            console.print()
        case "*": # check for '*' as the box character and add '*' for the end of text line
            console.print(f"[bold green]{text_len * box_char}[/bold green]")
            console.print(f"[bold green]*[/bold green]   [bold]{text}[/bold]   [bold green]*[/bold green]")
            console.print(f"[bold green]{text_len * box_char}[/bold green]")
            if show_time:
                date_today = datetime.now().strftime("%d/%m/%y") # todays date in dd/mm/yy format
                time_now = datetime.now().strftime("%H:%M:%S") # time to the second
                console.print(f"[bold cyan]{date_today:<{text_len - (len(time_now) + 1)}} {time_now}[/bold cyan]")  # Adjust padding if needed
                console.print()  # Extra newline
            console.print()
        case _: # any other box_char is just used at the top and bottom
            # console.print("Using the catchall")
            console.print(f"[bold green]{text_len * box_char}[/bold green]")
            console.print(f"    [bold]{text}[/bold]    ")
            console.print(f"[bold green]{text_len * box_char}[/bold green]")
            if show_time:
                date_today = datetime.now().strftime("%d/%m/%y") # todays date in dd/mm/yy format
                time_now = datetime.now().strftime("%H:%M:%S") # time to the second
                console.print(f"[bold cyan]{date_today:<{text_len - (len(time_now) + 1)}} {time_now}[/bold cyan]")  # Adjust padding if needed
                console.print()  # Extra newline
            console.print()

def clear_screen():
    print("\033[H\033[J", end="")  # \033[H moves cursor to top left; \033[J clears


def screen_pause():
    press_enter = input("Press enter to continue ...")
