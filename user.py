from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"user",
        "message":"New user - Name: ",
    },
]

def add_user(*args):
    infos = prompt(user_questions)
    if (infos['user'] == "" or infos['user'] == " "):
        print("Mandatory user information : Name")
        add_user(*args)
        return False
    f = open('./users.csv', 'a') # Open the file in write mode
    f.write(infos['user'])
    f.write("\n") #else it appends directly to last line
    f.close()
    print("User Added !")
    return True