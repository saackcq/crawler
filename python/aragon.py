
import keyboard
import msvcrt

import os

# Limpia la terminal
os.system("cls" if os.name == "nt" else "clear")
numero = ""


         
while True:
    print("ENTER THE FIRST NUMBER")                             
    keyn1 = msvcrt.getch()         
    if keyn1.isdigit(): 
        skey=keyn1.decode()
    print(skey, end="", flush=True )
    cda += skey      
    break    


print("CALCULATOR")
print("---------------------")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
print("5.MODULO")
print("5.EXIT")
print("---------------------")
print("ENTER THE OPERATION: ")

while True:                                     # bucle infinito
    key = msvcrt.getch()                        # Captura 1 tecla
    if key in [b'1', b'2', b'3', b'4', b'5']:   # ¿Es un número del 1-5?
        op = int(key.decode())


        if op == 1 :     
           
        



    




'''

# CAPTURE ONLY NUMBERS

while True:   # bucle infinito, se detiene solo con "break"

    tecla = msvcrt.getch()   # captura la tecla en bytes (ejemplo: b'1', b'a', b'\r')
    if tecla.isdigit():  # si la tecla es un dígito (0–9)
        print(tecla.decode(), end="", flush=True)  # la muestra en pantalla / .decode() convierte ese byte en un string normal 
        numero += tecla.decode()  # la agrega a la variable numero

# ALLOWS TO ERASE NUMBER

    elif tecla == b'\x08':  # Backspace
        if len(numero) > 0:  # solo si hay algo escrito
            # quitar el último carácter
            numero = numero[:-1]
            # mover el cursor atrás, borrar el carácter en pantalla, mover cursor atrás de nuevo
            print("\b \b", end="", flush=True)

    elif tecla == b'\r':  # Enter
        break


def add(num1, num2):
   print("ENTER THE FISRT NUMBER")
    

def show():
    print("ENTER THE FISRT NUMBER")
'''