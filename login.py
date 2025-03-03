import pandas as pd
import tkinter as tk

########################
def user_login():

    loginWindow = tk.Tk()
    loginWindow.title("Pokedex")
    loginWindow.geometry("480x680")

    user_id = ""
    
    def submit(username, password):

        df = pd.read_csv("users.csv")

        user_correct = False
        pass_correct = False

        print(df["Username"].tolist())

        print(username)

        if str(username) in df["Username"].tolist():
            print("Valid Username")
            user_correct = True
            selected_row = df.loc[df["Username"] == username]
            print(selected_row)

            if str(password) == selected_row.iloc[0,2] and user_correct == True:
                print("Valid Password")
                pass_correct = True

            user_id = selected_row.iloc[0,0]
        
        else:
            print("Invalid Username")

    def submit_start():
        submit(username_entry.get(), password_entry.get())

    username_entry = tk.Entry(loginWindow)
    username_entry.grid(row=0,column=1)

    password_entry = tk.Entry(loginWindow)
    password_entry.grid(row=1,column=1) 

    sub_btn=tk.Button(loginWindow,text = 'Submit', command = submit_start)
    sub_btn.grid(row=2,column=1)

    loginWindow.mainloop()

    return(user_id)

user_id = user_login()

print(user_id)
