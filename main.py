#A program to validate plate number of a car

##Requesting for plate number
plateNumber = input("Enter Plate Number")

#checking for valid plate number 

if ( len(plateNumber) == 6 or len(plateNumber) == 7 or len(plateNumber) == 8 ):
    
    #The requested plate number is valid and old
    if plateNumber[0:3].isalpha():

     print("This is an old plate number")

    #The requested plate number is valid and new 
    elif plateNumber[0:4].isalpha() or plateNumber[0:5].isalpha():

      print("This is a new plate number")

    else:

      print("Your plate number should start with 3 alphabets for old plate number and 4 or 5 alphabets for new plate number)

else:

#The requested plate number is invalid
    print("Plate Number is Invalid")


 
