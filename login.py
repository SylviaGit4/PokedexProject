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
        #command = lambda: user_login(username_entry.get(), password_entry.get()),
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