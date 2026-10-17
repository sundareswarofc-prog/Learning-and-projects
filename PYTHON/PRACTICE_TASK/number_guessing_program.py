import random 

secrets=random.randint(1,100)
attempts=0
print(secrets)

while True:
   try:
      guess=int(input("Guess the number?"))
   except:
      print("enter  whole Number")
      continue
   attempts+=1

   if guess>secrets:
      print("The value is too high than the actual number")
   elif guess<secrets:
      print("The value is too low than the actual number")
   else:
      print(f"Correct! You got it in {attempts} attempts.")
      break
      