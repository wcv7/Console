import datetime
import os
import sqlite3
cwd = os.getcwd()

class DB():
    global dbfile
    dbfile = os.path.join(cwd+r"\Users\Users.db")
    def Create():
        with sqlite3.connect(dbfile) as db:
            cursor = db.cursor()
            sql = """CREATE TABLE IF NOT EXISTS Users(
                user_id integer Primary Key,
                username text,
                password text);"""
            cursor.execute(sql)
    def Insert(user, passw):
        with sqlite3.connect(dbfile) as db:
            cursor = db.cursor()
            sql  = """INSERT INTO Users(
                username,
                password)
                Values(?,?);"""
            cursor.execute(sql, (user,passw))
    def GetUser(user):
        with sqlite3.connect(dbfile) as db:
            cursor = db.cursor()
            sql = """SELECT username FROM Users
                WHERE username = ?"""
            cursor.execute(sql, (user,))
            result = cursor.fetchone()
            if result == None:
                return False
            else:
                return True
    def GetPass(user):
        with sqlite3.connect(dbfile) as db:
            cursor = db.cursor()
            sql = """SELECT password FROM Users
                WHERE username = ?"""
            cursor.execute(sql, (user,))
            result = cursor.fetchone()
            return result[0]
    def Remove():
        with sqlite3.connect(dbfile) as db:
            cursor = db.cursor

class Console:
    def Commands():
        print(" commands - to see commands \n clear - To Clear The Screen \n create {filename} - To Create A File \n read {filename} - To Read A File \n echo - Echo's your text \n remove - To Remove A File \n edit - To Edit A File \n list - List The Files In Directory \n cd - To CD Into A Directory \n time - To Get Time \n date - To Get Date \n year - To Get Year \n exit - To Exit")
    def Create(path, filename):
        if "." in filename:
            file = os.path.join(path, filename)
            Check = os.path.exists(file)
            if Check != True:
                with open(file, "x") as f:
                    f.close()
            else:
                print("Error")
        elif "." not in filename:
            file = os.path.join(path, filename)
            Check = os.path.isdir(file)
            if Check != True:
                os.mkdir(file)
            else:
                print("File Already Exists")
        else:
            print("Error")
    def Remove(path, filename):
        if "." in filename:
            file = os.path.join(path, filename)
            Check = os.path.exists(file)
            if Check:
                user = input("Are You Sure You Want To Delete "+filename+" (Y/N): ")
                if user == "Y" or user == "":
                    os.remove(file)
                elif user == "N":
                    print("Cancelling...")
                else:
                    print("Error, Cancelling...")
            else:
                print("Error")
        elif "." not in filename:
            file = os.path.join(path, filename)
            Check = os.path.isdir(file)
            if Check == True:
                user = input("Are You Sure You Want To Delete "+filename+" (Y/N): ")
                if user == "Y" or user == "":
                    os.rmdir(file)
                elif user == "N":
                    print("Cancelling...")
                else:
                    print("Error, Cancelling...")
            else:
                print("File Doesnt Exist")
        else:
            print("Error")
    def Echo(text):
        print(text)
    def Read(path, filename):
        file = os.path.join(path, filename)
        Check = os.path.exists(file)
        if Check:
            user = input("Do You Want To Open Notepad (Y/N): ").upper()
            if user == "N":
                with open(file, "r") as f:
                    content = f.read()
                    print(content)
            elif user == "Y" or user == "":
                notepadcmd = "notepad.exe " + file
                os.system(notepadcmd)
            else:
                print("Error")
        else:
            print("File Does Not Exist!")
    def List(path):
        Check = os.path.isdir(path)
        if Check == True:
            print(os.listdir(path))
        else:
            print("Error")
    def Cd(path, folder):
        if folder == "..":
            return ""
        else:
            dir = os.path.join()
    def Clear():
        os.system("cls")
    def Edit(path, filename):
        try:
            file = os.path.join(path, filename)
            Check = os.path.exists(file)
            if Check:
                user = input("Do You Want To Open Notepad (Y/N): ")
                if user == "N":
                    with open(file, "r") as f:
                        content = f.read()
                        f.close()
                    if content == "":
                        print("File Has No Text")
                        text = input(file+": ")
                        with open(file, "w") as f:
                            f.write(text)
                            f.close()
                            Console.Read(path, filename)
                    elif content != "":
                        print("File Has Text Do You Still Want To Edit?")
                        user = input(cwd+"> (Y/N): ").upper()
                        if user == "Y" or user == "":
                            print("Start On Same Line?")
                            user = input(cwd+"> (Y/N): ").upper()
                            if user == "Y" or user == "":
                                with open(file, "a") as f:
                                    text = input(file+"> \n"+content+ "> ")
                                    f.write(" "+text)
                                    f.close()
                            elif user == "N":
                                with open(file, "a") as f:
                                    text = input(file+"> \n"+content+ "\n> ")
                                    f.write("\n"+text)
                                    f.close()
                            else:
                                print("Error")
                        elif user == "N":
                            print("Cancelling")
                        else:
                            print("Error")
                elif user == "Y" or user == "":
                    notepadcmd = "notepad.exe " + file
                    os.system(notepadcmd)
                else:
                    print("Error")
            else:
                print("File Does Not Exist")
        except:
            print("Fatal Error")
    def Time():
        print(datetime.time().strftime("%H:%M:%S"))
    def Date():
        print(datetime.date.today().strftime("%d-%m-%Y"))
    def Year():
        print(datetime.date.today().year)

def CreateData():
    try:
        print("Creating Data...")
        DataFolder = os.path.join(cwd + r"\Data")
        UserFolder = os.path.join(cwd + r"\Users")
        os.mkdir(DataFolder)
        os.mkdir(UserFolder)
        DB.Create()
    except:
        print("Failed to create files")

def AccountLogin(username):
    Users = os.path.join(cwd + r"\Users\Users.txt")
    for line in open(Users, "r").readlines():
        Login_Details = line.split(":")
        Login_Details[1] = Login_Details[1].strip()
        if username == Login_Details[0]:
            return Login_Details[1]

def FileChecker():
    DataFolder = os.path.join(cwd + r"\Data")
    UserFolder = os.path.join(cwd + r"\Users")
    D_Check = os.path.isdir(DataFolder)
    U_Check = os.path.isdir(UserFolder)
    if D_Check == True and U_Check == True:
        return True
    else:
        return False
       
def Main(username):
    path = os.path.join(cwd + r"\Data", username)
    PathExists = os.path.isdir(path)
    if PathExists == False:
        os.mkdir(path)
    Stop = False
    while Stop == False:
        try:
            user = input(cwd+">")
            user = user.split(" ")
            user[0] = user[0].upper()
            if user[0] == "READ":
                Console.Read(path, user[1])
            elif user[0] == "CREATE":
                Console.Create(path, user[1])
            elif user[0] == "EDIT":
                Console.Edit(path, user[1])
            elif user[0] == "LIST":
                if len(user) > 1:
                    folder = os.path.join(path, user[1])
                else:
                    folder = path
                print(folder)
                Console.List(folder)
            elif user[0] == "ECHO":
                Console.Echo(user[1])
            elif user[0] == "CD":
                path = Console.Cd(path, user[1])
            elif user[0] == "TIME":
                Console.Time()
            elif user[0] == "REMOVE":
                Console.Remove(path, user[1])
            elif user[0] == "CLEAR":
                Console.Clear()
            elif user[0] == "DATE":
                Console.Date()
            elif user[0] == "YEAR":
                Console.Year()
            elif user[0] == "COMMANDS":
                Console.Commands()
            elif user[0] == "EXIT":
                Stop = True
            elif user[0] == "":
                None
            else:
                print("No Command Found")
        except:
            print("Minor Error")

def Login():
    username = input("Enter your username: ")
    AccountCheck = DB.GetUser(username)
    if AccountCheck:
        Stop = False
        while Stop == False:
            password = input("Enter your password: ")
            savedpass = DB.GetPass(username)
            print(savedpass)
            if password == savedpass:
                print("Successfully Logged In!")
                Stop = True
                Main(username)
            elif password != savedpass:
                print("Wrong password!")
            else:
                print("Error")
    else:
        user = input("Wrong Username, Do You Want To Create An Accout (Y/N): ").upper()
        if user == "Y" or user == "":
            SignUp()
        elif user == "N":
            Login()
        else:
            print("Error")
            Login()

def SignUp():
    username = ""
    while len(username) < 3:
        print("Username too short")
        username = input("Enter a username: ")
    Check = DB.GetUser(username)
    Same = True
    if Check == True:
        print("Username already exists")
        SignUp()
    elif Check == False:
        while Same == True:
            password = input("Enter a password: ")
            confirm_pass = input("Confirm your password: ")
            if password == confirm_pass:
                Same = False
                DB.Insert(username, password)
                Login()
            else:
                print("Password incorrect")
    else:
        print("Error")

def Start():
    DB.Create()
    a = input("Do you have an account (Y/N): ").upper()
    Check = FileChecker()
    if Check == False:
        CreateData()
        Start()
    elif Check:
        if a == "N":
            SignUp()
        elif a == "Y" or a == "":
            Login()
        else:
            print("Error")
            Start()

Start()