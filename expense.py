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



def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on expense_report.csv
    f = open('./expense_report.csv', 'w') # Open the file in write mode
    f.write(infos['amount'] + "," + infos['label'] + "," + infos['spender'])
    f.close()
    print("Expense Added !")
    return True