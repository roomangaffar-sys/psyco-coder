balance_record = []  

def check_balance(customer_id):
    for record in balance_record:
        if record[0] == customer_id:
            return record[1]
    return 0


def deposit(customer_id, amount):
    for record in balance_record:
        if record[0] == customer_id:
            record[1] += amount
            return
    balance_record.append([customer_id, amount])


def withdraw(customer_id, amount):
    for record in balance_record:
        if record[0] == customer_id:
            if record[1] >= amount:
                record[1] -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient balance.")
            return
    print("No balance record found.")