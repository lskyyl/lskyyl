
# Password:

print('BANK OF MAZEN')
print('                                                AAA                                                                                   ')  
print('          MMMM             MMMM                AA AA                ZZZZZZZZZZZZZ       EEEEEEEEEEEEE      NNNN           NN          ')                                                       
print('          MM MM           MM MM               AA   AA                        ZZZ        EE                 NN NN          NN          ')                              
print('          MM  MM         MM  MM              AA     AA                      ZZZ         EE                 NN  NN         NN          ')                         
print('          MM   MM       MM   MM             AA       AA                    ZZZ          EE                 NN   NN        NN          ')                    
print('          MM     MM   MM     MM            AA         AA                  ZZZ           EE                 NN     NN      NN          ')                                             
print('          MM      MM MM      MM           AA           AA                ZZZ            EEEEEEEEEEEEE      NN      NN     NN          ')                                  
print('          MM       MMM       MM          AAAAAAAAAAAAAAAAA              ZZZ             EE                 NN       NN    NN          ')                                                      
print('          MM                 MM         AA               AA            ZZZ              EE                 NN        NN   NN          ')                                                                             
print('          MM                 MM        AA                 AA          ZZZ               EE                 NN         NN  NN          ')                                                      
print('          MM                 MM       AA                   AA        ZZZ                EE                 NN          NN NN          ')                                     
print('          MM                 MM      AA                     AA      ZZZZZZZZZZZZZ       EEEEEEEEEEEEE      NN           NNNN          ')  


pin = int(input('Enter your PIN: '))

while pin != 1122:
    pin = int(input('Incorrect PIN. Enter your PIN again: '))
if pin == 1122:
  print('PIN accepted!')
print('--------------------------------------------------------------------------------------')
#####################################################


# Art:

print('                                                AAA                                                                                   ')  
print('          MMMM             MMMM                AA AA                ZZZZZZZZZZZZZ       EEEEEEEEEEEEE      NNNN           NN          ')                                                       
print('          MM MM           MM MM               AA   AA                        ZZZ        EE                 NN NN          NN          ')                              
print('          MM  MM         MM  MM              AA     AA                      ZZZ         EE                 NN  NN         NN          ')                         
print('          MM   MM       MM   MM             AA       AA                    ZZZ          EE                 NN   NN        NN          ')                    
print('          MM     MM   MM     MM            AA         AA                  ZZZ           EE                 NN     NN      NN          ')                                             
print('          MM      MM MM      MM           AA           AA                ZZZ            EEEEEEEEEEEEE      NN      NN     NN          ')                                  
print('          MM       MMM       MM          AAAAAAAAAAAAAAAAA              ZZZ             EE                 NN       NN    NN          ')                                                      
print('          MM                 MM         AA               AA            ZZZ              EE                 NN        NN   NN          ')                                                                             
print('          MM                 MM        AA                 AA          ZZZ               EE                 NN         NN  NN          ')                                                      
print('          MM                 MM       AA                   AA        ZZZ                EE                 NN          NN NN          ')                                     
print('          MM                 MM      AA                     AA      ZZZZZZZZZZZZZ       EEEEEEEEEEEEE      NN           NNNN          ')  
print('--------------------------------------------------------------------------------------')                                                            
#####################################################


# "if your age is... ":

age = 17

if age > 17:
    print("you are older than 17")
elif age == 17:
    print("thats your age")
else:
    print("you are younger than 17")
print('----------------------------')
#####################################################


# Welcome Admin:

username = "admin"
password = "password"

if username == "admin" and password == "password":
    print("welcome admin")
else:
    print("Incorrect Credentials")
print('----------------------------')
#####################################################

# Name Writer:    

names = ("Mazen","Yousef","Alsadoun")

for i in names:
    print("My name is "+i)


# Number + 1:

num = 3
while num < 10:
        print(f'num is : {num}')
        num = 1 + num
print('-------------------')
#####################################################


# Grades that passed/Failed part 1:

grades = [65,80,60,61,93,76,36,85,79,48]

passes_grades = [grade for grade in grades if grade > 59]
failed_grades = [grade for grade in grades if grade < 60]
 
print(f"Grages that passed: {passes_grades}")
print(f"Grades that failed: {failed_grades}")
print('-------------------------------------------')
#####################################################

# Grades that passed/Failed part 2:

grades = [65,80,60,61,93,76,36,85,79,48]
passed = []
failed = []

for i in grades:
    if i >= 60:
        passed.append(i)
    else:
        failed.append(i)
print(f"Grades that passed: {passed}")
print(f"Grades that failed: {failed}")
print('-------------------------------------------')
#####################################################


# Fahrenheit to Celseus:

Fahrenheit = float(input("Whats the wehter in Fahrenheit? "))

F_to_C = Fahrenheit - 32 
F_to_C2 = F_to_C / 1.8

print(f"The wether in Celsius is {F_to_C2} C")
print('-----------------------------------------------------')
#####################################################


#BMI Calculater:

mass = float(input('Whats your wight? '))
height = float(input('Whats your height? '))

bmi = mass / (height**2)


print(f'Your BMI is: {bmi:4f} Kg/m2')
print('------------------------------------------------------')
#####################################################


# Right Triangle Calculater:

a1 = float(input("Enter a: "))
b1 = float(input('Enter b: '))

a2 = a1 ** 2
b2 = b1 ** 2

C = (a2 + b2)**0.5
print(f'C = {C}')
print('-------------------------------------------------------')
#####################################################


# School CGP Calculator:

grade1 = float(input("shcool CGP: "))
grade2 = float(input("gdrat: "))
grade3 = float(input("tasele: "))

final_grade = grade1 * 0.30 + grade2 * 0.30 + grade3 * 0.40

print(f"(CGP) is: %{final_grade:f}")
print('--------------------------------------------------')
#####################################################

# currency converter:

pesos = float(input('How much do you have left in pesos? '))
soles = float(input('How much do you have left in soles? '))
realis = float(input('How much do you have in realis? '))

pesos_usa = pesos / 18.51
soles_usa = soles / 3.57
realis_usa = realis / 5.555

total = pesos_usa + soles_usa + realis_usa
 
print(total)
print('---------------------------')
#####################################################

# Ph level:

ph = float(input('What is the Ph? '))

if ph > 7:
  print('Basic')
elif ph < 7:
  print('Acidic')
else:
  print('Neutral')
print('---------------------------')
#####################################################

# Magic 8 Ball:      +   Random Numbers. 

import random

question = input('Question:  ')
num = random.randint(1,9)

if num == 1:
  print('Magic 8 Ball: Yes - definitely.')
elif num == 2:
  print('Magic 8 Ball: It is decidedly so.')
elif num == 3:
  print('Magic 8 Ball: Without a doubt.')
elif num == 4:
  print('Magic 8 Ball: Reply hazy, try again.')
elif num == 5:
  print('Magic 8 Ball: Ask again later.')
elif num == 6:
  print('Magic 8 Ball: Better not tell you now.')
elif num == 7:
  print('Magic 8 Ball: My sources say no.')
elif num == 8:
  print('Magic 8 Ball: Outlook not so good.')
else:
  print('Magic 8 Ball: Very doubtful.')
print('------------------------------------')
#####################################################

# the_cyclone.py:

height = int(input('Height: '))

cred = int(input('Credit: '))

if height >= 137 and cred >= 10:
  print('Enjoy the ride!')
elif height <= 137 and cred >= 10:
  print('You are not tall enough to ride.')
elif height >= 137 and cred <= 10:
  print("You don't have enough credits.")
else:
  print("You have not met either of the requirement")
print('------------------------------------')
#####################################################

# 🦁 Gryffindor, 🦅 Ravenclaw, 🦡 Hufflepuff, 🐍 Slytherin:

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print('Q1) Do you like Dawn or Dusk?')
print('    1) Dawn')
print('    2) Dusk')
anwer1 = int(input('Enter your asnwer ( 1 or 2 ):'))
if anwer1 == 1:
 Gryffindor += 1
 Ravenclaw += 1
elif anwer1 == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print('Wrong input.')


print('Q2) When I’m dead, I want people to remember me as:')
print('    1) The Good')
print('    2) The Great')
print('    3) The Wise')
print('    4) The Bold')

anwer2 = int(input('Enter you anwer (1-4):'))

if anwer2 == 1:
  Hufflepuff += 2
elif anwer2 == 2:
  Slytherin += 2
elif anwer2 == 3:
  Ravenclaw += 2
elif anwer2 == 4:
  Gryffindor += 2
else:
  print('Wrong input.')

print("Q3) Which kind of instrument most pleases your ear?")
print('    1) The violin')
print('    2) The trumpet')
print('    3) The piano')
print('    4) The drum')

anwer3 = int(input('Enter anwer (1-4):'))

if anwer3 == 1:
  Slytherin += 4
elif anwer3 ==2:
  Hufflepuff += 4
elif anwer3 == 3:
  Ravenclaw += 4
elif anwer3 == 4:
  Gryffindor += 4
else:
  print('Wrong input.')
print('Final Results:   ')
print(f'Slytherin: {Slytherin}')
print(f'Hufflepuff: {Hufflepuff}')
print(f'Ravenclaw: {Ravenclaw}')
print(f'Gryffindor: {Gryffindor}')
print('------------------------------------')
#####################################################

# Password **************************


print('BANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))

while pin != 1234:
    pin = int(input('Incorrect PIN. Enter your PIN again: '))
if pin == 1234:
  print('PIN accepted!')
print('------------------------------------')
#####################################################

# "99 Bottles of Beer"

for x in range(99, 0, -1):
  print(f'{x} bottles of beer on the wall')
  print(f'{x} bottles of beer')
  print('  Take one down, pass it around')
print('------------------------------------')
#####################################################

#Fizz Buzz: 


for i in range(1, 101):
  if i % 3 == 0:
    print('Fizz')
  elif i % 5 == 0:
    print('Buzz')
  elif i % 3 == 0 and i % 5 == 0:
    print('FizzBuzz')
  else:
    print(i)
print('------------------------------------')
#####################################################
