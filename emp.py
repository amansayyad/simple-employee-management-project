import mysql.connector 


class Database:                                                     #creating database
   def __init__(self):                                              #simple constructor
      self.con=mysql.connector.connect(host="localhost",user="root",password="12345678")       #we have made object of mysql connector 
      query='create database if not exists employee'                #we made query of database
      cur=self.con.cursor()                                         #for firing query 
      cur.execute(query)                                            #query executed
      print("\n***database created***")

h=Database()                                                      #object of class Database

      

class table:                                  #creating table 
   def __init__(self):
      self.con=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee")
      query='create table if not exists user(empID int(11) unsigned primary key not null,firstname varchar(200) not null,lastname varchar(200) not null,email varchar(200) not null)'
      cur=self.con.cursor()
      cur.execute(query)
      print("\n***table created***")

b=table()                                                         #object of class table


while True:                        # for infinit loop 

     print("\n1:adding new employee")
     print("\n2:update existing employee")
     print("\n3:delete existing employe")
     print("\n4:exit")
     choice=int(input("\nenter your choice=")) 


     if choice==1:                                                         #adding new employee

         con=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee") #for making connection from python to mysql
         cur=con.cursor()                                       #for creating cursor object,we want to call cursor function from connecion object
         empid=int(input("\nenter employee ID = "))
         
         firstname=input("\nenter first name of employee = ")
         lastname=input("\nenter last name of employee = ")
         email=input("\n enter email = ")
         query="insert into user values ({},'{}','{}','{}')".format(empid,firstname,lastname,email)
         cur.execute(query)                                                      #we have execute query here
         con.commit()                                                            #to commit changes3
         print("\n***inserted successfully***")



     elif choice==2:                                                            #update existing employee
         con=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee")

         cur=con.cursor()

         s=input("\nenter employee ID which you want to update=")

         print("\nwhich colum you want to update")
         print("\n1:empID     2:firstname\n\n3:lastname  4:email")
         choice=int(input("\nenter your choice="))

         if choice==1:                                                                #empID

            h=input("\nenter new employee ID=")
            query="update user set empID={} where empID='{}'".format(h,s)
            cur.execute(query)
            con.commit()
            print("\n***update successfully***") 

         elif choice==2:                                                            #first name

            f=input("\nenter first name=")
            query="update user set firstname='{}' where empID='{}'".format(f,s)
            cur.execute(query)
            con.commit()
            print("\n***update successfilly***")

         elif choice==3:                                                            #last name
            l=input("\nenter last name=")
            query="update user set lastname='{}' where empID='{}'".format(l,s)
            cur.execute(query)
            con.commit()
            print("\n***update successfilly***")

         elif choice==4:                                                            #email
            e=input("\nenter email=")
            query="update user set email='{}' where empID='{}'".format(e,s)
            cur.execute(query)
            con.commit()
            print("\n***update successfilly***")
            # break

         else:                                                                      #exit
            print("\n***invalid input***")

     elif choice==3:                                                         #delete existing employe
        con=mysql.connector.connect(host="localhost",user="root",password="12345678",database="employee")
        cur=con.cursor()
        u=input("\nenter employee id which you want to delete=")
        query="delete from user where empID='{}'".format(u)
        cur.execute(query)
        con.commit()
        print("\n***deleted successfully***")
     elif choice==4:
         break
     else:
         print("\n***invalid choice***")








            



#main
