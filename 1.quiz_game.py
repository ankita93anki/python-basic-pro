print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play  :)")
score = 0
answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print('correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stands for?")
if answer.lower() == "graphics processing unit":
    print('correct!')
    score += 1

else:
    print("Incorrect!")


answer = input("What does ALU stands for?")
if answer.lower() == "arithmatic logic unit":
    print('correct!')
    score += 1

else:
    print("Incorrect!")


answer = input("What does MU stands for?")
if answer.lower() == "memory unit":
    print('correct!')
    score += 1

else:
    print("Incorrect!")

print("you got " + str(score) + "question correct!")
print("You got " +  str((score/4)*100)+ "%")
