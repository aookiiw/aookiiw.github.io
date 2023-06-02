import random
from prettytable import PrettyTable
import os

#Aqui lo que hago es que me haga una ilustración de tabla para decoración, no es de juego
tablailustracion = """
|   |   |   |   | 
-----------------
|   |   |   |   |
-----------------
|   |   |   |   |
-----------------
|   |   |   |   |
-----------------
|   |   |   |   |
-----------------
|   |   |   |   |
"""
introduccion = """

  ____  _                           _     _                 __  __           _                      _           _ _  
 |  _ \(_)                         (_)   | |               |  \/  |         | |                    (_)         | | | 
 | |_) |_  ___ _ ____   _____ _ __  _  __| | ___     __ _  | \  / | __ _ ___| |_ ___ _ __ _ __ ___  _ _ __   __| | | 
 |  _ <| |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ _ \   / _` | | |\/| |/ _` / __| __/ _ \ '__| '_ ` _ \| | '_ \ / _` | | 
 | |_) | |  __/ | | \ V /  __/ | | | | (_| | (_) | | (_| | | |  | | (_| \__ \ ||  __/ |  | | | | | | | | | | (_| |_| 
 |____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/   \__,_| |_|  |_|\__,_|___/\__\___|_|  |_| |_| |_|_|_| |_|\__,_(_) 
                                                                                                                     
                                                                                                                     

"""
winmessage = """

  _    _                                         _       _ 
 | |  | |                                       | |     | |
 | |__| | __ _ ___    __ _  __ _ _ __   __ _  __| | ___ | |
 |  __  |/ _` / __|  / _` |/ _` | '_ \ / _` |/ _` |/ _ \| |
 | |  | | (_| \__ \ | (_| | (_| | | | | (_| | (_| | (_) |_|
 |_|  |_|\__,_|___/  \__, |\__,_|_| |_|\__,_|\__,_|\___/(_)
                      __/ |                                
                     |___/                                 
"""

lostmessage = """


  _    _                                _ _     _       _ 
 | |  | |                              | (_)   | |     | |
 | |__| | __ _ ___   _ __   ___ _ __ __| |_  __| | ___ | |
 |  __  |/ _` / __| | '_ \ / _ \ '__/ _` | |/ _` |/ _ \| |
 | |  | | (_| \__ \ | |_) |  __/ | | (_| | | (_| | (_) |_|
 |_|  |_|\__,_|___/ | .__/ \___|_|  \__,_|_|\__,_|\___/(_)
                    | |                                   
                    |_|                                   
"""
byemessage ="""

  ___      _ _           _ 
 / _ \    | (_)         | |
/ /_\ \ __| |_  ___  ___| |
|  _  |/ _` | |/ _ \/ __| |
| | | | (_| | | (_) \__ \_|
\_| |_/\__,_|_|\___/|___(_)
                           
                           

"""
#Colores de juego (instrucción)
def coloresguia():
  print("Aquí puede ver los colores con que se puede jugar: ")
  colores = PrettyTable()
  colores.field_names = ["COLORES (CODIGO)", "COLORES (NOMBRE)"]
  colores.add_row(["G B R P Y Pu", "Green, Blue, Red, Pink, Yellow, Purple"])
  print(colores)
  input("Pulsa cualquier tecla \n > ")

#Instucciones de juego
def instrucciones():
  print("Aquí puede ver las reglas del juego: ")
  instruccionesjuego = PrettyTable() #PrettyTable es un modulo externo que he importado a mi codigo para mejor estetica
  instruccionesjuego.field_names = ["N", "Instrucciones"]
  instruccionesjuego.add_row([
    1,
    "El juego se juega con un código secreto de cuatro colores, sin repetición."
  ])
  instruccionesjuego.add_row([
    2,
    "El jugador tiene un número limitado de intentos para adivinar el código secreto dependiedo de nivel que eliga."
  ])
  instruccionesjuego.add_row([
    3,
    "Si colores están en la posición correcta (@) y cuántos colores son correctos pero están en una posición incorrecta (&)."
  ])
  instruccionesjuego.add_row([
    4,
    "El jugador gana el juego si adivina el código secreto antes de que se agoten sus intentos."
  ])
  instruccionesjuego.add_row([
    5,
    "El jugador pierde el juego si no logra adivinar el código secreto en el número limitado de intentos."
  ])
  print(instruccionesjuego)
  input("Pulsa cualquier tecla \n > ")

#Menu de inicio
mainmenu = PrettyTable()
mainmenu.field_names = ["N.", "Acción"]
mainmenu.add_row([1, "Jugar"])
mainmenu.add_row([2, "Reglas de juego"])
mainmenu.add_row([3, "Colores"])
mainmenu.add_row([4, "Salir"])

#Mensaje de perdida
def lost():
  print(lostmessage)
  while True:#Este bucle comprueba si el valor es un numbero o no. Lo he usado muchas veces
    yesorno = input("Quieres volver a menu principal?\n1-Si\nOther-No\n > ")
    try:
      yesorno = int(yesorno)
      break
    except ValueError:
      print("Introduce un numero que sea 1 o 2! ")
    if yesorno == 1:
      menu()
    else:
      print(byemessage)
      exit()

#Aqui lo que hace es elegir quien indica codigo para juego
def selectfirstplayer(user2):
  while True:
    selectfirstplayer = input(" > ")
    try:
      selectfirstplayer = int(selectfirstplayer)
      break
    except ValueError:
      print("Introduce ún numero! ")
  while True:
    if selectfirstplayer == 1:
      print("Perfecto, " + user)
      print("Ahora elige combinación de colores. Tiene que ser de 4 colores en el rango disponible de colores (G B R P Y Pu), separado por comas!")
      while True:
          code = input(" > ").upper().split(",")
          if len(code) != 4:
              print("Por favor, introduce 4 valores!")
          elif not all(i in colours for i in code):
              print("El valor introducido no es un color de juego, recuerda que los colores de juego son: (G B R P Y Pu), separado por comas!")
          else:
              break
      os.system("clear") | os.system("CLS")
      multiplayergame(code)
        
    elif selectfirstplayer == 2:
      print("Perfecto, " + user2)
      print("Ahora elige combinación de colores. Tiene que ser de 4 colores en el rango disponible de colores (G B R P Y Pu), separado por comas!")
      while True:
          code = input(" > ").upper().split(",")
          if len(code) != 4:
              print("Por favor, introduce 4 valores!")
          elif not all(i in colours for i in code):
              print("El valor introducido no es un color de juego, recuerda que los colores de juego son: (G B R P Y Pu), separado por comas!")
          else:
              break
      os.system("clear") | os.system("CLS")
      multiplayergame(code)
    else:
        print("Por favor, introduce el usuario valido!")
        while True:
          selectfirstplayer = input(" > ")
          try:
            selectfirstplayer = int(selectfirstplayer)
            break
          except ValueError:
            print("Introduce ún numero! ")
        break
#El codigo de juego de dos personas. Por defecto el juego es de nivel medio, de 12 turnos.
def multiplayergame(code):
  turno = 0
  resultado = ""
  for i in range(12):
    table.append([" ", " ", " ", " "])
  while turno < 12:
    print("Intento #", turno + 1)
    print("Introduce su suposición. Tiene que ser de 4 colores en el rango disponible de colores (G B R P Y Pu) separado por comas!")
    while True:
      intento = input(" > ").upper().split(",")
      if len(intento) != 4:
        print("Por favor, introduce 4 valores!")
      elif not all(i in colours for i in intento):
        print("El valor introducido no es un color de juego. Recuerda que los colores de juego son: (G B R P Y Pu), separados por comas!")
      else:
        break
    if intento == code:
      print(winmessage)
      while True:
        yesorno = input("¿Quieres volver al menú principal?\n1 - Sí\nOtro - No\n > ")
        try:
          yesorno = int(yesorno)
          break
        except ValueError:
          print("Introduce un número que sea 1 o 2!")
      if yesorno == 1:
        menu()
      else:
        print(byemessage)
        exit()
    resultado = []
    copiadelcodigo = code.copy()  # Make a copy of the code list
    for i in range(4):
      if intento[i] == copiadelcodigo[i]:
        resultado.append("@")
        copiadelcodigo[i] = " "
    for i in range(4):
      if intento[i] in copiadelcodigo:
        resultado.append("&")
        copiadelcodigo[copiadelcodigo.index(intento[i])] = " "
    try:
      resultado = random.sample(resultado, k=4)
    except:
      ()
    table[turno] = intento + resultado
    for i in table:
      print(i)
    turno += 1
  lost()

def bienvenida():
  print(introduccion)
  print(tablailustracion)
  print("Hola" + " " + user + ",", "por favor, indica que quiere hacer:")
#Esta funcion genera codigo con los colores en random
def generate_random_colors():
    code = random.sample(colours, k=4)
    return code

intento = []
table = []
code = []
#Funcion de juego, 20 turnos
def tableez ():
  code = generate_random_colors()
  turno = 0
  resultado = ""
  for i in range(20):#Inicio la tabla para jugar
    table.append([" ", " ", " ", " "])
  while turno < 20:
    print("Intento #", turno + 1)
    print("Introduce su suposición. Tiene que ser de 4 colores en el rango disponible de colores (G B R P Y Pu) separado por comas!")
    while True:
      intento = input(" > ").upper().split(",")#Aqui el jugador indica su suposición, y el codigo lo divide en diferentes valores a lista
      if len(intento) != 4:#Compueba de que si la lista es de 4 valores
          print("Por favor, introduce 4 valores!")
      elif not all(i in colours for i in intento):#Comprueba de que el ususario ha introducido los colores validas (de los colores disponibles)
          print("El valor introducido no es un color de juego, recuerda que los colores de juego son: (G B R P Y Pu), separado por comas!")
      else:
          break
    if intento == code:
      print(winmessage)
      while True:
        yesorno = input("Quieres volver a menu principal?\n1-Si\nOther-No\n > ")
        try:
          yesorno = int(yesorno)
          break
        except ValueError:
          print("Introduce un numero que sea 1 o 2! ")
      if yesorno == 1:
        break
      else:
        print(byemessage)
        exit()
    resultado = []
    copiadelcodigo = code.copy()#Hago una copia y voy quitando los valores encontrados para que no haya repiticiónes en resultado final
    for i in range(4):#Comprobación si hay coincidencia de los colores en la tabla, y si el color está en la posición correcta
      if intento[i] == copiadelcodigo[i]:
        resultado.append("@")
        copiadelcodigo[i] = " "
    for i in range(4):#Comprobación si hay coincidencia de los colores en la tabla.
      if intento[i] in copiadelcodigo:
        resultado.append("&")
        copiadelcodigo[copiadelcodigo.index(intento[i])] = " "
    try:
      resultado = random.sample(resultado, k=4)
    except:
      ()
    table[turno] = intento + resultado
    for i in table:
      print(i)
    turno += 1
  lost()
#Funcion de juego, 12 turnos

def tablemid ():
  code = generate_random_colors()
  turno = 0
  resultado = ""
  for i in range(12):
    table.append([" ", " ", " ", " "])
  while turno < 12:
    print("Intento #", turno + 1)
    print("Introduce su suposición. Tiene que ser de 4 colores en el rango disponible de colores (G B R P Y Pu) separado por comas!")
    while True:
      intento = input(" > ").upper().split(",")
      if len(intento) != 4:
          print("Por favor, introduce 4 valores!")
      elif not all(i in colours for i in intento):
          print("El valor introducido no es un color de juego, recuerda que los colores de juego son: (G B R P Y Pu), separado por comas!")
      else:
          break
    if intento == code:
      print(winmessage)
      while True:
        yesorno = input("Quieres volver a menu principal?\n1-Si\nOther-No\n > ")
        try:
          yesorno = int(yesorno)
          break
        except ValueError:
          print("Introduce un numero que sea 1 o 2! ")
      if yesorno == 1:
        break
      else:
        print(byemessage)
        exit()
    resultado = []
    copiadelcodigo = code.copy()
    for i in range(4):
      if intento[i] == copiadelcodigo[i]:
        resultado.append("@")
        copiadelcodigo[i] = " "
    for i in range(4):
      if intento[i] in copiadelcodigo:
        resultado.append("&")
        copiadelcodigo[copiadelcodigo.index(intento[i])] = " "
    try:
      resultado = random.sample(resultado, k=4)
    except:
      ()
    table[turno] = intento + resultado
    for i in table:
      print(i)
    turno += 1
  lost()
#Funcion de juego, 7 turnos

def tablehard ():
  code = generate_random_colors()
  turno = 0
  resultado = ""
  for i in range(7):
    table.append([" ", " ", " ", " "])
  while turno < 7:
    print("Intento #", turno + 1)
    print("Introduce su suposición. Tiene que ser de 4 colores en el rango disponible de colores (G B R P Y Pu) separado por comas!")
    while True:
      intento = input(" > ").upper().split(",")
      if len(intento) != 4:
          print("Por favor, introduce 4 valores!")
      elif not all(i in colours for i in intento):
          print("El valor introducido no es un color de juego, recuerda que los colores de juego son: (G B R P Y Pu), separado por comas!")
      else:
          break
    if intento == code:
      print(winmessage)
      while True:
        yesorno = input("Quieres volver a menu principal?\n1-Si\nOther-No\n > ")
        try:
          yesorno = int(yesorno)
          break
        except ValueError:
          print("Introduce un numero que sea 1 o 2! ")
      if yesorno == 1:
        menu()
      else:
        print(byemessage)
        exit()
    resultado = []
    copiadelcodigo = code.copy()
    for i in range(4):
      if intento[i] == copiadelcodigo[i]:
        resultado.append("@")
        copiadelcodigo[i] = " "
    for i in range(4):
      if intento[i] in copiadelcodigo:
        resultado.append("&")
        copiadelcodigo[copiadelcodigo.index(intento[i])] = " "
    try:
      resultado = random.sample(resultado, k=4)
    except:
      ()
    table[turno] = intento + resultado
    for i in table:
        print(i)
    turno += 1
  lost()
  
def singleplayer():
  gamelevel()
  while True:
        choosegamelvl = input(" > ")
        try:
          choosegamelvl = int(choosegamelvl)
          if choosegamelvl >= 1 or choosegamelvl <= 3:
            break
        except ValueError:
          print("Introduce un numero y que sea entre 1 y 3! ")
  while True:
    if choosegamelvl == 1:
      tableez()
      choosegamelvl = 0
    elif choosegamelvl == 2:
      tablemid()
      choosegamelvl == 0
    elif choosegamelvl == 3:
      tablehard()
      choosegamelvl == 0
    else:
      menu()


    

def gamelevel():
  print("Perfecto! Por favor, eliga el nivel de juego:")
  print("1. Easy-Peasy-Lemon-Squeezy (20 turnos)")
  print("2. Medium (12 turnos)")
  print("3. HAAAAAAAAAAAAAAAAARD (7 turnos)")
  print("Other. Salir")


singleormulti = PrettyTable()
singleormulti.field_names = ["N.", "Descripción"]
singleormulti.add_rows([
  [1, "Single Player :<"],
  [2, "Multiplayer :>"],
  ["Other", "Salir"],
])

def menu():
  while True:
    print(mainmenu)
    mainmenuchoice = input("Elige una opción \n > ")
    try:
      mainmenuchoice = int(mainmenuchoice)
      while (mainmenuchoice < 1) or (mainmenuchoice > 4):
        print("El número tiene que ser entre 1 y 4!")
        mainmenuchoice = int(input("Elige una opción \n > "))
      if mainmenuchoice == 1:
        print("Perfecto! Vamos a jugAAAAAAAAAr")
        print(singleormulti)
        while True:
          choosegamemode = input(
            "Eliga modo de juego (para salir, cualquier numero desde 3) \n > ")
          try:
            choosegamemode = int(choosegamemode)
            break
          except ValueError:
            print("Introduce un numero! ")
        if choosegamemode == 1:
          singleplayer() #AQUI --------------------------------------------------------------------------------------------------------------------------------------
        elif choosegamemode == 2:
          user2 = input("Perfecto! Introduce el nombre de segundo jugador \n > ")
          print("Hola, " + user2 + ".",
                "Quien elige codigo? \n > 1) " + user + "\n > 2) " + user2)
          code = []
          selectfirstplayer(user2)
          os.system("clear")
          print("PRUEBAAAA")
          #CONTINUEGAMEHERE
        else:
          continue
      elif mainmenuchoice == 2:
        instrucciones()
      elif mainmenuchoice == 3:
        coloresguia()
      elif mainmenuchoice == 4:
        print("Adiós!")
        break  # Salimos del ciclo para terminar el programa
    except ValueError:
      print("Introduzca un número!")


#-----------------------AQUI INICIO EL JUEGO------------------------------

colours = ["G", "B", "R", "P", "Y", "PU"]

user = input("Por favor, introduzca su nombre \n > ")

bienvenida()
menu()