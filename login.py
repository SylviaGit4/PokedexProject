import pandas as pd

########################
def user_login(username, password):
    data = pd.read_csv("users.csv")

    user_correct = False
    pass_correct = False

    if username not in data["Username"].values:
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

    if password not in data["Password"].values:
        print("Invalid Password, try again.")
    else:
        print("Valid Password")
        pass_correct = True

user_login("test","test")