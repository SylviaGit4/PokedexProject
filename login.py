import pandas as pd
import tkinter as tk

########################

global user_id

def login_view():
    global user_id

    def user_login(username, password):
        global user_id

        user_data = pd.read_csv("users.csv")

        if str(username) in user_data["Username"].tolist():
            selected_row = user_data.loc[user_data["Username"] == username]
            print("Valid Username")

            if str(password) == selected_row.iloc[0,2]:
                print("Valid Password")

                user_id = selected_row.iloc[0,0]
                print(user_id)

                loginWindow.destroy()
                return(user_id)

                
            else:
                print("Error: Invalid password.")


        else:
            print("Error: Username not found or invalid.")

    def user_register(username, password):
        global user_id

        df = pd.read_csv("users.csv")
        
        user_id = (df.iloc[-1][0]) + 1

        new_user = {"UID":user_id,
                    "username":username, 
                    "password":password,
                    "poke1":"empty",
                    "poke2":"empty",
                    "poke3":"empty",
                    "poke4":"empty",
                    "poke5":"empty",
                    "poke6":"empty"
                    }

        new_row = pd.DataFrame([new_user])

        new_row.to_csv("users.csv", mode="a", header=False, index=False)

        loginWindow.destroy()
        return(user_id)

    loginWindow = tk.Tk()
    loginWindow.title("Login")

    loginWindow.columnconfigure(0, weight=1)
    loginWindow.columnconfigure(1, weight=1)
    loginWindow.columnconfigure(2, weight=1)

    frm_main = tk.Frame(
        loginWindow,
        bg="indian red",
        height=75,
        width=200,
        highlightbackground="grey27",
        highlightthickness=5,
    )
    frm_main.grid(row=0,column=1)

    lbl_info = tk.Label(
        master=frm_main,
        text="Please Log-in or register here.",
        bg="indian red",
        fg="white",
    )

    lbl_username = tk.Label(
        master=frm_main,
        text="Username:",
        bg="indian red",
        fg="white",
    )

    username_entry = tk.Entry(
        master=frm_main,
        bg="firebrick3",
        fg="white",
    )

    lbl_password = tk.Label(
        master=frm_main,
        text="Password:",
        bg="indian red",
        fg="white",
    )

    password_entry = tk.Entry(
        master=frm_main,
        bg="firebrick3",
        fg="white",
    )

    sub_btn=tk.Button(
        master=frm_main,
        text = 'Submit', 
        command = lambda: user_login(username_entry.get(), password_entry.get()),
        bg="indian red",
        fg="white",
    )

    reg_btn=tk.Button(
        master=frm_main,
        text = 'Register', 
        command = lambda: user_register(username_entry.get(), password_entry.get()),
        bg="indian red",
        fg="white",
    )

    lbl_info.grid(row=0,column=0, columnspan=3)
    lbl_username.grid(row=1,column=0)
    username_entry.grid(row=1,column=1, columnspan=2)
    lbl_password.grid(row=2,column=0)
    password_entry.grid(row=2,column=1, columnspan=2)
    sub_btn.grid(row=3,column=1, pady=2)
    reg_btn.grid(row=3,column=2, pady=2)

    loginWindow.mainloop()

    return(user_id)


def user_options(user_id):
    def change_username(user_id, new_username):
        df = pd.read_csv("users.csv")

        df.loc[df["UID"] == user_id, "Username"] = new_username

        df.to_csv("users.csv", index=False)

        lbl_info2.config(text="Username Changed")
    
    def delete_account(user_id):
        df = pd.read_csv("users.csv")

        df = df[df["UID"] != user_id]

        df.to_csv("users.csv", index=False)

        lbl_info2.config(text="Account Deleted.")


    OptionWindow = tk.Tk()
    OptionWindow.title("Option")

    OptionWindow.columnconfigure(0, weight=1)
    OptionWindow.columnconfigure(1, weight=1)
    OptionWindow.columnconfigure(2, weight=1)

    frm_main = tk.Frame(
        OptionWindow,
        bg="indian red",
        height=75,
        width=200,
        highlightbackground="grey27",
        highlightthickness=5,
    )
    frm_main.grid(row=0,column=1)

    btn_close = tk.Button(
        master=frm_main,
        text="Close",
        command=OptionWindow.destroy,
        bg="firebrick3",
        fg="white",
    )

    lbl_info = tk.Label(
        master=frm_main,
        text="Change your username or delete your account here.",
        bg="indian red",
        fg="white",
    )

    lbl_info2 = tk.Label(
        master=frm_main,
        text="",
        bg="indian red",
        fg="white",
    )

    lbl_username = tk.Label(
        master=frm_main,
        text="New Username:",
        bg="indian red",
        fg="white",
    )

    username_entry = tk.Entry(
        master=frm_main,
        bg="firebrick3",
        fg="white",
    )

    confirm_btn=tk.Button(
        master=frm_main,
        text = 'Submit', 
        command = lambda: change_username(user_id, username_entry.get()),
        bg="indian red",
        fg="white",
    )

    delete_btn=tk.Button(
        master=frm_main,
        text = 'Delete Account', 
        command = lambda: delete_account(user_id),
        bg="indian red",
        fg="white",
    )

    btn_close.grid(row=0, column=2, pady=2)
    lbl_info.grid(row=0,column=0, columnspan=2)
    lbl_info2.grid(row=2,column=0)
    lbl_username.grid(row=1,column=0)
    username_entry.grid(row=1,column=1)
    confirm_btn.grid(row=1,column=2, pady=2)
    delete_btn.grid(row=2,column=1, pady=2, columnspan=2)

    OptionWindow.mainloop()

