from PyInquirer import prompt
import csv

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

]

def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on expense_report.csv
    f = open('./expense_report.csv', 'a') # Open the file in write mode
    f.write(infos['amount'] + "," + infos['label'] + "," + get_users())
    f.write("\n") #else it appends directly to last line
    f.close()
    print("Expense Added !")
    return True

#get users to the cli when adding a new expense
def get_users():
    with open('./users.csv', 'r') as f:
        reader = csv.reader(f)
        users = []
        for row in reader:
            users.append(row[0])
    users_list = {
        "type":"list",
        "name":"users_list",
        "message":"New Expense - Spender: ",
        "choices": users
    }
    option = prompt(users_list)
    return option['users_list']