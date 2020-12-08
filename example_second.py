from time import sleep
num = int(input("enter number"))


def fd(number):
    con = num
    while con <= number:
        print(con)
        sleep(1)
        con -= 1
fd(num)

