def main():
    #Define Function
    def greet(name,time):
        print(f'Good {time_of_day} {name}, hope you are well!')

    #Ask User to enter name and time
    name = input ("Enter your name: ")
    time = int(input("Enter the time of day (as military time): "))

    #Process time
    if time >= 2000:
        time_of_day = "Night"
        
    elif time >= 1800:
        time_of_day = "Evening"
        
    elif time >= 1200:
        time_of_day = "Afternoon"

    elif time >= 0:
        time_of_day = "Morning"

    else:
        time_of_day = "Day"

    greet (name, time_of_day)

    #Asking the user if they'd like the program to loop
    #the .lower() attached on the end makes sure Yes/YES/YeS all return as yes
    restart=input("Do you want to start again?\n").lower()
    if restart == "yes":
        main()
    else:
        exit()
#Where the code starts
main ()
