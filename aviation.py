
import mysql.connector as connector

class aviation:
    def __init__(self):
        self.con=connector.connect(host='localhost',port='3306',user='root',password='harsha0510',database='aviation')
        query='create table if not exists customer(cus_id int PRIMARY KEY,cus_fname varchar(200),cus_lname varchar(200),phone_no int,aadhar_no int,flight_id int)'
        cur=self.con.cursor()
        cur.execute(query)
        print("Created")
        query2='create table if not exists flight(flight_ int,flight_name varchar(200),depature_time int,f_from varchar(200),f_to varchar(200))'
        cu2=self.con.cursor()
        cu2.execute(query2)
        print("flights created")
        query4='create table if not exists flightstaff(flight_ int,staff_one varchar(200),staff_two varchar(200),staff_three varchar(200),p_one varchar(200),p_two varchar(200))'
        cur4=self.con.cursor()
        cur4.execute(query4)
        print("created")
        query5='create table if not exists laggage(cus_id int,checked int,personal int)'
        cur5=self.con.cursor()
        cur5.execute(query5)
        print("created")






    def insert_customer(self,cus_id,cus_fname,cus_lname,phone_no,aadhar_no,flight_id):
        query="insert into customer(cus_id,cus_fname,cus_lname,phone_no,aadhar_no,flight_) values({},'{}','{}',{},{},{})".format(cus_id,cus_fname,cus_lname,phone_no,aadhar_no,flight_id)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")

    def fetch_all(self):
        query="select * from customer"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Customer ID: ",row[0])
            print("First Name: ",row[1])
            print("Last Name: ",row[2])
            print("Phone number: ",row[3])
            print("Aadhar Card Number: ",row[4])
            print("Flight ID: ",row[5])
    
    def delete_customer(self,cus_id):
        query="delete from customer where cus_id={}".format(cus_id)
        print(query)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("deleted")

    def update_customer(self,cus_id,newf_name,newl_name,newphone_no,newaadhar_no,newflight_):
        query="update customer set cus_fname='{}',cus_lname='{}',phone_no={},aadhar_no={},flight_={} where cus_id={}".format(newf_name,newl_name,newphone_no,newaadhar_no,newflight_,cus_id)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")
    
    def fetch_allflights(self):
        query="select * from flight"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Flight ID: ",row[0])
            print("Flight Name: ",row[1])
            print("Departure: ",row[2])
            print("From: ",row[3])
            print("To: ",row[4])

    def insert_flights(self,flight_,flight_name,depature_time,f_from,f_to):
        query="insert into flight(flight_,flight_name,depature_time,f_from,f_to) values({},'{}',{},'{}','{}')".format(flight_,flight_name,depature_time,f_from,f_to)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("flight saved to db")
    


    def insert_flightstaff(self,flight_,staff_one,staff_two,staff_three,p_one,p_two):
        query="insert into flightstaff(flight_,staff_one,staff_two,staff_three,p_one,p_two) values({},'{}','{}','{}','{}','{}')".format(flight_,staff_one,staff_two,staff_three,p_one,p_two)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("staff saved to db")

    
    def update_flightstaff(self,flight_,staff_one,staff_two,staff_three,p_one,p_two):
        query="update flightstaff set staff_one='{}',staff_two='{}',staff_three='{}',p_one='{}',p_two='{}' where flight_={}".format(staff_one,staff_two,staff_three,p_one,p_two,flight_)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")

    def fetch_flightstaff(self):
        query="select * from flightstaff"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Flight ID: ",row[0])
            print("Staff One: ",row[1])
            print("Staff Two: ",row[2])
            print("Staff Three: ",row[3])
            print("Pilot One: ",row[4])
            print("Pilot Two: ",row[4])

    def insert_luggage(self,cus_id,checked,personal):
        query="insert into laggage(cus_id,checked,personal) values({},{},{})".format(cus_id,checked,personal)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user luggage saved to db")

    def fetch_luggage(self):
        query="select * from laggage"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Customer ID: ",row[0])
            print("No. of checked luggage: ",row[1])
            print("No. of personal luggage: ",row[2])

    

    

