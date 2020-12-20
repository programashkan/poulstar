from turtle import textinput, Screen
sc = Screen()
u = textinput("usarname" , "enter usarname")
p = textinput("password", "pls enter your password")

login =("ashkan" , "as123345678")
if u == login[0] and p == login[1]:
    print("welcome:)")
else:
    print("incorect:(")



