import pandas as pd

########################
def user_login(username, password):
    df = pd.read_csv("users.csv")

    user_correct = False
    pass_correct = False

    if username not in df["Username"].values:
        print("Invalid Username")
        while True:
            choice = input("Register a new account or try again [R/T]: ").upper()[0]
            if choice == "R":
                pass
            if choice == "T":
                break
            else:
                print("Invalid selection")
    else:
        print("Valid Username")
        user_correct = True

    if password not in df["Password"].values:
        print("Invalid Password, try again.")
    else:
        print("Valid Password")
        pass_correct = True

    selected_row = df.loc[df["Username"] == username]
    user_id = selected_row.iloc[0,0]
    
    if user_correct == True and pass_correct == True:
        return(True, user_id)

login, user_id = user_login("test","test")

print(user_id)