from button import Button
from commands import ButtonCommand
from receptor import Receptor

recep = Receptor()
but = Button()

but.set_command(ButtonCommand(recep, {"Hello": "World"}))
but.action()