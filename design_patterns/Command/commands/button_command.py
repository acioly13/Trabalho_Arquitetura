# Command pattern example
from .interface import CommandInterface


class ButtonCommand(CommandInterface):

    def __init__(self, receptor: any, information: any) -> None:
        self.receptor = receptor
        self.message = self.format_information(information)

    def format_information(self, information: any) -> any:
        return information

    def execute(self) -> None:
        self.receptor.process_information(self.message)
