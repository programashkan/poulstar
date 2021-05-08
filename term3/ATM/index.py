from os import read
from tkinter import *
from tkinter import messagebox
import json
import hashlib

# ─── FAUNCTION ──────────────────────────────────────────────────────────────────


def check_digit(a, b, c):

    cond1 = len(sv_card_number.get()) == 16
    cond2 = sv_card_number.get().isdigit()
    if cond1 and cond2:
        e1.config(bg='#78ffa0')
    else:
        e1.config(bg='#ff7a7a')

def find_person(card, path):
    json_data = read_json(path)
    for person in json_data:
        if person["card_number"] == card:
            return json_data.index(person)
    return None


def to_shal(password):
    return hashlib.sha1(password.encode('utf-8')).hexdigest()


def read_json(path):
    with open(path, "r") as file:
        return json.load(file)


def append_json (data,path):
    json_data=read_json(path)
    json_data.append(data)
    with open(path,"w") as file:
        json.dump(json_data, file, indent=4)


def write_json (data, path):
    with open(path,"w") as file:
        json.dump(data, file, indent=4)


def get_id(path):
    json_data=read_json(path)
    return len(json_data)+1


def check_person(name, path):
    json_data = read_json(path)
    for person in json_data:
        if person["name"] == name:
            messagebox.showerror('register faild', "this username is already used")
            return False
    return True       

 # ─── LOGIN AND SIGN IN ──────────────────────────────────────────────────────────


def sing(s):
    if s =="login":
        def log_in():
            username=sv_username.get()
            password=to_shal(sv_password.get())
            data_json = read_json("register.json")
            for person in data_json:
                if person["name"] == username and person['password']==password:
                   menu(person["id"])

        login=Toplevel()
        login.configure(bg= "black")
        Label(login, text="Username", bg = ("black"), fg = ("#FFF59D")).grid(row=0, column=0)
        sv_username=StringVar()
        Entry(login, textvariable=sv_username).grid(row=1,column=0)
        Label(login, text="password", bg = ("black"), fg = ("#FFF59D")).grid(row=2, column=0)
        sv_password=StringVar()
        Entry(login, textvariable=sv_password).grid(row=3,column=0)
        Button(login,text='login',command=log_in, bg = ("#607D8B"), fg = ("#FBC02D")).grid(row=4,column=0)
        Button(login, text="Exit", command=login.destroy, bg = ("#607D8B"), fg = ("#FBC02D")).grid(row=7,column=0)
    elif s=="register":
        def sign_up():
            is_let = check_person(sv_username.get(), 'register.json')
            if is_let:
                new_obj ={
                    "id":get_id("register.json"),
                    "name":sv_username.get(),
                    "password":to_shal(sv_password.get()),
                    'card_number':sv_card_number.get(),
                    "cash":0
                }
                append_json(new_obj, "register.json")
        register=Toplevel()
        register.configure(bg ="black")
        Label(register, text="Username", bg = ("black"), fg = ("#FFF59D")).grid(row=0, column=0)
        sv_username=StringVar()
        Entry(register, textvariable=sv_username).grid(row=1,column=0)
        Label(register,text="password", bg = ("black"), fg = ("#FFF59D")).grid(row=2,column=0)
        sv_password=StringVar()
        Entry(register, textvariable=sv_password).grid(row=3,column=0)
        Label(register,text="card number", bg = ("black"), fg = ("#FFF59D")).grid(row=4,column=0)
        global sv_card_number, e1
        sv_card_number=StringVar()
        sv_card_number.trace("w", check_digit)
        e1 = Entry(register, textvariable=sv_card_number)
        e1.grid(row=5,column=0)
        Button(register,text="sign up",command=sign_up, bg = ("#607D8B"), fg = ("#FBC02D")).grid(row=6,column=0)
        Button(register,text="Exit",command=register.destroy, bg = ("#607D8B"), fg = ("#FBC02D")).grid(row=7,column=0)

# ─── MENU ───────────────────────────────────────────────────────────────────────


def menu(person_id):
    def balance():
        all_data = read_json('register.json')
        your_balance = 0
        for person in all_data:
            if person["id"] == person_id:
                your_balance = person["cash"]                
        top = Toplevel()
        top.configure(bg = "black")
        Label(top, text="Your Balance:", bg = "black", fg = ("#FFF59D")).grid(row=0,column=0)
        Label(top, text=your_balance, bg = "black", fg = ("#FFF59D")).grid(row=1,column=0)    

    def withdrawal():
        all_data = read_json('register.json')
        for person in all_data:
            if person["id"] == person_id:
                if person["cash"] > withdraw_amount.get():
                    person["cash"] -= withdraw_amount.get()
                    write_json(all_data, 'register.json')
                else:
                    messagebox.showerror('Withdraw Fail', "Not Enough Money!!!")

    def transfer_money():
        index_des = find_person(transfer_card.get(), 'register.json')
        if index_des is None:
            messagebox.showerror('transfer Faild', "invaild destenation")

        else:
            all_data = read_json('register.json')
            for person in all_data:
                if person["id"] == person_id:
                    if person["cash"] > transfer_amount.get():
                        person["cash"] -= transfer_amount.get()
                        all_data[index_des]["cash"] += transfer_amount.get()
                        write_json(all_data, "register.json")
                        messagebox.showinfo("Sucsesfully!", "transfer sucsesfully done!")
                        top_t.destroy
                    else:
                        essagebox.showerror('transfer Faild', "Not Enough Money!!!")



    def transfer():
        global top_t
        top_t = Toplevel()
        top_t.configure(bg= "black")
        Label(top_t, text="card:", bg = ("black"), fg = ("#FFF59D")).grid(row=0,column=0)
        global transfer_card
        transfer_card = StringVar()
        Entry(top_t, textvariable = transfer_card).grid(row=0,column=1)

        Label(top_t, text="Amount:", bg = ("black"), fg = ("#FFF59D")).grid(row=1,column=0)
        global transfer_amount
        transfer_amount = IntVar()
        Entry(top_t, textvariable = transfer_amount).grid(row=1,column=1)

        Button(top_t, text="transfer", command= transfer_money, bg = ("#607D8B"), fg = ("#FBC02D")).grid(row=2,column=0)


    def change_pass():
        old_pass = sv_cur_pass.get()
        new_pass01 = sv_new_pass01.get()
        new_pass02 = sv_new_pass02.get()
        all_data = read_json('register.json')
        for person in all_data:
            if person["id"] == person_id:
                if person["password"] == to_shal(old_pass):
                    if new_pass01:
                        if new_pass01 == new_pass02 :
                            person["password"] = to_shal(new_pass02)
                            write_json(all_data, "register.json")
                            messagebox.showinfo("Sucsesfully!", "password changed sucsesfully !")
                            top_c.destroy()
                        else : 
                            messagebox.showerror("Dont match " , "Please type same password")
                    else:
                        messagebox.showerror("Are u ok? " , "Please type  password")
                else : 
                    messagebox.showerror("Wrong password" , "please enter vaild password")








    def withdraw():
        top = Toplevel()
        top.configure(bg = "black")
        Label(top, text="Amount:", bg = ("black"), fg = ("#FFF59D")).grid(row=0,column=0)
        global withdraw_amount
        withdraw_amount = IntVar()
        Entry(top, textvariable=withdraw_amount).grid(row=0,column=1)
        Button(top, text="Withdraw", command=withdrawal, bg = ("#607D8B"), fg = ("#FBC02D")).grid(row=1,column=0)


    def change():
        global top_c
        top_c = Toplevel()
        top_c.configure(bg = "black")

        Label(top_c, text = "currently password : ", bg = ("black"), fg = ("#FFF59D")).grid(row = 0, column = 0)
        global sv_cur_pass
        sv_cur_pass = StringVar()
        Entry(top_c, textvariable = sv_cur_pass).grid(row = 0, column = 1)

        Label(top_c,text = "New Password : " , bg = ("black"), fg = ("#FFF59D")).grid(row = 1, column = 0)
        global sv_new_pass01
        sv_new_pass01 = StringVar()
        Entry(top_c , textvariable = sv_new_pass01).grid(row = 1, column = 1)

        Label(top_c,text = "coniform your  Password : " , bg = ("black"), fg = ("#FFF59D")).grid(row = 2, column = 0)
        global sv_new_pass02
        sv_new_pass02 = StringVar()
        Entry(top_c , textvariable = sv_new_pass02).grid(row = 2, column = 1)

        Button(top_c, text = "change", command = change_pass, bg = ("#607D8B"), fg = ("#FBC02D")).grid(row = 3, column = 1)



    menu_page = Toplevel()
    menu_page.configure(bg= "black")
    Button(menu_page, text="Balance", command=balance, bg = ("#607D8B"), fg = ("#FBC02D")).grid(row=0,column=0)
    Button(menu_page, text="Withraw", command=withdraw, bg = ("#607D8B"), fg = ("#FBC02D")).grid(row=1,column=0)
    Button(menu_page, text="Transfer", command = transfer, bg = ("#607D8B"), fg = ("#FBC02D")).grid(row=2,column=0)
    Button(menu_page, text="ChangePin", command = change, bg = ("#607D8B"), fg = ("#FBC02D")).grid(row=3,column=0 , padx = 0)
    Button(menu_page, text="Cancel", command=menu_page.destroy, bg = ("#607D8B"), fg = ("#FBC02D")).grid(row=4,column=0)


main=Tk()
main.title("main page")
main.geometry("100x100")
main.configure(bg = "black")
Button(main,text="login",command=lambda:sing("login"), bg = ("#607D8B"), fg = ("#FBC02D")).grid(row=0,column=1 , pady= 5 , padx = 10)
Button(main,text="register",command=lambda:sing("register"), bg = ("#607D8B"), fg = ("#FBC02D")).grid(row=1,column=1, pady= 5 , padx = 10)
main.mainloop()