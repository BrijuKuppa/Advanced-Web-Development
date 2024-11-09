<<<<<<< HEAD
import mysql.connector
from tabulate import tabulate

# con = mysql.connector.connect(host="bpgfgctbrm9rowvrggxd-mysql.services.clever-cloud.com",
#                               user="uwpf2q04p4q5xodv",
#                               password="VLoXSieQ0qbxO20LppUm",
#                               database="bpgfgctbrm9rowvrggxd")

con = mysql.connector.connect(host="localhost",
                              user="root",
                              password="",
                              database="registers_infyni")

if con:
    print("Connected to Database\n")
else:
    print("Unable to connect to Database\n")

res = con.cursor()


def insert():
    print("\nYou chose to sign up. Enter the details below to create an account.\n")
    name=input("Enter your chosen Name here:")
    age=input("Enter your Age here:")
    email=input("Enter your Email here:")
    contact=input("Enter your Contact # here:")
    address=input("And finally, enter your location here:")
    sql="INSERT INTO registers_infyni (Name, Age, Email, Contact, Address)VALUES(%s, %s, %s, %s, %s)"
    res.execute(sql,(name,age,email,contact,address))
    print("Thank you for signing up to Infyni! Returning to menu...\n\n")

    con.commit()

def select():
    print("\nYou chose to display the Accounts.\nHere are the accounts displayed in a table:\n")
    sql="SELECT * FROM registers_infyni"
    res.execute(sql)
    data=res.fetchall()
    print(tabulate(data,["ID","Name","Age","Email","Contact","Address"]))
    print("\nReturning to menu...\n")
    con.commit()

def update():
    print("\nYou chose to update your Account.\nChoose the detail youi want to update.\n---\n1. Name\n2. Age\n3. Email\n4. Contact #\n5. Address\n---\n")
    choice=int(input("Enter your choice here:"))\

    if choice==1:
        print("\nYou chose to update your Name. Please fill out the fields appearing below.")
        id=int(input("\nPut your ID here:"))
        name=input("\nPut your new Name here:")
        sql="UPDATE registers_infyni SET Name=%s WHERE ID=%s"
        res.execute(sql,(name,id))
        print("\nWe have updated your account (if you want to see your account, go to 'Display the Accounts'). Returning to menu...\n")
        con.commit()

    elif choice==2:
        print("\nYou chose to update your Age. Please fill out the fields appearing below.")
        id=int(input("\nPut your ID here:"))
        age=input("\nPut your new Age here:")
        sql="UPDATE registers_infyni SET Age=%s WHERE ID=%s"
        res.execute(sql,(age,id))
        print("\nWe have updated your account (if you want to see your account, go to 'Display the Accounts'). Returning to menu...\n")
        con.commit()

    elif choice==3:
        print("\nYou chose to update your Email. Please fill out the fields appearing below.")
        id=int(input("\nPut your ID here:"))
        email=input("\nPut your new Email here:")
        sql="UPDATE registers_infyni SET Email=%s WHERE ID=%s"
        res.execute(sql,(email,id))
        print("\nWe have updated your account (if you want to see your account, go to 'Display the Accounts'). Returning to menu...\n")
        con.commit()

    elif choice==4:
        print("\nYou chose to update your Contact. Please fill out the fields appearing below.")
        id=int(input("\nPut your ID here:"))
        contact=input("\nPut your new Contact here:")
        sql="UPDATE registers_infyni SET Contact=%s WHERE ID=%s"
        res.execute(sql,(contact,id))
        print("\nWe have updated your account (if you want to see your account, go to 'Display the Accounts'). Returning to menu...\n")
        con.commit()

    elif choice==5:
        print("\nYou chose to update your Address. Please fill out the fields appearing below.")
        id=int(input("\nPut your ID here:"))
        location=input("\nPut your new Address here:")
        sql="UPDATE registers_infyni SET Address=%s WHERE ID=%s"
        res.execute(sql,(location,id))
        print("\nWe have updated your account (if you want to see your account, go to 'Display the Accounts'). Returning to menu...\n")
        con.commit()

def delete():
    print("\nYou chose to delete your Account. Please fill out your ID to delete your account.")
    id=int(input("\nPlease enter your ID here:"))
    sql="DELETE FROM registers_infyni WHERE ID=%s"
    confirm=input("\nAre you sure you want to delete your account? (Type 'yes' or 'no'):")
    if confirm=="yes":
        res.execute(sql,(id,))
        print("\nWe have successfully deleted your account. Thank you for joining us. Returning to menu...\n")
        con.commit()
    else:
        print("\nYou chose not to delete your account. Thank you for staying with us! Returning to main menu...\n")
        con.commit()



while True:
    print("Welcome to Infyni!")
    print("Please choose one of the options below:")
    print("---------------------------------------------------")
    print("1. Sign Up\n2. Display the Accounts\n3. Update your Account\n4. Delete your Account\n5. Exit")
    print("---------------------------------------------------")
    choose=int(input("Enter your option here:"))

    if choose==1:
        insert()
    elif choose==2:
        select()
    elif choose==3:
        update()
    elif choose==4:
        delete()
    elif choose==5:
        print("\nThank you for choosing Infyni. Exiting...")
        break
    else:
        print("\nYour option was not valid. Please try again.\n")
        continue

=======
import mysql.connector
from tabulate import tabulate

# con = mysql.connector.connect(host="bpgfgctbrm9rowvrggxd-mysql.services.clever-cloud.com",
#                               user="uwpf2q04p4q5xodv",
#                               password="VLoXSieQ0qbxO20LppUm",
#                               database="bpgfgctbrm9rowvrggxd")

con = mysql.connector.connect(host="localhost",
                              user="root",
                              password="",
                              database="registers_infyni")

if con:
    print("Connected to Database\n")
else:
    print("Unable to connect to Database\n")

res = con.cursor()


def insert():
    print("\nYou chose to sign up. Enter the details below to create an account.")
    name=input("Enter your chosen Name here:")
    age=input("Enter your Age here:")
    email=input("Enter your Email here:")
    contact=input("Enter your Contact # here:")
    address=input("And finally, enter your location here:")
    sql="INSERT INTO registers_infyni (Name, Age, Email, Contact, Address)VALUES(%s, %s, %s, %s, %s)"
    res.execute(sql,(name,age,email,contact,address))
    print("Thank you for signing up to Infyni! Returning to menu...\n\n")

    con.commit()

def select():
    print("\nYou chose to display the Accounts.\nHere are the accounts displayed in a table:\n")
    sql="SELECT * FROM registers_infyni"
    res.execute(sql)
    data=res.fetchall()
    print(tabulate(data,["ID","Name","Age","Email","Contact","Address"]))
    print("\nReturning to menu...\n")
    con.commit()

def update():
    print("\nYou chose to update your Account.\nChoose the detail youi want to update.\n---\n1. Name\n2. Age\n3. Email\n4. Contact #\n5. Address\n---\n")
    choice=int(input("Enter your choice here:"))\

    if choice==1:
        print("\nYou chose to update your Name. Please fill out the fields appearing below.")
        id=int(input("\nPut your ID here:"))
        name=input("\nPut your new Name here:")
        sql="UPDATE registers_infyni SET Name=%s WHERE ID=%s"
        res.execute(sql,(name,id))
        print("\nWe have updated your account (if you want to see your account, go to 'Display the Accounts'). Returning to menu...\n")
        con.commit()

    elif choice==2:
        print("\nYou chose to update your Age. Please fill out the fields appearing below.")
        id=int(input("\nPut your ID here:"))
        age=input("\nPut your new Age here:")
        sql="UPDATE registers_infyni SET Age=%s WHERE ID=%s"
        res.execute(sql,(age,id))
        print("\nWe have updated your account (if you want to see your account, go to 'Display the Accounts'). Returning to menu...\n")
        con.commit()

    elif choice==3:
        print("\nYou chose to update your Email. Please fill out the fields appearing below.")
        id=int(input("\nPut your ID here:"))
        email=input("\nPut your new Email here:")
        sql="UPDATE registers_infyni SET Email=%s WHERE ID=%s"
        res.execute(sql,(email,id))
        print("\nWe have updated your account (if you want to see your account, go to 'Display the Accounts'). Returning to menu...\n")
        con.commit()

    elif choice==4:
        print("\nYou chose to update your Contact. Please fill out the fields appearing below.")
        id=int(input("\nPut your ID here:"))
        contact=input("\nPut your new Contact here:")
        sql="UPDATE registers_infyni SET Contact=%s WHERE ID=%s"
        res.execute(sql,(contact,id))
        print("\nWe have updated your account (if you want to see your account, go to 'Display the Accounts'). Returning to menu...\n")
        con.commit()

    elif choice==5:
        print("\nYou chose to update your Address. Please fill out the fields appearing below.")
        id=int(input("\nPut your ID here:"))
        location=input("\nPut your new Address here:")
        sql="UPDATE registers_infyni SET Address=%s WHERE ID=%s"
        res.execute(sql,(location,id))
        print("\nWe have updated your account (if you want to see your account, go to 'Display the Accounts'). Returning to menu...\n")
        con.commit()
def delete():
    print("\nYou chose to delete your Account. Please fill out your ID to delete your account.")
    id=int(input("\nPlease enter your ID here:"))
    sql="DELETE FROM registers_infyni WHERE ID=%s"
    confirm=input("\nAre you sure you want to delete your account? (Type 'yes' or 'no'):")
    if confirm=="yes":
        res.execute(sql,(id,))
        print("We have successfully deleted your account. Thank you for joining us. Returning to menu...\n")
        con.commit()
    else:
        print("You chose to delete your account. Thank you for staying with us! Returning to main menu...\n")
        con.commit()



while True:
    print("Welcome to Infyni!")
    print("Please choose one of the options below:")
    print("---------------------------------------------------")
    print("1. Sign Up\n2. Display the Accounts\n3. Update your Account\n4. Delete your Account\n5. Exit")
    print("---------------------------------------------------")
    choose=int(input("Enter your option here:"))

    if choose==1:
        insert()
    elif choose==2:
        select()
    elif choose==3:
        update()
    elif choose==4:
        delete()
    elif choose==5:
        print("Thank you for choosing Infyni. Exiting...")
        break
    else:
        print("Your option was not valid. Please try again.\n")
        continue

>>>>>>> origin/main
con.commit()