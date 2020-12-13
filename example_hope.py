from time import sleep
from turtle import textinput , Screen
sc = Screen()
sc.setup(1, 1)
x = textinput("Multiplication", "please enter number")



number = 0
max = 7
while True:
    sleep(0.5)
    print(number)
    number += 1
    if number % int(x) == 0:
        print("hope")



