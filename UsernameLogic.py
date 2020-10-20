while True:
    print("Please Create a username: ")
    username = input()
    if len(username) < 8:
        print("Please create a username that contains at least 8 characters")
    elif len(username) > 8:
        print("Username Created")
        break

while True:
    print("Please Create a Password: ")
    password = input()
    if len(password) < 16:
        print("Please create a stronger password that contains at least 16 characters")
    elif len(password) > 16:
        print("Password Created")
        break

print("Your Username and password have both been created.  Please login to Continue.")


