print("We are going to play a game. I want you to pick a number then do a series of calculations. I bet I know what the result of those calculations will be !")
answer = input("*you* This will be the answer. Select a number 10-49: ")
answer = int(answer)
play = input("*Player* Pick any number 50-99: ")
play = int(play)
factor = 99-answer
intermediate = (play+factor)-100
mod = int((play+factor)/100)
print("I said the answer was going to be ",answer, "and the calculation result is ",play-(mod+intermediate))

