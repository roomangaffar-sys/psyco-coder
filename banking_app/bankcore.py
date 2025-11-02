branch_id = 2057
users_info = []  

def create_account(name, password):
    customer_id = f"{branch_id}-{len(users_info) + 1}"
    users_info.append([customer_id, name, password])
    print("Account created successfully!")
    print("Your customer ID is:", customer_id)
    return customer_id


def login(customer_id, password):
    for user in users_info:
        if user[0] == customer_id and user[2] == password:
            print("Login successful!")
            return True
    print("Invalid login.")
    return False