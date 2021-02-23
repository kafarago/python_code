#!/bin/python

#===info===
#Who:   karol.farago@t-systems.com
#When:  2021_0222
#What:  text based game
#=================================




# function for clearing the screen
def clear(numlines=100):
  """Clear the console.
numlines is an optional argument used only as a fall-back.
"""

  if os.name == "posix":
    # Unix/Linux/MacOS/BSD/etc
    os.system('clear')
  elif os.name in ("nt", "dos", "ce"):
    # DOS/Windows
    os.system('CLS')
  else:
    # Fallback for other operating systems.
    print('\n' * numlines)

# case/switches selection of trieda/class 
def bojovnik(x):
    return {
        '1': print ("bojovnik"),
        '2': print ("carodejnik"),
        '3': print ("lukostrelec")
    }.get(x, "Skus to este raz.")

playerName = input("Zadaj svoje meno bojovnik: ")
clear()
print('Ahoj %s. Si pripraveny na boj? Tak podme do toho %s.' %(playerName, playerName))

trieda = 0
#while trieda != (1 or 2 or 3): >>>>>>>>> not valid conde always will be TRUE
while trieda not in  ( '1', '2', '3'):
    print("""Vyber si typ hrdinu:
        1. bojovnik
        2. carodejnik 
        3. lukostrelec""")
    trieda = input("Zadaj svoj vyber: ")

    bojovnik(trieda)


