print("Welcome to the Quiz of Basic Computer !")
print("Rules for the  Quiz : ")
print("1.This is MCQ based TEST. \n2.Choose Right Option there is no turning back. \n3.Data Entry is not case sensitive. \n Be Your BEST !")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
score = 0
print("Choose a/b/c/d")

#Question 1
answer = input("Q1. What does the word Computer Means? \na.Calculate \nb.Control \nc.Calibrate \nd.Cancel\n")
if answer == "a":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT\n")

#Question 2
answer = input("Q2. Which is an Operating System from the Following? \na.Windows \nb.Linux \nc.MacOS \nd.All of these\n")
if answer == "d":
    print("CORRECT!")
    score += 1

else:
    print("INCORRECT\n")

#Question 3
answer = input("Q3. Which is an OS? \na.On System \nb.Operating System \nc.Off System \nd.None of these\n")
if answer == "b":
    print("CORRECT!")
    score += 1

else:
    print("INCORRECT\n")

#Question 4
answer = input("Q4. Who is father of Computer? \na.Adolf Hitler \nb.Donald Trump \nc.Charles Babbage \nd.Imran Khan\n")
if answer == "c":
    print("CORRECT!")
    score += 1

else:
    print("INCORRECT\n")

#Question 5
answer = input("Q5. Which is Brain of Computer? \na.CPU \nb.GPU \nc.MotherBoard \nd.Hard Drive\n")
if answer == "a":
    print("CORRECT!")
    score += 1

else:
    print("INCORRECT\n")

print("Your Score is " +  str(score) )