import json
from customer import Customer

def add_new_customer():
    user_input = input("Enter CUSTOMER NAMES, PHONE NUMBER, GENDER and DATE OF BIRTH. \
        Then press enter.\n ")
    split_input = user_input.split(',')

    for i in range(len(split_input)):
        split_input[i] = split_input[i].strip()

    if customer_exists(split_input):
        print(f"{split_input[0]} already exists as a customer. \nThank you.")
        return None
    else:
        new_customer = Customer(
            split_input[0], 
            split_input[1], 
            split_input[2], 
            split_input[3]
            )
        
        data = json.dumps(new_customer.print())
        save_data(data[1:-1])

        print(f"New customer's full info is:\n {new_customer.print()}\n")
        print(f"Only the account number: {new_customer.account_number}")
        return new_customer

def save_data(data):
    with open("customer_data.txt", 'a') as customer_file:
        customer_file.write(data)
        customer_file.write('\n')

def customer_exists(customer_data):
    return False
    data = None
    with open("customer_data.txt") as customer_file:
        data = customer_file.read()
        name = data.find(customer_data[0])
        dob = data.find(customer_data[-1])
    if name != -1 and dob != -1:
        return True
    else:
        return False

def load_data():
    with open("customer_data.txt") as f:
        data = f.read()
        ans = data.find("Ifec")
        
        if ans == -1:
            print("data not found")
        else:
            print("data found!")
        # new_data = data.split("\n")
        # for item in new_data:
        #     if item:

        #         print(item.split(","))
        #         print("Item is not empty.")
        # print(len(new_data))

def transfer():
    customer = add_new_customer()
    if customer:
        customer.balance = 1000000
        status = customer.send_money("Joe Biden", 234567890, "Bank of America", 20000)
        if status:
            print(f"Transaction successful. Balance for {customer.name} is {customer.balance}.")

#add_new_customer()
#load_data()
transfer()