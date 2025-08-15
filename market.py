produce = {
    "mango" : {
        "price": 2500,
        "stock": 2
    },
    "orange": {
        "price": 2000,
        "stock": 0
    },
    "banana": {
        "price": 1500,
        "stock": 13
    }
}

shopping_list = ["mango", "banana", "pear", "orange"]

def calculate_bill(produce_items, customer_list):
    
    total_cost = 0
    
    for item in customer_list:
        if item in produce_items:
            if produce_items[item]["stock"] == 0:
                print(f"Sorry, {item} is currently out of stock")
            else:
                print(f"Adding {item} to the cart.")
                total_cost = total_cost + produce_items[item]["price"]
        else:
            print(f"Sorry, we are out of stock for {item}.")
    return total_cost

final_bill = calculate_bill(produce, shopping_list)

print(f"Your total bill is {final_bill}.")
        