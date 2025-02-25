import pandas as pd

########################
def user_login():
    df = pd.read_csv("users.csv")

    user_correct = False
    pass_correct = False

    while user_correct == False:
        username = input("Username: ")
        if username not in df["Username"].values:
            print("Invalid Username")
        else:
            print("Valid Username")
            user_correct = True
    
    selected_row = df.loc[df["Username"] == username]
    
    while pass_correct == False:
        password = input("Password: ")
        if password != selected_row.iloc[0,2]:
            print("Invalid Password, try again.")
        else:
            print("Valid Password")
            pass_correct = True

    user_id = selected_row.iloc[0,0]
        
    return(user_id)

user_id = user_login()

print(user_id)