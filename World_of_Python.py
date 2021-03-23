#!/bin/python

#===info===
#Who:   karol.farago@t-systems.com
#When:  2021_0222
#What:  text based game for my sons
#Why:   to learn the python basics
''' used new 'features'
import random
fuctions
loops if-else, while
substraction in print
global variables
dictioneries, nested dictioneries
ternary operators
'''
#=================================


import os
from random import randrange
# variables

hero = 0
name = ""
life = 0
damage = 0
heal = 0
special_attack = 0
special = ""
enemy_life=randrange(61,110)
step_counter=0
heal_counter = 2

#representation of rooms
rooms_list = {
  0 : { 'num' : 0,  'name' : "NULL", 'east' : 0, 'west' : 0, 'north' : 0, 'south' : 0, 'enemy' : 0},
  1 : { 'num' : 1,  'name' : "vstupna hala", 'east' : 0, 'west' : 0, 'north' : 2, 'south' : 0, 'enemy' : 0},
  2 : { 'num' : 2,  'name' : "rozdelovac", 'east' : 10, 'west' : 3, 'north' : 0, 'south' : 1, 'enemy' : 0},
  3 : { 'num' : 3,  'name' : "chodba", 'east' : 2, 'west' : 4, 'north' : 0, 'south' : 0, 'enemy' : 0},
  4 : { 'num' : 4,  'name' : "chodba", 'east' : 3, 'west' : 5, 'north' : 0, 'south' : 0, 'enemy' : 0},
  5 : { 'num' : 5,  'name' : "chodba", 'east' : 4, 'west' : 0, 'north' : 6, 'south' : 0, 'enemy' : 0},
  6 : { 'num' : 6,  'name' : "chodba", 'east' : 0, 'west' : 0, 'north' : 0, 'south' : 5, 'enemy' : 'bojovnik'},
  10: { 'num' : 10, 'name' : "chodba", 'east' : 0, 'west' : 2, 'north' : 0, 'south' : 0, 'enemy' : 'drak'}
}

actual_room = rooms_list[1] #initial starting room -> Entry hall
#print('aktual room:' + str(actual_room))
# function for clearing the screen
'''
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
'''

# selection of hero/class
def hero_type(x):
  if x == 1:
    fun_warrior()
  elif x == 2:
    fun_mage()
  elif x == 3:
    fun_ranger()
  elif x == 4:
    fun_knight()
  else:
    print("Taky bojovnik neexistuje.")
   
#case/switches selection of hero/class - not returning the default
##    switcher = {
##        '1': warrior(),
##        '2': mage(),
##        '3': ranger(),
##    }
##    return switcher.get(x, "Skus to este raz.")

def fun_warrior():
  global name
  global life
  global damage
  global heal
  global special_attack
  global special  
  name = "barbar"
  life = 120
  damage = 1
  heal = 10
  special_attack = 22
  special = "brutal utok sekerou"

def fun_mage():
  global name
  global life
  global damage
  global heal
  global special_attack
  global special
  name = "carodejnik"
  life = 80
  damage = 3
  heal = 15
  special_attack = 30
  special = "ohnivy fireball"

def fun_ranger():
  global name
  global life
  global damage
  global heal
  global special_attack
  global special  
  name = "lukostrelec"
  life = 100
  damage = 2
  heal = 12
  special_attack = 25
  special = "utok jedovatymi sipmi"

def fun_knight():
  global name
  global life
  global damage
  global heal
  global special_attack
  global special  
  name = "rytier"
  life = 100
  damage = 2
  heal = 12
  special_attack = 25
  special = "utok obojrucnym mecom"

def fn_action(x):
  '''calling the action function based on players input'''
  #was moved to main section


def fun_attack():
  global enemy_life
  global life
  global damage
  attack_good = randrange(1,21)
  attack_bad = randrange(1,21)

  if attack_good >= attack_bad:
    enemy_life -= (attack_good + damage)
    print("HaHaHa. Prave si ubral nepriatelovi " + str(attack_good + damage) + " zivotov.")     #substraction in print
  else:
    life -= attack_bad
    print(str(attack_bad))    
    print("AU. Prave si dostal na gebulu. Nepriatel ti ubral %s zivotov." %attack_bad)

def fun_special():
  print("special")

def fun_heal():
  global life
  global heal_counter
  global step_counter
  heal_randomizer = randrange(1,21)
  luck_randomizer = randrange(0,2)

  print("heal counter vo fun_heal: " + str(heal_counter))
  if step_counter == 0:
    print("Mi nepovedz, ze uz chces podvadzat. ved boj ani nezacal a uz sa liecis???? Bojuuuuuuuuuj!!!!!")
  elif heal_counter == 0:
    print("Je mi luto, uz sa nevies liecit. Liecenie si pouzil 2 krat.")
  else:
    heal_counter -= 1
    if luck_randomizer == 0:
      print("Si nemehlo, vypadla ti flaska s liecivim lektvarom. Ale sa ti ani necudujem v tom velkom boji.")
    else:
      print("Vyliecil si si %s zivotov" %heal_randomizer)
      life += heal_randomizer


def fn_rooms(direction):
  global actual_room
  if actual_room[direction] == 0:
    print('Au, prave si narazil do steny. Tym smerom nemozes ist.')
  else:
    print("Prave si presiel do novej miestnosti.")
    next_room = rooms_list[actual_room['num']][direction] #>>>>>>>extracting the new rooms number from direction
    actual_room = rooms_list[next_room] #>>>>>>>must return dict
    #print(rooms_list[actual_room])
    #return rooms_list[actual_room]


#==========INTRO==========

playerName = input("Zadaj svoje meno bojovnik: ")
#clear()
print('Ahoj %s. Si pripraveny na boj? Tak podme do toho %s.' %(playerName, playerName))

while hero not in  ( 1, 2, 3, 4):
    print("""Vyber si typ hrdinu:
        1. bojovnik
        2. carodejnik
        3. lukostrelec
        4. rytier""")
    hero = int(input("Zadaj svoj vyber: "))
    print("##########################################")

    #selection of hero and calling its function
    hero_type(hero)
   
print("Dobry vyber. Vybral si si bojovat za %s." %name)    
print("Priprav sa na boj.")

#==========MAIN==========

while life >= 1 and enemy_life >=1 :

#print out the main action menu
  print("##########################################")
  print('STAV:')
  print('Ty: %s zivotov' %life)
  print('On: %s zivotov' %enemy_life)
  print('Si v miestnosti ' + actual_room['name'] + ' a mozes ist tymito smermi: ', end=' ')
  print('dolava' if actual_room['west'] != 0 else '-', end=' ')
  print('dole' if actual_room['south'] != 0 else '-', end=' ')
  print('doprava' if actual_room['east'] != 0 else '-', end=' ')
  print('hore' if actual_room['north'] != 0 else '-', end=' ')
  print()
  print("""Co spravis?
 Vyber si cislo akcie:
        1. utok
        2. special utok
        3. liecenie
 Vyber si cislo pre pohyb:
        4. dolava
        5. dole
        6. doprava
        8. hore""")
  print("##########################################")
 
  usr_input = input()
  if not usr_input.isdigit(): #>>>>>>>only digits are valid inputs
    print("Zadaj iba cisla")
  else:
    usr_input = int(usr_input)
#    if rooms_list[actual_room]['enemy'] == 1:
    if usr_input == 1:
      fun_attack()
    elif usr_input == 2:
      fun_special()
    elif usr_input == 3:
      fun_heal()
    elif usr_input == 4:
      fn_rooms('west')
    elif usr_input == 5:
      fn_rooms('south')
    elif usr_input == 6:
      fn_rooms('east')
    elif usr_input == 8:
      fn_rooms('north')
    else:
      print("Taky vyber si nemal.")

  step_counter += 1

#==========EPILOG==========
if life <= 0:
  print("==========GAME OVER==========")
  print("Je mi luto prehral si. Nepriatelovi este ostalo %s zivotov." %enemy_life)
else:
  print("Gratulujem prave si porazil svojho uhlavneho nepriatela. A to ti este  ostalo %s zivotov." %name)

input()


-- 
Dakujem

S pozdravom

Karol Farago
Karol <karol.farago@gmail.com>
	
11:13 (pred 12 hodinami)
	
komu: mne
#!/bin/python

#===info===
#Who:   karol.farago@t-systems.com
#When:  2021_0222
#What:  text based game for my boys
#Why:   to learn the python basics
''' used new 'features'
import random
functions
loops if-else, while
subtraction in print
global variables
dictionaries, nested dictionaries
list, append
ternary operators
'''
#=================================


import os
from random import randrange
# variables

usr_input=0
name = ""
usr_life = 0
damage = 0
heal = 0
special_attack = 0
special_name = ""
special_counter = 1
back_pack=[]
enemy_life=0
cerberus_life=randrange(61,110)
dragon_life=randrange(120,150)
princess = False
step_counter=0
heal_counter = 2
enemy_name = 0
enemy_bool = False                                                             #>>>>>>>representation of enemy: disabled

#dictionarie representation of rooms
rooms_list = {
  0 : { 'num' : 0,  'name' : "NULL",        'east' : 0, 'west' : 0, 'north' : 0,  'south' : 0,  'enemy' : 0, 'item' : 0},
  1 : { 'num' : 1,  'name' : "vstup",       'east' : 0,     'west' : 0, 'north' : 2,  'south' : 0,  'enemy' : 0, 'item' : 0},
  2 : { 'num' : 2,  'name' : "krizovatka",  'east' : 10,    'west' : 3, 'north' : 8,  'south' : 1,  'enemy' : 0, 'item' : 0},
  3 : { 'num' : 3,  'name' : "chodba1",     'east' : 2, 'west' : 4, 'north' : 0,  'south' : 0,  'enemy' : 0, 'item' : 0},
  4 : { 'num' : 4,  'name' : "chodba2",     'east' : 3, 'west' : 5, 'north' : 0,  'south' : 0,  'enemy' : 0, 'item' : 0},
  5 : { 'num' : 5,  'name' : "chodba3",     'east' : 4, 'west' : 0, 'north' : 6,  'south' : 0,  'enemy' : 0, 'item' : 0},
  6 : { 'num' : 6,  'name' : "arena",       'east' : 0, 'west' : 0, 'north' : 7,  'south' : 5,  'enemy' : 'Cerberus',   'item' : 'kluc'},
  7 : { 'num' : 7,  'name' : "chodba4",     'east' : 0, 'west' : 0, 'north' : 0,  'south' : 6,  'enemy' : 0,    'item' : 'mec drakobijec'},
  8 : { 'num' : 8,  'name' : "komora",      'east' : 0, 'west' : 0, 'north' : 0,  'south' : 2,  'enemy' : 0,        'item' : 'lopta'},
  10: { 'num' : 10, 'name' : "jaskyna",     'east' : 0, 'west' : 2, 'north' : 11, 'south' : 0,  'enemy' : 'Drak',    'item' : 0},
  11: { 'num' : 11, 'name' : "komnata",     'east' : 0, 'west' : 0, 'north' : 0,  'south' : 10, 'enemy' : 0,        'item' : 'princezna'}
}

actual_room = rooms_list[1]                                   #>>>>>>> nested dict for initial starting room -> Entry hall


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


#not used yet
def fn_decorator(func):
 print('+' * 50)
 func()
 print('+' * 50)

# switch for selection of hero/class based on user input and calling it's relevant function
def fn_hero_type(x):
  if x == 1:
    fn_warrior()
  elif x == 2:
    fn_mage()
  elif x == 3:
    fn_ranger()
  elif x == 4:
    fn_knight()
  else:
    print("Taky bojovnik neexistuje.")
   
'''case/switches selection of hero/class - not returning the default
def fn_hero_selection(x):
    switcher = {1 : fn_warrior(), 2 : fn_mage(), 3 : fn_ranger(), 4 : fn_knight()}
    return switcher.get(x, "Skus to este raz.")
'''

def fn_back_pack():
    if actual_room['item'] == 0:
        print('Hladas, hladas, ale nic si nenasiel. Nevies nic zobrat.')
    else:
        print('Nasiel si ' + str(actual_room['item']))        
        back_pack.append(actual_room['item'])
        actual_room['item'] = 0

   
def fn_warrior():
  global name
  global usr_life
  global damage
  global heal
  global special_attack
  global special_name  
  name = "barbar"
  usr_life = 120
  damage = 1
  heal = 10
  special_attack = 40
  special_name = "brutal sekera"

def fn_mage():
  global name
  global usr_life
  global damage
  global heal
  global special_attack
  global special_name
  name = "carodejnik"
  usr_life = 80
  damage = 3
  heal = 15
  special_attack = 30
  special_name = "ohnivy fireball"

def fn_ranger():
  global name
  global usr_life
  global damage
  global heal
  global special_attack
  global special_name  
  name = "lukostrelec"
  usr_life = 100
  damage = 5
  heal = 12
  special_attack = 20
  special_name = "jedovate sipi"

def fn_knight():
  global name
  global usr_life
  global damage
  global heal
  global special_attack
  global special_name  
  name = "rytier"
  usr_life = 100
  damage = 2
  heal = 12
  special_attack = 25
  special_name = "obojrucnym mecom"

def fn_action(x):
  '''calling the action function based on players input'''
  #was moved to main section
 
#@fn_decorator  
def fn_menu():
  '''main game menu print out'''
  print('\n\n\n\n')
  print("#"*50)
  print('STAV:')
  print('%s: \t\t%s zivotov' %(playerName,usr_life))
  print('V batohu mas: ', end=(''))  
  print( *back_pack, sep = ", ")
  print('Mozes ist tymito smermi: ', end=' ')
  print('dolava,' if actual_room['west'] != 0 else '-', end=' ')
  print('dole,' if actual_room['south'] != 0 else '-', end=' ')
  print('doprava,' if actual_room['east'] != 0 else '-', end=' ')
  print('hore' if actual_room['north'] != 0 else '-', end=' ')
  print()
 
  print('''Vyber si cislo pre pohyb:
        4. dolava
        5. dole
        6. doprava
        8. hore
        9. zober predmet''')
  print("#"*50)
  print('Si v miestnosti:  ' + actual_room['name'])
  if actual_room['item'] != 0:
        print('Na zemi vidis %s.' %actual_room['item'])
  print()

def fn_action_menu():
  '''battle menu'''
  print('\n\n\n\n')  
  print("#"*50)
  print('STAV:')
  print('%s: \t\t%s zivotov' %(playerName,usr_life))
  print('%s: \t%s zivotov' %(enemy_name,enemy_life))
  print('V batohu mas: ', end=(''))  
  print( *back_pack, sep = ", ")
  print('Nemozes ist ziadnym smerom, lebo ta neposluchaju nohy!')
 
  print('''Vyber si cislo akcie:
        1. utok
        2. special utok
        3. liecenie\n''')
  print("#"*50)
  print('Si v miestnosti:  ' + actual_room['name'])
 
def fn_dragon():
  global dragon_life    
  global enemy_bool
  global enemy_life
  global usr_life
 
  if 'mec drakobijec' not in back_pack:                                        #GAME OVER
      print('Zomrel si. Draka nevies porazit bez poriadnej zbrane.')
      usr_life = 0
     
  enemy_life = dragon_life  
  enemy_bool = True                                                            #>>>>>>>representation of enemy

def fn_cerberus():
  global cerberus_life    
  global enemy_bool
  global enemy_life
 
  enemy_life = cerberus_life
  enemy_bool = True

 
def fn_attack():
  global enemy_life
  global enemy_bool
  global usr_life
  global damage

  attack_good = randrange(1,21)
  attack_bad = randrange(1,21)

  if attack_good >= attack_bad:
    enemy_life -= (attack_good + damage)
    print("HaHaHa. Ubral si nepriatelovi " +
          str(attack_good + damage) + " zivotov.")                             #>>>>>>>subtraction in print
  else:
    usr_life -= attack_bad
    print(str(attack_bad))    
    print("AU. Prave si dostal na gebulu. Nepriatel ti ubral %s zivotov." %attack_bad)

  if enemy_life <=0:                                                           #remove enemy from dict room if killed
      actual_room['enemy'] = 0
      enemy_bool = False
      print("\n\nGratulujem. Zabil si %s. Mozes pokracovat v dobrodruzstve." %enemy_name)
     
def fn_special():
    global enemy_life
    global special_name
    global special_counter
    if special_counter == 0:
        print("Pouzil si vsetky svoje special utoky. Viac ich nemas.")
    else:
        print("Prave si pouzil svoj specialny utok %s. %s je uplne zniceny z tohto necakaneho utoku." %(special_name, enemy_name))
        print("Ubral si mu %s zivotov." %special_attack)
        enemy_life = enemy_life - special_attack
    special_counter = 0
   
       
def fn_heal():
  global usr_life
  global heal_counter
  global step_counter
  heal_randomizer = randrange(1,21)
  luck_randomizer = randrange(0,2)

  if step_counter == 0:
    print("Mi nepovedz, ze uz chces podvadzat. ved boj ani nezacal a uz sa liecis???? Bojuuuuuuuuuj!!!!!")
  elif heal_counter == 0:
    print("Je mi luto, uz sa nevies liecit. Liecenie si pouzil 2 krat.")
  else:
    heal_counter -= 1
    if luck_randomizer == 0:
      print("Si nemehlo, vypadla ti flaska s liecivim lektvarom. Ale sa ti ani necudujem v tom velkom boji.")
    else:
      print("Vyliecil si si %s zivotov" %heal_randomizer)
      usr_life += heal_randomizer

def fn_rooms(direction):
  '''moving between the rooms'''
  global actual_room
  global usr_life
  global enemy_name
  global princess
 
  if actual_room[direction] == 0:
    print('Auuuuuuu, narazil si do steny. Tym smerom nemozes ist a ubral si si aj jeden zivot.')
    usr_life -= 1
  else:
    print("Presiel si do novej miestnosti.")
 
    next_room = rooms_list[actual_room['num']][direction]                   #>>>>>>>extracting the new room number from direction
    actual_room = rooms_list[next_room]               #>>>>>>>must return dict

    enemy_name = actual_room['enemy']
    if enemy_name != 0:
      print("Pozor, v tejto miestnosti je nepriatel %s !!!!!!!!" %enemy_name)

      if enemy_name == 'Cerberus':
          fn_cerberus()

      if enemy_name == 'Drak':
          fn_dragon()
 
  if actual_room['item'] == 'princezna':
     princess = True
     
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#================================MAIN=======================================
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#==========INTRO==========

playerName = input("Zadaj svoje meno bojovnik: ")                           #>>>>>>>input for players name
#clear()
print('\n\n\n\n')
print('''Ahoj %s. Vitaj v tejto prekliatej krajine. Zly sedemhlavy drak ukradol kralovi princeznu.
Vyhnal vsetkych ludi a uvalil velke prekliatie na cele kralovstvo. Potrebujeme presne
takeho hrdinu ako si ty, aby si nam zachranil princeznu a cele kralovstvo.
Si pripracveny na boj?''' %playerName)
print("Tak podme na to!")
print('\n\n\n\n')

#user selection of hero type and calling it's relevant function to initialize the variables: name,life,damage,.....
while usr_input not in  ( 1, 2, 3, 4):                                         #>>>>>>>only digits 1-4 are valid inputs for hero selection and exiting loop
    print("#"*50)
    print("""Vyber si typ hrdinu:
        1. bojovnik
        2. carodejnik
        3. lukostrelec
        4. rytier""")
    print("#"*50)

    usr_input = input("Zadaj svoj vyber: ")                       #>>>>>>>user input of hero selection

    if not usr_input.isdigit():                       #>>>>>>>only digits are valid inputs, repeate loop for user input
      print("Zadavaj iba cisla!")
      continue

    usr_input = int(usr_input)                   #>>>>>>>conversion input to integer

    fn_hero_type(usr_input)                       #>>>>>>>selection of hero and calling its function

print("Dobry vyber. Vybral si si bojovat za %s." %name)    
print("Priprav sa na boj.")

#++++++++++++++++++++++++++++++++++
#==========MAIN_GAME_LOOP==========
#++++++++++++++++++++++++++++++++++

while usr_life >= 1 and princess == False:                                     # WIN condition, user is alive and princezna is find
 
  step_counter_bool = True                           #>>>>>>>enabling the step counter

  if enemy_bool == True:                                                       #>>>>>>>menu print out based on if enemy is present
      fn_action_menu()                                                         #>>>>>>>if yes only the action menu is available, moving is not possible
  else:
      fn_menu()                       #>>>>>>>if no, only the move menu is available
 
  usr_input = input("Zadaj cislo:")                           #>>>>>>>user input for expected action/move  
 
  if not usr_input.isdigit():                           #>>>>>>>only digits are valid inputs
    print("Zadaj iba cisla")
    continue

  else:
    usr_input = int(usr_input)                           #>>>>>>>conversion input to integer(as all menus works with numbers)
    if enemy_bool == True:                                 #>>>>>>>for rooms withou enemy attack actions are disabled
        if usr_input == 1:
          fn_attack()
        elif usr_input == 2:
          fn_special()
        elif usr_input == 3:
          fn_heal()
        else:
          print("Taky vyber si nemal.")
          step_counter_bool = False                       #>>>>>>>disabling the step counter for invalid step

    elif enemy_bool == False:
        if usr_input == 4:
          fn_rooms('west')
        elif usr_input == 5:
          fn_rooms('south')
        elif usr_input == 6:
          fn_rooms('east')
        elif usr_input == 8:
          fn_rooms('north')
        elif usr_input == 9:
          fn_back_pack()          
        else:
          print("Taky vyber si nemal.")
          step_counter_bool = False                       #>>>>>>>disabling the step counter for invalid step

  step_counter += 1                               #>>>>>>>counter of number of valid actions/steps
   
#++++++++++++++++++++++++++++++++++
#==============EPILOG==============
#++++++++++++++++++++++++++++++++++

if usr_life <= 0:
  print("==========GAME OVER==========")
  print("Je mi luto prehral si. %s este ostalo %s zivotov." %(enemy_name, enemy_life))
else:
  print("\n\n\n\n\nGratulujem, porazil si svojho uhlavneho nepriatela. A zachranil si princeznu. Este ti  ostalo %s zivotov." %usr_life)
  print("Zili ste stastne kym ste nepomreli.")