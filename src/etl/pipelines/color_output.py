from collections import defaultdict
from typing import Optional

from dynaconf import LazySettings

COLOR_END = "\033[0m"
COLORS = defaultdict(lambda: "\u001b[38;5;256m")
COLORS.update({
    "red": "\u001b[38;5;1m",
    "blue": "\u001b[38;5;4m",
    "green": "\u001b[38;5;2m",
    "yellow": "\u001b[38;5;3m",
})


def color_print(message: str, color: Optional[str] = None) -> None:
    print(f"{COLORS[color]}{message}{COLOR_END}")


def run(config: LazySettings):
    color_print(f"I should print [{config.COLOR}] colored message", config.COLOR)
