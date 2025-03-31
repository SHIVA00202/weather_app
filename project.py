import mysql.connector

mycon=mysql.connector.connect(host="localhost",user="root",passwd="QWE1245@#$qs",database="school_management_system")
mycur=mycon.cursor()
def staff():
    def insert():
        empno=int(input("ENTER ID NUMBER: "))
        empname=input("ENTER THE NAME OF STAFF: ")
        address=input("ENTER THE ADDRESS OF STAFF: ")
        city=input("ENTER THE CITY NAME: ")
        pin=int(input("ENTER PINCODE: "))
        state=input("ENTER THE NAME OF THE STATE: ")
        phone_no=int(input("ENTER PHONE NUMBER: "))
        mobile_no=int(input("ENTER MOBILE NUMBER: "))
        email=input("ENTER EMAIL ADDRESS: ")
        gender=input("ENTER GENDER: ")
        dob=str(input("ENTER DATE OF BIRTH: "))
        doj=str(input("ENTER DATE OF JOINING: "))
        dept=input("ENTER DEPARTMENT: ")
        nature_of_job=input("ENTER NATURE OF JOB: ")
        basic_pay=int(input("ENTER BASIC PAY : "))
        l=(empno,empname,address,city,pin,state,phone_no,mobile_no,email,gender,dob,doj,dept,nature_of_job,basic_pay)
        sql="insert into staff values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mycur.execute(sql,l)
        mycon.commit()
        print("SUCCESSFULLY INSERTED...")
    def display():
        while True:
            print('''
ENTER 1 FOR SEE YOUR RECORD 
ENTER 2 FOR SEE ALL RECORDS
ENTER 3 FOR EXIT
''')
            ch=int(input("ENTER YOUR CHOICE: "))
            for i in range(25):
                print("*",end="")
            if ch==1:
                print()
                a=int(input("ENTER ID NUMBER: "))
                print('''
''')
                sql="select * from staff"
                mycur.execute(sql)
                while True:
                    i=mycur.fetchone()
                    if a==i[0]:
                        print("ID NUMBER         :",i[0])
                        print("NAME              :",i[1])
                        print("ADDRESS           :",i[2])
                        print("CITY              :",i[3])
                        print("PINCODE           :",i[4])
                        print("STATE             :",i[5])
                        print("PHONE NUMBER      :",i[6])
                        print("MOBILE NUMBER     :",i[7])
                        print("EMAIL ADDRESS     :",i[8])
                        print("GENDER            :",i[9])
                        print("DATE OF BIRTH     :",i[10])
                        print("DATE OF JOINING   :",i[11])
                        print("DEPARTMENT        :",i[12])
                        print("NATURE OF JOB     :",i[13])
                        print("BASIC PAYMENT     :",i[14])
                        ch=int(input('''
+-----------------------+
|PRESS 1 FOR MAIN MANU  |
|PRESS 2 FOR STAFF MANU |
|PRESS ENTER TO EXIT    |
+-----------------------+

ENTER YOUR CHOICE: '''))
                        if ch==1:
                            menu()
                        elif ch==2:
                            staff()
                        else:
                            break
                    
            elif ch==2:
                 sql="select * from staff"
                 mycur.execute(sql)
                 row=mycur.fetchall()
                 for i in row:
                     print()
                     print("ID NUMBER         :",i[0])
                     print("NAME              :",i[1])
                     print("ADDRESS           :",i[2])
                     print("CITY              :",i[3])
                     print("PINCODE           :",i[4])
                     print("STATE             :",i[5])
                     print("PHONE NUMBER      :",i[6])
                     print("MOBILE NUMBER     :",i[7])
                     print("EMAIL ADDRESS     :",i[8])
                     print("GENDER            :",i[9])
                     print("DATE OF BIRTH     :",i[10])
                     print("DATE OF JOINING   :",i[11])
                     print("DEPARTMENT        :",i[12])
                     print("NATURE OF JOB     :",i[13])
                     print("BASIC PAYMENT     :",i[14])
                     for a in range(50):
                         print("_",end="")
                 print()
                 print("********HERE IS THE END********")
                 ch=int(input('''
+-----------------------+
|PRESS 1 FOR MAIN MANU  |
|PRESS 2 FOR STAFF MANU |
|PRESS 3 TO EXIT        |
+-----------------------+

ENTER YOUR CHOICE: '''))
                 if ch==1:
                     menu()
                 elif ch==2:
                     staff()
                 else:
                     break
            else:
                break
    def delete():
        idno=input("FOR DELETE, ENTER ID NUMBER: ")
        sql="delete from staff where empno=%s"
        l=(idno,)
        mycur.execute(sql,l)
        print("Data deleted successesfully!!!!!!!!!!!!")
        mycon.commit()
    while True:
        for i in range(50):
            print("*",end="")
        print('''
              STAFF MANU
        ENTER 1 FOR INSERT VALUES
        ENTER 2 FOR DISPLAY
        ENTER 3 FOR DELETE ANY VALUES
        ENTER 4 FOR EXIT''')
        for i in range(50):
            print("*",end="")
        choice=int(input('''
ENTER YOUR CHOICE: '''))
        if choice==1:
            insert()
        elif choice==2:
            display()
        elif choice==3:
            delete()
        else:
            break
     
def student():
    def insert():
        regno=int(input("ENTER ADMISSION NUMBER: "))
        rollno=int(input("ENTER ROLL NUMBER: "))
        Class=input("ENTER CLASS: ")
        name=input("ENTER NAME: ")
        fname=input("ENTER FATHER'S NAME: ")
        mname=input("ENTER MOTHER'S NAME: ")
        dob=input("ENTER DATE OF BIRTH: ")
        dor=input("ENTER DATE OF RESERTRETION: ")
        address=input("ENTER ADDRESS: ")
        city=input("ENTER CITY: ")
        state=input("ENTER STATE: ")
        pin=int(input("ENTER PINCODE: "))
        phone=int(input("ENTER PHONE NUMBER: "))
        l=(regno,rollno,Class,name,fname,mname,dob,dor,address,city,state,pin,phone)
        sql="insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mycur.execute(sql,l)
        mycon.commit()
    def display():
        while True:
            print('''
ENTER 1 FOR SEE YOUR RECORD 
ENTER 2 FOR SEE ALL RECORDS ''')
            ch=int(input("ENTER YOUR CHOICE: "))
            if ch==1:
                a=int(input("ENTER ID NUMBER: "))
                sql="select * from student"
                mycur.execute(sql)
    
                while True:
                    i=mycur.fetchone()
                    if a==i[0]:
                        print("ADMISSION NUMBER      :",i[0])
                        print("ROLL NUMBER           :",i[1])
                        print("CLASS                 :",i[2])
                        print("NAME                  :",i[3])
                        print("FATHER'S NAME         :",i[4])
                        print("MOTHER'S NAME         :",i[5])
                        print("DATE OF BIRTH         :",i[6])
                        print("DATE OF ADMISSION     :",i[7])
                        print("ADDRESS               :",i[8])
                        print("CITY                  :",i[9])
                        print("STATE                 :",i[10])
                        print("PIN                   :",i[11])
                        print("PHONE NUMBER          :",i[12])
                        ch=int(input('''
+-------------------------+
|PRESS 1 FOR MAIN MANU    |
|PRESS 2 FOR STUDENT MANU |
|PRESS 3 TO EXIT          |
+-------------------------+

ENTER YOUR CHOICE: '''))
                        if ch==1:
                            menu()
                        elif ch==2:
                            student()
                        else:
                            break
                        
            elif ch==2:
                 sql="select * from student"
                 mycur.execute(sql)
                 row=mycur.fetchall()
                 for i in row:  
                     print("ADMISSION NUMBER      :",i[0])
                     print("ROLL NUMBER           :",i[1])
                     print("CLASS                 :",i[2])
                     print("NAME                  :",i[3])
                     print("FATHER'S NAME         :",i[4])
                     print("MOTHER'S NAME         :",i[5])
                     print("DATE OF BIRTH         :",i[6])
                     print("DATE OF ADMISSION     :",i[7])
                     print("ADDRESS               :",i[8])
                     print("CITY                  :",i[9])
                     print("STATE                 :",i[10])
                     print("PIN                   :",i[11])
                     print("PHONE NUMBER          :",i[12])
                     for a in range(50):
                         print("_",end="")
                     print()
                 print("here is end")
                 ch=int(input('''
+-------------------------+
|PRESS 1 FOR MAIN MANU    |
|PRESS 2 FOR STUDENT MANU |
|PRESS 3 TO EXIT          |
+-------------------------+

ENTER YOUR CHOICE: '''))
                 if ch==1:
                     menu()
                 elif ch==2:
                     student()
                 else:
                     break
    def delete():
        idno=input("FOR DELETE, ENTER ADMISSION NUMBER: ")
        sql="delete from student where regno=%s"
        l=(idno,)
        mycur.execute(sql,l)
        print("Data deleted successesfully!!!!!!!!!!!!")
        mycon.commit()
    while True:
        for i in range(50):
            print("*",end="")
        print('''
              STUDENT MANU
        ENTER 1 FOR INSERT VALUES
        ENTER 2 FOR DISPLAY
        ENTER 3 FOR DELETE ANY VALUES
        ENTER 4 FOR EXIT''')
        for i in range(50):
            print("*",end="")
        choice=int(input('''
ENTER YOUR CHOICE: '''))
        if choice==1:
            insert()
        elif choice==2:
            display()
        elif choice==3:
            delete()
        else:
            break
def result():
    def insert():
        regno=int(input("ENTER ADMISSION NUMBER: "))
        Class=input("ENTER CLASS: ")
        max_marks=input("ENTER MAXIMUM MARKS: ")
        pass_marks=int(input("ENTER PASSING MARKS: "))
        marks_obt=input("ENTER MARKS OBTAIN: ")
        result=int(input("ENTER RESULT: "))
        l=(regno,Class,max_marks,pass_marks,marks_obt,result)
        sql="insert into result values(%s,%s,%s,%s,%s,%s)"
        mycur.execute(sql,l)
        mycon.commit()
    def display():
         while True:
            print('''
ENTER 1 FOR SEE YOUR RECORD 
ENTER 2 FOR SEE ALL RECORDS ''')
            ch=int(input("ENTER YOUR CHOICE: "))
            if ch==1:
                print()
                a=int(input("ENTER ID NUMBER: "))
                sql="select * from result"
                mycur.execute(sql)
                while True:
                    i=mycur.fetchone()
                    if a==i[0]:
                        print("ADMISSION NUMBER      :",i[0])
                        print("CLASS                 :",i[1])
                        print("ENTER MAXIMUM MARKS   :",i[2])
                        print("ENTER PASSING MARK    :",i[3])
                        print("ENTER MARKS OBTAIN    :",i[4])
                        print("ENTER RESULT          :",i[5])
                        ch=int(input('''
+-----------------------+
|PRESS 1 FOR MAIN MANU  |
|PRESS 2 FOR STAFF MANU |
|PRESS 3 TO EXIT        |
+-----------------------+

ENTER YOUR CHOICE: '''))
                        if ch==1:
                            menu()
                        elif ch==2:
                            result()
                        else:
                            break
            elif ch==2:
                 sql="select * from RESULT"
                 mycur.execute(sql)
                 row=mycur.fetchall()
                 for i in row:  
                     print("ADMISSION NUMBER      :",i[0])
                     print("CLASS                 :",i[1])
                     print("ENTER MAXIMUM MARKS   :",i[2])
                     print("ENTER PASSING MARK    :",i[3])
                     print("ENTER MARKS OBTAIN    :",i[4])
                     print("ENTER RESULT          :",i[5])
                     for a in range(50):
                         print("_",end="")
                     print()
                 print("here is end")
                 ch=int(input('''
+-----------------------+
|PRESS 1 FOR MAIN MANU  |
|PRESS 2 FOR STAFF MANU |
|PRESS 3 TO EXIT        |
+-----------------------+

ENTER YOUR CHOICE: '''))
                 if ch==1:
                     menu()
                 elif ch==2:
                     result()
                 else:
                     break
    def delete():
        idno=input("FOR DELETE, ENTER ID NUMBER: ")
        sql="delete from RESULT where regno=%s"
        l=(idno,)
        mycur.execute(sql,l)
        print("Data deleted successesfully!!!!!!!!!!!!")
        mycon.commit() 
    while True:
        for i in range(50):
            print("*",end="")
        print('''
              RESULT MANU
        ENTER 1 FOR INSERT VALUES
        ENTER 2 FOR DISPLAY
        ENTER 3 FOR DELETE ANY VALUES
        ENTER 4 FOR EXIT''')
        for i in range(50):
            print("*",end="")
        choice=int(input('''
ENTER YOUR CHOICE: '''))
        if choice==1:
            insert()
        elif choice==2:
            display()
        elif choice==3:
            delete()
        else:
            break
def menu():
    while True:
        print('''
        +--------------------------------------------------+          
        |                  MAIN MENU                       |
        |          ENTER 1 FOR RECORD OF STAFF             |
        |          ENTER 2 FOR RECORD OF STUDENT           |
        |          ENTER 3 FOR RECORD OF FEE               | 
        |          ENTER 4 FOR RECORD OF RESULT            |
        |          ENTER 5 FOR EXIT                        |
        +--------------------------------------------------+          
                  ''')
        choice=int(input("ENTER YOUR CHOICE: "))
        if choice==1:
            staff()
        elif choice==2:
            student()
        elif choice==3:
            print("FEATURE NOT AVAILABLE!!!")
        elif choice==4:
            result()
        else:
            break
            
print(menu())
