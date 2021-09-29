# Author MEE 09/29/21

x = int(input(" How many points did the team score"))

if x >= 15:
    print("They won the gold!")
elif x >= 12:
    print("They won the silver!")
elif x < 9:
    print(" No Medal")
else:
    print(" They won bronze")
  
