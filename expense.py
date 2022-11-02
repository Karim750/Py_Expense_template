from PyInquirer import prompt
import csv

#get users to the cli when adding a new expense
def get_users():
    with open('./users.csv', 'r') as f:
        reader = csv.reader(f)
        users = []
        for row in reader:
            users.append(row[0])
    return users

def get_consumers():
    with open('./users.csv', 'r') as f:
        reader = csv.reader(f)
        users = []
        for row in reader:
            users.append({'name': row[0]})
    return users

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"users_list",
        "message":"New Expense - Spender: ",
        "choices": get_users(),
    },
    {
        "type":"checkbox",
        "name":"consumers",
        "message":"New Expense - consumers: ",
        "choices": get_consumers(),
        'validate': lambda answer: 'You must choose at least one topping.' \
            if len(answer) == 0 else True
    },
    

]

def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on expense_report.csv
    f = open('./expense_report.csv', 'a') # Open the file in write mode
    f.write(infos['amount'] + "," + infos['label'] + "," + infos['users_list'])
    for consumer in infos['consumers']:
        if (consumer != infos['users_list']):
            f.write(" " + consumer)
    f.write("\n") #else it appends directly to last line
    f.close()
    print("Expense Added !")
    return True

