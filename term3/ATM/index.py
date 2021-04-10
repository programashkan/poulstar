from tkinter import *
main = Tk()
# ─── FUNCTION ───────────────────────────────────────────────────────────────────

def sing(s):

# ─── RIGESTER ───────────────────────────────────────────────────────────────────
    if s == 'register':
        print("login")

        def sign_up():
            username = sv_username.get()
            password = sv_password.get()


            f = open('term3/ATM/register.txt', 'a')
            f.write('[' + username + ','  + password + ']' '\n') 
            f.close()



        rigester = Toplevel()

        Label(rigester, text  = "password" ).grid(row = 0 , column = 0)
        sv_password = StringVar()
        Entry(rigester , textvariable = sv_password).grid(row = 1 , column = 0)

        Label(rigester, text  = "username" ).grid(row = 2 , column = 0)
        sv_username = StringVar()
        Entry(rigester , textvariable = sv_username).grid(row = 3 , column = 0)
        Button(rigester , text = "sign_up", command = sign_up).grid(row = 4 , column = 0)
# ─── LOGIN ──────────────────────────────────────────────────────────────────────
    if s == 'login':
        def login():
            password_login = sv_password_login.get()
            username_login = sv_username_login.get()
            c = open('term3/ATM/register.txt', 'r')
            
            r = c.read('[' + username + ','  + password + ']')
            if r == c:
                print("hello")




        Label(main, text  = "password" ).grid(row = 0 , column = 0)
        global sv_password_login
        sv_password_login = StringVar()

        Entry(main , textvariable = sv_password_login).grid(row = 1 , column = 0)

        Label(main, text  = "username" ).grid(row = 2 , column = 0)
        global sv_username_login
        sv_username_login = StringVar()

        Entry(main , textvariable = sv_username_login).grid(row = 3 , column = 0)

        Button(main , text = "sign_up", command = login).grid(row = 4 , column = 0)


# ─── MAIN PAGE ──────────────────────────────────────────────────────────────────

Button(main, text = "login" , command = lambda: sing("login")).grid(row = 0 , column = 0)

Button(main, text = "register" , command = lambda: sing("register")).grid(row = 1 , column = 0)
mainloop()

# ─── LOGIN PAGE ─────────────────────────────────────────────────────────────────




mainloop()
