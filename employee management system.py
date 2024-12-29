# employee management system using python 

from os import system
import re
# importing mysql connector
import mysql.connector

#making database

con = mysql.connector.connect(host="localhost", user="root",password ="ajees2609",database ="ajeesdb")

#make a regular expression
# for validating an email
regax = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# for validating an phone number
pattern = re.compile("(0|91)?[7-9][0-9]{9}")


#Function to add _employ
def Add_Employ():
    print("{:>60}".format("-->> add employee Record<<--"))
    Id = input("Enter Employee ID: ")
    #checking if employee Id is exit or not
    if(check_employee_Id(Id) == True):
        print("employee ID already exists\nTry Again..")
        press = input("press any key to continue..")
        Add_Employ()
    Name = input("Enter Employee Nmae: ")
    #checking if employee name is exit or not
    if(check_employee_name(Name) == True):
        print("employee Name already exists\nTry Again..")
        press = input("press any key to continue..")
        Add_Employ()
    Email_Id = input("Enter Employee Email ID: ")
    if (re.fullmatch (regax,Email_Id)):
        print("Valid Email")
    else:
        print("Invalid Email")
        press = input("press Any key to continue..")
        Add_Employ()
    Phone_no = input("Enter Employee Phone no: ")
    if(pattern.match(Phone_no)):
        print("Valid Phone Number")
    else:
        print("Invalid Phone Number")
        press = input("press Any key to continue..")
        Add_Employ()
    Address = input("Enter Employee Address: ")
    Post = input("Enter Employee Post: ")
    Salary = input("Enter Employee Salary: ")
    data = (Id, Name, Email_Id,Phone_no,Address,Post,Salary)
    # Instering Employee Details in
    #the employee (empdata) table
    sql ='insert into attendance values(%s,%s,%s,%s,%s,%s,%s)'
    c = con.cursor()

    #Executing the sql Query
    c.execute(sql,data)

    #commit() method to make change in the table 
    con.commit()
    print("Successfully Added Employee Record")
    press = input("press any key to continue..")
    menu()

# function to check if employee with
# given name exit or not

def check_employee_name(employee_name):
    #query to select all rows from
    #employee(empdata) table
    sql = 'select * from attendance where name =%s'

    #making cursor buffered to make
    #rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_name,)

    #Execute the sql query
    c.execute(sql, data)

    #rowcount method to find number
    #of rowa with given values
    r = c.rowcount 
    if r ==1:
        return True
    else:
        return False

# function to check if employee with
# given Id exit or not

def check_employee_Id(employee_Id):
    #query to select all rows from
    #employee(empdata) table
    sql = 'select * from attendance where Id =%s'

    #making cursor buffered to make
    #rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_Id,)

    #Execute the sql query
    c.execute(sql, data)

    #rowcount method to find number
    #of rowa with given values
    r = c.rowcount 
    if r ==1:
        return True
    else:
        return False
    
# Function to Display_Employ
def Display_Employ():
    print("{:>60}".format("-->Display Employee Record<<--"))
    #query to select all rows from Employee (empdata) table
    sql ='select * from attendance'
    c = con.cursor()

    #Executing the sql query
    c.execute(sql)

    #Fetching all details of all the Employees
    r = c.fetchall()
    for i in r:
        print("Employee Id: ",i[0])
        print("Employee Name: ",i[1])
        print("Employee Email Id: ",i[2])
        print("Employee Phone No: ",i[3])
        print("Employee Address: ",i[4])
        print("Employee post: ",i[5])
        print("Employee Salery: ",i[6])
        print("\n")
    press = input("Press Any key To Continue.. ")
    menu()

# Function to update_Employ
def Update_Employ():
    print("{:>60}".format("-->>update Employee Record<<--"))
    Id = input("Enter Employee ID: ")
    #checking if employee Id is exit or not
    if(check_employee_Id(Id) == False):
        print("employee ID already exists\nTry Again..")
        press = input("press any key to continue..")
        menu()
    else:
        Email_Id = input("Enter Employee  Email ID: ")
        if(re.fullmatch(regax,Email_Id)):
            print("Valid Email")
        else:
            print("Invalid Email")
            press = input("press Any key to continue..")
            Update_Employ()
            return
        Phone_no = input("Enter Employee Phone no: ")
        if(pattern.match(Phone_no)):
            print("Valid Phone Number")
        else:
            print("Invalid Phone Number")
            press = input("press Any key to continue..")
            Update_Employ()    
        Address = input("Enter Employee Address: ")
        #updating Employee details in the empdata table 
        sql = 'UPDATE attendance set Email_Id = %s , Phone_no = %s ,Address = %s  WHERE Id = %s'
        data =(Email_Id,Phone_no,Address,Id,)
    try: 
        c =con.cursor()

        #Executing the sql query
        c.execute(sql, data,)

        #commit() method to make changes in the table 
        con.commit()
        print("Update Employee Record")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        press = input("press Any key To Continue..")
        menu()
#function to promote_Employ
def promote_Employ():
    print("{:>60}".format("-->>promote Employee Record<<--"))
    Id = input("Enter Employee ID: ")
    #checking if employee Id is exit or not
    if(check_employee_Id(Id) == False):
        print("employee ID already exists\nTry Again..")
        press = input("press any key to continue..")
        menu()
    else:
        Amount = int(input("Enter Increase salary: "))
        #query to fetch salary of Empluyee with given data
        sql = 'select * from attendance where Id = %s'
        data = (Id,)
        c = con.cursor()

        #executing the sql query
        c.execute(sql,data)

        #fetching salary of employee with given Id
        r = c.fetchone()
        t = r[0]+Amount

        #query to update salary of employee with given id
        sql = 'update attendance set salary = %s where Id = %s'
        d = (t,Id)

        #executing the sql query
        c.execute(sql, d)

        #commit() method to make changes in the table 
        con.commit()
        print("Employee Promoted")
        press = input("Press Any key To Continue.. ")
        menu()

#Function to Remove_Employ
def Remove_Employ():
    print("{:>60}".format("-->>Remove Employee Record<<--"))
    Id = input("Enter Employee ID: ")
    #checking if employee Id is exit or not
    if(check_employee_Id(Id) == False):
        print("employee ID already exists\nTry Again..")
        press = input("press any key to continue..")
        menu()
    else:
        #query to delete Employee from empdata table
        sql = 'delete from attendance where id =%s'
        data =(Id,)
        c = con.cursor()

        #executing  the sql query
        c.execute(sql, data)

        #commit() method  to make changes in the empdata table
        con.commit()
        print("employee Removed")
        press = input("Press Any key To Continue.. ")
        menu()

# Function to Search_Employ
def Search_Employ():
    print("{:>60}".format("-->>Search Employee Record<<--"))
    Id = input("Enter Employee ID: ")
    #checking if employee Id is exit or not
    if(check_employee_Id(Id) == False):
        print("employee ID already exists\nTry Again..")
        press = input("press any key to continue..")
        menu()
    else:
        #query to Search Employee from empdata table
        sql ='select * from attendance where Id = %s'
        data = (Id,)
        c = con.cursor()

        #executing the sql query
        c.execute(sql, data)

        #fetching all datails of all the employee 
        r = c.fetchall()
        for i in r:
            print("Employee Id: ",i[0])
            print("Employee Name: ",i[1])
            print("Employee Email Id: ",i[2])
            print("Employee Phone No: ",i[3])
            print("Employee Address: ",i[4])
            print("Employee post: ",i[5])
            print("Employee Salery: ",i[6])
            print("\n")
    press = input("Press Any key To Continue.. ")
    menu()    

#menu function to display menu
def menu():
    system("cls")
    print("{:>60}".format("************************************"))
    print("{:>60}".format("-->> employee management system <<--"))
    print("{:>60}".format("************************************"))
    print("1. Add Employee")
    print("2. Display Employee Record")
    print("3. Update Employee Record")
    print("4. Promote Employee Record")
    print("5. Remove Employee Record")
    print("6. Search Employee Record")
    print("7. Exit\n")
    print("{:>60}".format("-->> Choice Option : [1/2/3/4/5/6/7] <<--"))

    ch = int(input("enter your choice: "))
    if ch == 1:
        system("cls")
        Add_Employ()
    elif ch == 2:
        system("cls")
        Display_Employ()
    elif ch == 3:
        system("cls")
        Update_Employ()
    elif ch == 4:
        system("cls")
        promote_Employ()
    elif ch == 5:
        system("cls")
        Remove_Employ()
    elif ch == 5:
        system("cls")
        Search_Employ()
    elif ch == 7:
        system("clc")
        print("{:>60}".format("Have A NIce day :)"))
        exit(0)

    else:
        print("Invalid Choice!")
        press = input("Press Any key To Continue.. ")
        menu()
# Calling menu function
menu()
