from colorama import Fore, Style

# Definir un diccionario de colores
COLORS = {
    "green": Fore.LIGHTGREEN_EX,
    "red": Fore.LIGHTRED_EX,
    "yellow": Fore.LIGHTYELLOW_EX,
    "cyan": Fore.LIGHTCYAN_EX,
    "white": Fore.LIGHTWHITE_EX,
}

def color(color_name, obj):
    # Verificar si el color_name es válido
    if color_name in COLORS:
        return f"{COLORS[color_name]}{obj}{Style.RESET_ALL}"
    else:
        # Devolver el objeto sin formato si el color no es válido
        return obj