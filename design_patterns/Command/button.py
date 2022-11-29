from commands import CommandInterface
from typing import Type


class Button:

    def __init__(self) -> None:
        self.command = None

    def set_command(self, command: Type[CommandInterface]) -> None:
        self.command = command

    def action(self) -> None:
        if self.command:
            self.command.execute()

