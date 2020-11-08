
import mysql.connector
myConnnection =""
cursor=""

def MYSQLconnectionCheck ():
    myConnection=mysql.connector.connect(host="localhost",user="root",passwd="1234" )
    if myConnection:
        print("\n MYSQL IS CONNECTED SUCCESSFULLY !")
        cursor=myConnection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS school")
        cursor.execute("use school")
        cursor.close()
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION CHECK USERNAME AND PASSWORD !")

def MYSQLconnection ():
    global myConnection
    myConnection=mysql.connector.connect(host="localhost",user='root',passwd='1234' , database="school")
    if myConnection:
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")
    myConnection.close()

def newStudent():
    myConnection=mysql.connector.connect(host="localhost",user='root',passwd='1234' , database="school")
    if myConnection:
        cursor=myConnection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS STUDENT(SNAME VARCHAR(30),FNAME VARCHAR(30),MNAME VARCHAR(30) ,PHONE VARCHAR(12), ADDRESS VARCHAR(100),GRADE VARCHAR(5),SECTION VARCHAR(5),ROLL_NO VARCHAR(5),ADMISSION_NO VARCHAR(10) PRIMARY KEY)")
        sname=input("\n ENTER STUDENT'S NAME : ")
        fname=input(" ENTER FATHER'S NAME : ")
        mname=input(" ENTER MOTHER'S NAME : ")
        phone=input(" ENTER CONTACT NO. : ")
        address=input(" ENTER ADDRESS : ")
        grade=input(" ENTER CLASS : ")
        section=input(" ENTER SECTION : ")
        roll_no=input(" ENTER ROLL_NO : ")
        admission_no=input(" ENTER ADMISSION_NO : ")
        sql="INSERT INTO student(SNAME,FNAME,MNAME,PHONE,ADDRESS,GRADE,SECTION,ROLL_NO,ADMISSION_NO)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values=(sname,fname,mname,phone,address,grade,section,roll_no,admission_no)
        cursor.execute(sql,values)
        cursor.execute("COMMIT")
        cursor.close()
        print("\nNew Student Enrolled Successfully !")
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")

def displayStudent():
    cursor=myConnection.cursor()
    if myConnection:
        cursor.execute("select * from STUDENT")
        for i in cursor:
            v=list(i)
            k=['SNAME','FNAME','MNAME','PHONE','ADDRESS','GRADE','SECTION','ROLL_NO','ADMISSION_NO']
            print(dict(zip(k,v)))
        cursor.close()
    else:
        print("\nSomthing Went Wrong ,Please Try Again !")

def updateStudent():
    cursor=myConnection.cursor()
    if myConnection:
        admission_no=input("ENTER ADMISSION NO")
        sql="SELECT * FROM STUDENT WHERE ADMISSION_NO= %s"
        cursor.execute(sql,(admission_no,))
        data=cursor.fetchall()
        if data:
            print("PRESS 1 FOR NAME")
            print("PRESS 2 FOR CLASS")
            print("PRESS 3 FOR ROLL NO")
            choice=int(input("Enter Your Choice"))
            if choice==1:
                name=input("ENTER NAME OF THE STUDENT :")
                sql="UPDATE STUDENT SET SNAME= %s WHERE ADMISSION_NO =%s"
                cursor.execute(sql,(name,admission_no))
                cursor.execute("COMMIT")
                print("NAME UPDATED")
            elif choice == 2:
                std=input("ENTER CLASS OF THE STUDENT :")
                sql="UPDATE STUDENT SET CLASS= %s WHERE ADMISSION_NO=%s"
                cursor.execute(sql,(std,admission_no))
                cursor.execute("COMMIT")
                print("CLASS UPDATED")
            elif choice==3:
                roll_no=int(input("ENTER ROLL NO OF THE STUDENT :"))
                sql="UPDATE STUDENT SET ROLL_NO= %s WHERE ADMISSION_NO = %s"
                cursor.execute(sql,(roll_no,admission_no))
                cursor.execute("COMMIT")
                print("ROLL NO UPDATED")
            else:
                print("Record Not Found Try Again !")
                cursor.close()
        else:
            print("\nSomthing Went Wrong ,Please Try Again !")

def marksStudent() :
    if myConnection:
        cursor=myConnection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS MARKS(ADMISSION_NO VARCHAR(10) PRIMARY KEY,HINDI INT,ENGLISH INT ,MATH INT , SCIENCE INT,SOCIAL INT,COMPUTER INT,TOTAL INT)")
        admission_no=input("ENTER ADMISSION NO OF THE STUDENT :")
        hindi=int(input("\n ENTER MARKS OF HINDI : "))
        english=int(input("\n ENTER MARKS OF ENGLISH : "))
        math=int(input("\n ENTER MARKS OF MATH : "))
        science=int(input("\n ENTER MARKS OF SCIENCE : "))
        social=int(input("\n ENTER MARKS OF SOCIAL : "))
        computer =int(input("\n ENTER MARKS OF COMPUTER : "))
        total = hindi + english + math + science + social + computer
        sql="INSERT INTO MARKS(ADMISSION_NO,HINDI,ENGLISH,MATH,SCIENCE,SOCIAL,COMPUTER,TOTAL) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        values=(admission_no,hindi,english,math,science,social,computer , total)
        cursor.execute(sql,values)
        cursor.execute("COMMIT")
        cursor.close()
        print("\nMarks of the Student Entered Successfully !")
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")

def reportCardAllStudent () :
    cursor=myConnection.cursor()
    if myConnection:
        cursor.execute("SELECT * FROM MARKS")
        for i in cursor:
            v=list(i)
            k=['ADMISSION_NO','HINDI','ENGLISH','MATH','SCIENCE','SOCIAL','COMPUTER','TOTAL']
            print(dict(zip(k,v)))
        cursor.close()
    else:
        print("\nSomthing Went Wrong ,Please Try Again !")

def reportCardOneStudent():
    cursor=myConnection.cursor()
    if myConnection:
        admission_no=input("ENTER ADMISSION NO OF THE STUDENT :")
        cursor=myConnection.cursor()
        sql="SELECT * FROM MARKS WHERE ADMISSION_NO= %s"
        cursor.execute(sql,(admission_no,))
        for i in cursor:
            v=list(i)
            k=['ADMISSION_NO','HINDI','ENGLISH','MATH','SCIENCE','SOCIAL','COMPUTER','TOTAL']
            print(dict(zip(k,v)))
        cursor.close()
    else:
        print("\nSomthing Went Wrong ,Please Try Again !")

def feeStudent () :
    if myConnection:
        cursor=myConnection.cursor()
        createTable ="""CREATE TABLE IF NOT EXISTS FEES(ADMISSION_NO VARCHAR(10) PRIMARY KEY,MONTH INT ,TUTION_FEES INT,VVN INT,COMPUTER_FEES INT , MUSIC_FEES INT, TOTAL INT)"""
        cursor.execute(createTable)
        admission_no=input("ENTER ADMISSION NO OF THE STUDENT :")
        month=int(input("\n ENTER MONTH IN NUMERIC FORM (1-12) : "))
        tutionfee=int(input("\n ENTER TUTION FEES : "))
        vvn=int(input("\n ENTER VVN : "))
        computerfee=int(input("\n ENTER COMPUTER FEES : "))
        musicfee=int(input("\n ENTER MUSIC FEES : "))
        total = tutionfee + vvn + computerfee + musicfee
        sql="INSERT INTO FEES(ADMISSION_NO,MONTH,TUTION_FEES,VVN,COMPUTER_FEES,MUSIC_FEES,TOTAL) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        values=(admission_no,month,tutionfee,vvn,computerfee,musicfee,total)
        cursor.execute(sql,values)
        cursor.execute("COMMIT")
        cursor.close()
        print("\nFees of Student Accepted Successfully !")
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")

def feeReceiptAllStudent():
    cursor=myConnection.cursor()
    if myConnection:
        cursor.execute("SELECT * FROM FEES")
        for i in cursor:
            v=list(i)
            k=['ADMISSION_NO','MONTH','TUTION_FEES','VVN''COMPUTER_FEES','MUSIC_FEES','TOTAL']
            print(dict(zip(k,v)))
        cursor.close()
    else:
        print("\nSomthing Went Wrong ,Please Try Again !")

def feeReceiptOneStudent():
    cursor=myConnection.cursor()
    if myConnection:
        admission_no=input("ENTER ADMISSION NO OF THE STUDENT :")
        cursor=myConnection.cursor()
        sql="SELECT * FROM FEES WHERE ADMISSION_NO= %s"
        cursor.execute(sql,(admission_no,))
        for i in cursor:
            v=list(i)
            k=['ADMISSION_NO','MONTH','TUTION_FEES','VVN''COMPUTER_FEES','MUSIC_FEES','TOTAL']
            print(dict(zip(k,v)))
            cursor.close()
    else:
        print("\nSomthing Went Wrong ,Please Try Again !")


def transferStudent():
    cursor=myConnection.cursor()
    if myConnection:
        admission_no=input("ENTER ADMISSION NO OF THE STUDENT :")
        cursor=myConnection.cursor()
        sql="SELECT * FROM STUDENT WHERE ADMISSION_NO= %s"
        cursor.execute(sql,(admission_no,))
        data=cursor.fetchall()
        if data:
            sql=("DELETE FROM STUDENT WHERE ADMISSION_NO=%s")
            cursor.execute(sql,(admission_no,))
            cursor.execute("COMMIT")
            print("Student's Transfer Certificate Generated !!!")
        else:
            print("Record Not Found , Please Try Again !")
            cursor.close()
    else:
        print("\nSomthing Went Wrong ,Please Try Again !")


print("\n|********************SCHOOL MANAGER ***********************|")
myConnection = MYSQLconnectionCheck()
if myConnection:
        MYSQLconnection ()
        while(1):
          print("|-------------------------------------------------------------|")
          print("| Enter 1  - New Admission.                                   |")
          print("| Enter 2  - Display Student's Data.                          |")
          print("| Enter 3  - Update Students's Data.                          |")
          print("| Enter 4  - Issue Transfer Certififcate.                     |")
          print("| Enter 5  - Add Student's Marks Detail.                      |")
          print("| Enter 6  - Generate All Student's Report Card.              |")
          print("| Enter 7  - Generate Student Wise Report Card.               |")
          print("| Enter 8  - Pay Student's Fee.                               |")
          print("| Enter 9  - Generate Student Wise Fees Receipt.              |")
          print("| Enter 10 - Generate Student's Fee Receipt.                  |")
          print("| Enter 11 - Exit.                                            |")
          print("|-------------------------------------------------------------|")
          choice=int(input("PLEASE ENTER YOUR CHOICE : "))
          if choice==1:
              newStudent()
          elif choice==2:
              displayStudent()
          elif choice==3:
              updateStudent()
          elif choice==4:
             transferStudent()
          elif choice==5:
              marksStudent()
          elif choice==6:
              reportCardAllStudent()
          elif choice==7:
            reportCardOneStudent()
          elif choice==8:
              feeStudent()
          elif choice==9:
             feeReceiptAllStudent()
          elif choice==10:
             feeReceiptOneStudent()
          elif choice==11:
             myConnection.close()
             break
          else:
             print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
else:
        print("Check Your MYSQL Connection First !!! ")


