import pandas as pd
import tkinter as tk

########################
def user_login():
    loginWindow = tk.Toplevel()
    loginWindow.title("Login")
    loginWindow.geometry("200x100")

    loginWindow.columnconfigure(0, weight=1)
    loginWindow.columnconfigure(1, weight=1)
    loginWindow.columnconfigure(2, weight=1)
    
    def submit(username, password):

        global user_id

        df = pd.read_csv("users.csv")

        user_correct = False
        pass_correct = False

        if str(username) in df["Username"].tolist():
            print("Valid Username")
            user_correct = True
            selected_row = df.loc[df["Username"] == username]

            if str(password) == selected_row.iloc[0,2] and user_correct == True:
                print("Valid Password")
                pass_correct = True
                lbl_info.config(text="Username and Password Correct.")
                loginWindow.destroy()

            else:
                print("Invalid Password")
                pass_correct = False
                lbl_info.config(text="Invalid Password Input.")
        
        elif str(username) not in df["Username"].tolist():
            print("Invalid Username")
            lbl_info.config(text="Invalid Username Input.")
        
        else:
            print("Invalid Input Occured.")

        if user_correct == True and pass_correct == True:
            user_id = str(selected_row.iloc[0,0])

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
        command = lambda: submit(username_entry.get(), password_entry.get()),
        bg="indian red",
        fg="white",
    )

    lbl_info.grid(row=0,column=0, columnspan=3)
    lbl_username.grid(row=1,column=0)
    username_entry.grid(row=1,column=1, columnspan=2)
    lbl_password.grid(row=2,column=0)
    password_entry.grid(row=2,column=1, columnspan=2)
    sub_btn.grid(row=3,column=1)

    loginWindow.mainloop()

    return(user_id)