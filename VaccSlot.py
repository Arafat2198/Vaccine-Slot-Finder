import requests
import json
from datetime import date
import winsound
import webbrowser
import time

# Function to Display the Details of the Available Slots
def getDetails(data,center_id):
    if data["centers"]:
        for x in range(len(data["centers"])):
            if(data["centers"][x]["center_id"] in center_id):
                print("\nxxxxxxxxxxxxxxxxxxxxx")
                print("Vaccine Center: "+data["centers"][x]["name"])
                print("Address: "+data["centers"][x]["address"])
                print("Pincode: "+str(pin))
                print("Vaccine Type: "+data["centers"][x]["fee_type"])
                if(len(data["centers"][x]["sessions"]) == 0):
                    print("No Vaccine Avaliable!")
                else:
                    print("^^^^^^ Avaliable Dates  ^^^^^^")
                    sessions = data["centers"][x]["sessions"]
                    for y in range(len(sessions)):
                        if(data["centers"][x]["sessions"][y]['vaccine'] == vaccine and data["centers"][x]["sessions"][y]['available_capacity'] != 0):
                            print("Session"+str(y+1)+" Avaliable !!")
                            print("Vaccine Name: "+data["centers"][x]["sessions"][y]['vaccine'])
                            print("Date: "+data["centers"][x]["sessions"][y]['date'])
                            if(data["centers"][x]["sessions"][y]['min_age_limit'] == 45):
                            	print("Avaliable for Ages 45+")
                            else:
                            	print("Avaliable for Ages 18+")
                            print("Total Avaliable Doses: "+str(data["centers"][x]["sessions"][y]['available_capacity']))
                            print("Total Avaliable Dose 1: "+str(data["centers"][x]["sessions"][y]['available_capacity_dose1']))
                            print("Total Avaliable Dose 2: "+str(data["centers"][x]["sessions"][y]['available_capacity_dose2']))
                            for z in range(len(data["centers"][x]["sessions"][y]['slots'])):
                                print("Time Slot"+str(z+1)+" : "+data["centers"][x]["sessions"][y]['slots'][z])
                            print("\n")
                        else:
                            print("Session"+str(y+1)+" On "+data["centers"][x]["sessions"][y]['date']+" Filled !!")
    else:
        print("No Centers Avaliable :(")

# Function to check Vaccine Availability 
def checkVacc(pin,today,vaccine): 
    # The 2 Input Parameters required to fetch the JSON Data
    query = {'pincode':pin, 'date':today}
    data = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin', params=query)
    if(data.status_code == 200):
        # print("Successful Connection")
        pass
    elif(data.status_code == 400):
        print("Bad Request Correct Input parameter missing")
        exit()
    elif(data.status_code == 500):
        print("Internal Server Error")
        exit()

    data = data.json() # Converts the Data into JSON Readable Format
    flag = 0
    age1 = 0
    age2 = 0
    avaliable_center_id = list()   

    if data["centers"]:
        for x in range(len(data["centers"])):
            if(len(data["centers"][x]["sessions"]) == 0):
                pass
            else:
                sessions = data["centers"][x]["sessions"]
                for y in range(len(sessions)):
                    if(data["centers"][x]["sessions"][y]['vaccine'] == vaccine and data["centers"][x]["sessions"][y]['available_capacity'] != 0):
                        avaliable_center_id.append(data["centers"][x]["center_id"])
                        if(data["centers"][x]["sessions"][y]['min_age_limit'] == 45):
                            age1 = 45
                            flag = flag+1
                        if(data["centers"][x]["sessions"][y]['min_age_limit'] == 18):
                            age2 = 18
                            flag = flag+1
    if(flag==0):
        print("No Vaccine Avaliable!")
    else:
        if(age1 == 45):
            print("\n ###### Hurry Vaccine Bookings Avaliable for Ages 45+ !! ######")
        if(age2 == 18):
            print(" ###### Hurry Vaccine Bookings Avaliable for Ages 18+ !! ######")
        frequency = 2000  # Set Frequency To 2500 Hertz
        duration = 500  # Set Duration To 1000 ms == 1 second
        for i in range(3):
            winsound.Beep(frequency, duration)
            time.sleep(0.1)
    return data, avaliable_center_id

	

    
today = date.today()
today = today.strftime("%d-%m-%Y")
print("Today's date:", today)
pin = input("Enter the Pin Code: ")
print("Vaccines Avaliable: ")
print("  1)COVISHIELD")
print("  2)COVAXIN")
choice = input("Enter the Vaccine Type: ")
vaccine="COVISHIELD" if choice=="1" else "COVAXIN"
# Return the Vaccine Details and the Various Center ID that have Slots    
data, center_id = checkVacc(pin,today,vaccine) # checkVacc check for the avaliability of Vaccine 

# While Loop Runs Infinitely to Provide the Menu to the User   
while(1):
    print("\n\n      ######### What to do Next #########")
    print("1) Get More Details about the Avaliable Vaccines")
    print("2) Book the Vaccine Slot")
    print("3) Search for a new Pin Code")
    print("4) Exit")
    choice = input("Enter your choice: ")
    if(choice == "1"):
        getDetails(data,center_id)
    elif(choice == "2"):
        webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open("https://selfregistration.cowin.gov.in/")
    elif(choice == "3"):
        pin = input("Enter the Pin Code: ")
        print("Vaccines Avaliable: ")
        print("  1)COVISHIELD")
        print("  2)COVAXIN")
        choice = input("Enter the Vaccine Type: ")
        vaccine="COVISHIELD" if choice=="1" else "COVAXIN"
        data, center_id = checkVacc(pin,today,vaccine)
    elif(choice == "4"):
        break
    else:
        print("Invalid Input !!")