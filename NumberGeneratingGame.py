  #  *********** NUMBER GENERATOR GAME // NUMBER GUESSING GAME ***********

number=88
count=1
nguess=0
t=0
while nguess != number:
   nguess=int(input("Enter a number between 1 and 100: \n"))
   if nguess>number:
     print("Lower Number Please \n")
   elif nguess<number:
     print("Higher Number Please \n")
   else:
      print("You Guessed in ",count, "attempts." )
   count+=1
t=count
if t<=10:
    print("You Win the Game !!!! ")
else:
    print("You Lose the Game !!!! ")





























