from http import client
import json
from posixpath import split
from turtle import update
import pymongo
from customer import Customer

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["bank_app"]
my_collection = db["customer_data"]


def add_new_customer(name=""):
    split_input = []
    if name:
        split_input.append(name)
    else:
        user_input = input("Enter CUSTOMER NAMES, PHONE NUMBER, GENDER and DATE OF BIRTH. \
        Then press enter.\n ")
    split_input = user_input.split(',')

    for i in range(len(split_input)):
        split_input[i] = split_input[i].strip()

    existing_customer = customer_exists(split_input[0])
    if customer_exists(split_input):
        print(f"{split_input[0]} already exists as a customer. \nThank you.")
        existing_customer.pop("_id")
        Customer_info = Customer(**existing_customer)
        return Customer_info

    else:
        new_customer = Customer(
            split_input[0], 
            split_input[1], 
            split_input[2], 
            split_input[3]
            )
        
        # data = json.dumps(new_customer.print())
        # save_data(data[1:-1])
        save_data(new_customer.print())

        print(f"New customer's full info is:\n {new_customer.print()}\n")
        #print(f"Only the account number: {new_customer.account_number}")
        return new_customer

def save_data(data):
    # with open("customer_data.txt", 'a') as customer_file:
    #     customer_file.write(data)
    #     customer_file.write('\n')
    my_collection.insert_one(data)

def customer_exists(customer_data):
    # return False
    # data = None
    # with open("customer_data.txt") as customer_file:
    #     data = customer_file.read()
    data = my_collection.find_one({'name': customer_data})
    if data:
        print(data)
        return data
    else:
        return None
#         name = data.find(customer_data[0])
#         dob = data.find(customer_data[-1])
#     if name != -1 and dob != -1:
#         return True
#     else:
#         return False

# def load_data():
#     with open("customer_data.txt") as f:
#         data = f.read()
#         ans = data.find("Ifec")
        
#         if ans == -1:
#             print("data not found")
#         else:
#             print("data found!")
        # new_data = data.split("\n")
        # for item in new_data:
        #     if item:

        #         print(item.split(","))
        #         print("Item is not empty.")
        # print(len(new_data))

def transfer(sender_name, receiver_name, receiver_account_number, receiver_bank, amount):
    customer = add_new_customer(sender_name)
    if customer:
        customer.balance = 1000000
        customer.send_money(receiver_name, receiver_account_number,receiver_bank, amount)

        update_filter = {"account_number": customer.account_number}
        update_value = {"$set": {"transactions": customer.transaction}}
        my_collection.update_one(update_filter, update_value)

        data = my_collection.find_one({"account_number": customer.account_number})
        print(data)

sender, receiver, account, bank, amount = "onyebuchi", "frank", 3452738956, "first Bank", 50000
transfer(sender, receiver, account, bank, amount)
#add_new_customer()
#load_data()
#