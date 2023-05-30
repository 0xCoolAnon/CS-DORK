# CODER: 0xCoolAnon
# This file have a virus


from googlesearch import search
from colorama import Fore
import os

def banners():
    print()
    print(Fore.LIGHTWHITE_EX + "       ░█████╗░░██████╗  ░█████╗░██████╗░███████╗░██╗░░░░░░░██╗")
    print(Fore.LIGHTWHITE_EX + "       ██╔══██╗██╔════╝  ██╔══██╗██╔══██╗██╔════╝░██║░░██╗░░██║")
    print(Fore.LIGHTWHITE_EX + "       ██║░░╚═╝╚█████╗░  ██║░░╚═╝██████╔╝█████╗░░░╚██╗████╗██╔╝")
    print(Fore.LIGHTWHITE_EX + "       ██║░░██╗░╚═══██╗  ██║░░██╗██╔══██╗██╔══╝░░░░████╔═████║░")
    print(Fore.LIGHTWHITE_EX + "       ╚█████╔╝██████╔╝  ╚█████╔╝██║░░██║███████╗░░╚██╔╝░╚██╔╝░")
    print(Fore.LIGHTWHITE_EX + "       ░╚════╝░╚═════╝░  ░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░")
    print(Fore.YELLOW + "══════════════════╦═══════════════════════════╦═══════════════════")
    print(Fore.YELLOW + "      ╔════════════╩═══════════════════════════╩════════════╗")
    print(Fore.YELLOW + "      ║ • " + Fore.GREEN + "CODER " + Fore.RED + "   |" + Fore.LIGHTYELLOW_EX + "           0xCOOLANON                  " + Fore.YELLOW + " ║")
    print(Fore.YELLOW + "      ║ • " + Fore.GREEN + "GITHUB " + Fore.RED + "  |" + Fore.LIGHTYELLOW_EX + "      GITHUB.COM/0XCOOLANON            " + Fore.YELLOW + " ║")
    print(Fore.YELLOW + "      ╚═════════════════════════════════════════════════════╝")

banners()
try:
    # Prompt the user for inputs
    ny1 = input(f"{Fore.YELLOW}\n[💀] #OpsHebrew [💀]{Fore.RED} - {Fore.GREEN}Dork: {Fore.CYAN}")
    ny2 = int(input(f"{Fore.YELLOW}\n[💀] #OpsHebrew [💀]{Fore.RED} - {Fore.GREEN}Amount: {Fore.CYAN}"))
    ny3 = int(input(f"{Fore.YELLOW}\n[💀] #OpsHebrew [💀]{Fore.RED} - {Fore.GREEN}Time (Minutes): {Fore.CYAN}"))

    # Convert minutes to seconds
    ny3 = ny3 * 60

    custom_file_name = input(f"{Fore.YELLOW}\n[💀] #OpsHebrew [💀]{Fore.RED} - {Fore.GREEN}File Name You Want to Create: {Fore.CYAN}")
    print(f'{Fore.BLUE}\n═════════════════════════════════════════════')

    result = "result"  # Specify the name of the directory
    os.makedirs(result, exist_ok=True)
    custom_file_path = os.path.join('result', custom_file_name)

    nyx = 0
    ny2 = 10  # Initial value for the number of results
    while nyx < ny2:
        for i in search(ny1, num_results=ny2, start=nyx, stop=None, pause=ny3):
            with open(custom_file_path, 'a') as f:
                f.write(f'{i}\n')
            nyx += 1
            print(f'{Fore.WHITE}       {nyx}) {Fore.CYAN}{i}')
            if nyx >= ny2:
                break

        if nyx < ny2:
            prompt = input(f"{Fore.YELLOW}\n[💀] #OpsHebrew [💀]{Fore.RED} - {Fore.GREEN}Continue searching for more results? (Y/N): {Fore.CYAN}")
            if prompt.lower() != 'y':
                break

        ny2 += 10  # Increase the number of results by 10 for each iteration

    print(f'{Fore.BLUE}═════════════════════════════════════════════')
    print(f'{Fore.YELLOW}\n[D0rK!] {Fore.GREEN}Saved: {Fore.GREEN}{custom_file_path}')
except ValueError:
    exit(f'{Fore.RED}Exit! Input error')
except KeyboardInterrupt:
    exit(f'\n\n{Fore.RED}Exit!')
