from datetime import date



def get_expense_and_amount():
    """Receive an expense and amount and add to expenses list."""
    expense_list = {}
    item_id = 1
    while item_id < 10000:
        item_description = input("Enter your item description: Enter 'q' at any time to quit. ")
        if item_description != 'q':
            item_amount = (input("Enter your amount: $"))
            date_added = date.today().strftime(" %Y-%m-%d")
            expense_list[item_id] = str({item_description : "$"+ item_amount}) + date_added
            item_id += 1
        else:
            break
    return expense_list

def display_expense_list():
    """Display entire list of expense IDs with items and amount."""
    print(get_expense_and_amount())


display_expense_list()
    
