import time
import os
from colorama import init, Fore, Style
import random

init(autoreset=True)

halloween_title = """
██╗  ██╗ █████╗ ██╗     ██╗      ██████╗ ██╗    ██╗███████╗███████╗███╗   ██╗
██║  ██║██╔══██╗██║     ██║     ██╔═══██╗██║    ██║██╔════╝██╔════╝████╗  ██║
███████║███████║██║     ██║     ██║   ██║██║ █╗ ██║█████╗  █████╗  ██╔██╗ ██║
██╔══██║██╔══██║██║     ██║     ██║   ██║██║███╗██║██╔══╝  ██╔══╝  ██║╚██╗██║
██║  ██║██║  ██║███████╗███████╗╚██████╔╝╚███╔███╔╝███████╗███████╗██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═══╝
"""

pumpkin_face = """
⠀⠀⠀⠀⠀ ⠀⠀⠀⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀                                    
⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣷⣀⣀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀                                     
⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿  ⣿⣿⠀⠀                                   
⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿    ⣿⣿⣿⣿⣿⣿⣿⣿      ⣿⣿⣿⠀⠀                                      
⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿      ⣿⣿⣿      ⣿⣿⣿⣿⣿⠀                          ⣿⣿    ⣿⣿   ⣿⣿
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                            ⣿⣿   ⣿⣿ ⣿⣿
⠀⠀⠀⠀ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧                              ⣿⣿ ⣿⣿ ⣿⣿
⠀⠀⠀⠀ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿     ⣿⣿⣿⣿⣿⣿⣿⣧                                  ⣿⣿⣿⣿
⠀⠀⠀⠀  ⣿⣿  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⣿ ⣿⣿                                ⣿⣿ ⣿⣿
⠀⠀⠀⠀  ⣿⣿⣿  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⣿ ⣿ ⣿⣿                                ⣿⣿    ⣿⣿
⠀⠀⠀⠀   ⣿⣿ ⣿ ⣿ ⣿ ⣿ ⣿ ⣿ ⣿ ⣿⣿⣿⣿                                ⣿⣿      ⣿⣿
⠀⠀⠀⠀     ⣿ ⣿⣿ ⣿ ⣿ ⣿ ⣿⣿⣿⣿⣿                                   ⣿⣿        ⣿⣿
⠀⠀⠀⠀       ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                                                 

"""

spider_web = """
⠀⠀⠀     ⠀⢀⣠⣤⣤⣤⣀⡀⠀⢀⣤⣤⣤⣄⡀⠀⠀⠀
⠀     ⢀⣴⠿⠛⠉⠉⠙⠛⠿⠿⢿⣿⣿⣿⣿
⠀ ⠀⢀⣠⣶⣿   ⣿⣿⣿⣿   ⣿⣿⣿⣿
⠀⠿⠛⠉⠉⠙⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

def animate_halloween():
    clear_screen()
    title_color = Fore.LIGHTRED_EX + Style.BRIGHT
    pumpkin_color = Fore.LIGHTYELLOW_EX + Style.BRIGHT
    spider_color = Fore.LIGHTBLACK_EX + Style.DIM

    print(title_color + center_text(halloween_title))
    print("\n" + spider_color + center_text(spider_web))

    print(pumpkin_color + center_text(pumpkin_face))

    for i in range(5):
        clear_screen()
        print(title_color + center_text(halloween_title))
        print("\n" + spider_color + center_text(spider_web))
        print(pumpkin_color + center_text(pumpkin_face))

        for _ in range(3):
            x, y = random.randint(15, 40), random.randint(2, 10)
            print(("\033[" + str(y) + ";" + str(x) + "H") + "🕷️")

        time.sleep(1.5)
    time.sleep(2)
    clear_screen()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def get_terminal_width(default_width=80):
    try:
        return os.get_terminal_size().columns
    except OSError:
        return default_width

def center_text(text):
    columns = get_terminal_width()
    return "\n".join(line.center(columns) for line in text.splitlines())

animate_halloween()
