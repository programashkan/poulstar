number_one = int(input("please enter student math score:"))

number_two  = int(input("please enter student arabic score:"))
  
number_three = int(input("please enter student history score:"))

number_four = int(input("please enter student art score:"))

number_five = int(input("please enter student persian score:"))

number_six = int(input("please enter student english score:"))

number_seven = int(input("please enter student Physics score:"))

number_eight = int(input("please enter student chemistry score:"))

number_nine = int(input("please enter student biology score :"))

number_nine = int(input("please enter student sport score :"))

number_ten = int(input("please enter student dini score :"))

number_eleven  = int(input("please enter student ghoran score :"))


ave = number_one + number_five + number_two + number_four + number_three + number_six +number_seven + number_eight + number_nine +number_ten + number_eleven
avr_2 = ave / 11
if avr_2 >=10:
    print("Accept")
if avr_2 <10:
    print("Rejected")
print("your avrange is : " + str(avr_2))