from PyInquirer import prompt
import csv
    

def show_status(*args):
    with open('./expense_report.csv', 'r') as f:
        reader = csv.reader(f)
        users = []
        for row in reader:
            users.append(row[2])
    print(users)
    return users

    