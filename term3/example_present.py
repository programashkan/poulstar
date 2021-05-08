        def withdrawal():
            all_data = read_json("ATM/register.json")
            for person in all_data:
            if person["id"] == person_id:
                if person["cash"]> withdraw_amount.get()
                person["cash"] -= withdraw_amount.get()
                    write_json(all_data, "ATM/register.json")
                else:
                    messagebox.showerror("withdraw faild",'not eanugh money!!!')
        def withdraw():
            top = Toplevel():
            Label(top, text = "Amount").grid(row = 0, column = 0)
           global withdraw_amount
           withdraw_amount = IntVar()
           Entry(top, textvariable = withdraw_amount).grid(row = 1, column = 0)
           Button(top, text = withdraw , command = withdrawal).grid(row = 1, column = 1)