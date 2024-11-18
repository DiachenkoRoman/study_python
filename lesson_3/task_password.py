#-------------------VARIABLES---------------------------

const_pass = "password123"

#---------------------LOGIC------------------------------

requested_pass = input("Enter your password: ")

if const_pass == requested_pass:
    print("You`re in")

else:
    print("Bad pass")