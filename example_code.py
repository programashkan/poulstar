str_id = input("please enter your id: ")
lst_id = list(str_id)
print(lst_id)
print(lst_id[9])


counter = 10
mul = 0
sum = 0
for i in lst_id:
    if counter >= 2:
        mul = int(i) * counter
        sum += mul
        print(i, counter, mul)
        counter -= 1
print(sum)
r = sum % 11
print(r)

if r < 2:
    if int(lst_id[9]) == r:
        print("correct")
    else:
        print("incorrect")
else:
    if int(lst_id[9]) == 11 - r:
        print("correct")
    else:
        print("incorrect")