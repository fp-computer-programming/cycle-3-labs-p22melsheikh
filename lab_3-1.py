# Author MEE 09/29/21

x = int(input(" How many points did the team score"))

if x >= 15:
    print("They won the gold!")
else:
    if x >= 12:
        print("They won the silver!")
    else:
        if x < 9:
            print("No medal for you")
        else:
            print(" they won bronze") 
