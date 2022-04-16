q1=input("Hello! Can I drive now?\n")
if q1=="yes":
  print("Great!")
  car=float(input("Thank you so much! I appreciate it!"))
else:
  print("NO?! Then why did you invite me here?")
print("\n")



q1=input("Hello this is GrubHub, did you place an order?\n")
if q1=="yes":
  print("Great!")
  food_cost=float(input("How much does it cost?"))
  people=float(input("how many people are paying the order?"))
  total=food_cost/people
  print("The total cost is: $",total)
else:
  print("NO?! So who is cooking?")
print("\n")



user= int(input("How many rolls do you want to play?"))
numero=int(input("Guess the number!"))
#New
import timeit 
import random
Score= 0
x = random.randint(1,6)
print(x)

if numero == x:
  result= + 6
else:
  result= -1
  print("your score is " + str(result))

#New
import timeit 