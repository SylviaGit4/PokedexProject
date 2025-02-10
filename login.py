import pandas as pd

########################
def login(username, password):
    data = pd.read_csv("users.csv")

    user_name = username
    user_pass = password

    print(data)

login(1,2)