vault_data = {"amna" : 1234,
              "ali" : 5673,
              "usman" : 12093,
              "asad" : 56714}
blocked_users = {"ahmed", "asad", "akram", "atif"}
def authentication_function(username, password):
    if username in blocked_users:
        raise PermissionError("Access Denied: Account Blocked")
    elif username in vault_data:
        if vault_data[username] == password:
            return "Access Granted"
        else:
            return "Incorrect Password"
    else:
        return "user not found"

while True:
    user_input = input("Enter your username or type exit to quit ").lower()
    if user_input == "exit":
        print("Shutting down the vault system")
        break
    try:
        pass_token = int(input("Enter pass token"))
        result = authentication_function(user_input, pass_token)
        print(f"status: {result}")
    except ValueError:
        print("password token must be a valid integer code")
    except PermissionError as e:
        print("Security alert {e}")




    