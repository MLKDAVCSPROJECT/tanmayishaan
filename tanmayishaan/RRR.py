print("===============CODER BANK================")
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='1234',database='BANK_MANAGEMENT')
def OpenAcc():
    n=input("Enter The Name: ")
    ac=input("Enter The Account No: ")
    db=input("Enter The Date of Birth: ")
    add=input("Enter The Address: ")
    cn=input("Enter The Contact Number: ")
    ob=int(input("Enter The Opening Balance: "))
    data1=(n,ac,db,add,cn,ob)
    data2=(n,ac,ob)
    sql1=('insert into account values (%s,%s,%s,%s,%s,%s)')
    sql2=('insert into amount values(%s,%s,%s)')
    x=mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit()
    print("Data Entered Successfully..")
    main()


def DepoAmo():
    amount=input("Enter the amount you want to deposit: ")
    ac = input("Enter The Account No: ")
    a=f"select balance from amount where AccNo='{ac}'"
    x=mydb.cursor()
    x.execute(a)
    result=x.fetchone()
    if result:
        t=int(result[0])+int(amount)
        sql=f"update amount set balance={t} where AccNo='{ac}'"
        print("Your new balance is",t)
        x.execute(sql)
        mydb.commit()
    else:
        print("No account found....")
    main()

def WithdrawAmount():
    amount = input("Enter the amount you want to withdraw: ")
    ac = input("Enter The Account No: ")
    a = f"select balance from amount where AccNo='{ac}'"
    x = mydb.cursor()
    x.execute(a)
    result = x.fetchone()
    if result:
        t = int(result[0]) -int(amount)
        sql = (f"update amount set balance={t} where AccNo='{ac}'")
        print("Your new balance is",t)
        x.execute(sql)
        mydb.commit()
        main()
    else:
        print("no such account found")

def BalEnq():
    ac=input("Enter the account no: ")
    a=f"select * from amount where AccNo='{ac}'"
    x=mydb.cursor()
    x.execute(a)
    result=x.fetchone()
    print("Balance for account",ac,'is :',result[-1])
    main()

def DisDetails():
    ac = input("Enter the account no: ")
    sql = f"select * from amount where AccNo='{ac}'"
    x = mydb.cursor()
    x.execute(sql )
    result = x.fetchone()
    for i in result:
        print(i)
    main()
def CloseAcc():
    ac = input("Enter the account no: ")
    sql=f"delete from account amount where AccNo='{ac}';"
    x=mydb.cursor()
    x.execute(sql)
    sql=f"delete from amount amount where AccNo='{ac}';"
    x.execute(sql)
    mydb.commit()
    print("Account deleted successfully")
    main()


def main():
    print('''
                1. OPEN NEW ACCOUNT
                2. DEPOSIT AMOUNT
                3. WITHDRAW AMOUNT
                4. BALANCE ENQUIRY
                5. DISPLAY CUSTOMER DETAIL
                6. CLOSE AN ACCOUNT''')
    choice =input("Enter The task you want to perform: ")
    if (choice=='1'):
        OpenAcc()
    elif (choice=='2'):
        DepoAmo()
    elif (choice=='3'):
        WithdrawAmount()
    elif (choice == '4'):
        BalEnq()
    elif (choice == '5'):
        DisDetails()
    elif (choice == '6'):
        CloseAcc()
    else:
        print("Invalid choice")
        main()
main()
