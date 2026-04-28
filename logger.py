import datetime
from colorama import Fore, Style, init

init(autoreset=True)


def _ts():
    return datetime.datetime.now().strftime("%H:%M:%S")


def info(msg):
    print(f"{Fore.CYAN}[{_ts()}] INFO  → {msg}{Style.RESET_ALL}")


def success(msg):
    print(f"{Fore.GREEN}[{_ts()}] PASS  ✔ {msg}{Style.RESET_ALL}")


def warn(msg):
    print(f"{Fore.YELLOW}[{_ts()}] WARN  ⚠ {msg}{Style.RESET_ALL}")


def error(msg):
    print(f"{Fore.RED}[{_ts()}] ERROR ✘ {msg}{Style.RESET_ALL}")


def price(product, amount):
    border = "─" * 48
    print(
        f"\n{Fore.MAGENTA}{border}\n"
        f"  🛒  PRODUCT : {product}\n"
        f"  💵  PRICE   : {amount}\n"
        f"{border}{Style.RESET_ALL}\n"
    )
