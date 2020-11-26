number_one = int(input("please enter math score:"))
number_two = int(input("please enter scinse score:"))
number_three = int(input("please enter history score:"))
number_four = int(input("please enter art score:"))
number_five = int(input("please enter english score:"))

ave = number_one + number_five + number_two + number_four + number_three
avr_2 = ave / 5
if avr_2 >=10:
    print("Accept")
if avr_2 <10:
    print("Rejected")
print("your avrange is : " + str(avr_2))