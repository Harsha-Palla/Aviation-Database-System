from aviation import aviation

def main():
    db=aviation()
    while True:
        print("******WELCOME*****")
        print()
        print("Press 1 To Insert New User")
        print("press 2 To Display All User")
        print("Press 3 To Delete A User")
        print("Press 4 To Update User")
        print("Press 5 To Enter User Luggage")
        print("Press 6 To Display User Luggage")
        print("Press 7 To Insert Flights")
        print("Press 8 To Display All Flights")
        print("Press 9 To Insert Flight Staff")
        print("Press 10 To Display Flight Staff")
        print("Press 11 To Update Flight Staff")
        print("Press 12 To Exit")
        print()
        try:
            choice=int(input())
            if(choice==1):
                #insert user
                cid=int(input("Enter Customer ID"))
                cfname=input("Enter Customer First Name")
                clname=input("Enter Customer Lirst Name")
                cusp=int(input("Enter Customer Phone Number"))
                cad=int(input("Enter Customer Aadhar Number"))
                fid=int(input("Enter Customer Flight ID"))
                db.insert_customer(cid,cfname,clname,cusp,cad,fid)
                pass
            elif (choice==2):
                #display user
                db.fetch_all()
                pass
            elif (choice==3):
                #delete user
                cid=int(input("Enter Customer ID"))
                db.delete_customer(cid)
                pass
            elif (choice==4):
                #update user
                cid=int(input("Enter Customer ID"))
                cfname=input("Enter Customer First Name")
                clname=input("Enter Customer Lirst Name")
                cusp=int(input("Enter Customer Phone Number"))
                cad=int(input("Enter Customer Aadhar Number"))
                fid=int(input("Enter Customer Flight ID"))
                db.update_customer(cid,cfname,clname,cusp,cad,fid)
                pass
            elif(choice==5):
                cid=int(input("Enter Customer ID"))
                check=int(input("Enter Number of Checked Luggage"))
                personal=int(input("Enter Number Of Personal Luggage"))
                db.insert_luggage(cid,check,personal)
                pass
            elif(choice==6):
                db.fetch_luggage()
                pass
            elif(choice==7):
                #insert flight
                fid=int(input("Enter Flight ID"))
                fname=input("Enter Flight First Name")
                dt=int(input("Departure Time"))
                f=input("Enter From Location")
                t=input("Enter To Location")
                db.insert_flights(fid,fname,dt,f,t)
                pass
            elif(choice==8):
                #display flight
                db.fetch_allflights()
                pass
            elif(choice==9):
                fid=int(input("Enter Flight ID"))
                staffone=input("Enter Staff Name")
                stwoname=input("Enter Staff Name")
                sthreename=input("Enter Staff Name")
                pilotone=input("Enter Pilot Name")
                pilottwo=input("Enter Pilot Name")
                db.insert_flightstaff(fid,staffone,stwoname,sthreename,pilotone,pilottwo)
                pass
            elif(choice==10):
                db.fetch_flightstaff()
            elif(choice==11):
                fid=int(input("Enter Flight ID"))
                soname=input("Enter Staff Name")
                stname=input("Enter Staff Name")
                sthname=input("Enter Staff Name")
                po=input("Enter Pilot Name")
                pt=input("Enter Pilot Name")
                db.update_flightstaff(fid,soname,stname,sthname,po,pt)
                pass
            elif choice==12:
                break
            else:
                print("Invalid Input Try Again")
        except Exception as e:
            print(e)
            print("Invalid Details Try Again")

if __name__=="__main__":
    main()
