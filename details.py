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
