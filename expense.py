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
    {
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },

]

user_questions = [
    {
        "type":"input",
        "name":"user",
        "message":"New user - Name: ",
    },
]



def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on expense_report.csv
    f = open('./expense_report.csv', 'a') # Open the file in write mode
    f.write("\n") #else it appends directly to last line
    f.write(infos['amount'] + "," + infos['label'] + "," + infos['spender'])
    f.close()
    print("Expense Added !")
    return True

def new_user(*args):
    infos = prompt(user_questions)
    f = open('./users.csv', 'a') # Open the file in write mode
    f.write("\n") #else it appends directly to last line
    f.write(infos['user'])
    f.close()
    print("User Added !")
    return True