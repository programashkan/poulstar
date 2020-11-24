from time import sleep


second = 0
hour = 0
min = 0

while True:
    sleep(1)
    second += 1
    print(hour, ":", min ,":", second)
    if second == 59:
        min += 1
        second = 0
        if min == 59:
            hour += 1
            min = 0