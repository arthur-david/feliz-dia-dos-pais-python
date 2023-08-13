from termcolor import colored, cprint
from time import sleep
from random import uniform
import sys
import pyfiglet as pf

text = "Feliz Dia dos Pais!\n\ (^.^) /"

result = pf.figlet_format(text, font = "doh", width = 200, justify = "center")

for x in result:
    cprint(x, "green", attrs=["bold"], end = "")
    sys.stdout.flush()
    sleep(uniform(0, 0.0003))