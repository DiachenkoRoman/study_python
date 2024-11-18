#--------------------VARIABLES---------------------

days_dict = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

#---------------------LOGIC-------------------------

requested_day = int(input("Enter the day number: "))

if requested_day > 0 and requested_day <= 7:
    print(days_dict[requested_day])

else: print("Error")