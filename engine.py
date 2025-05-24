import random
import lcm
import geometprog

choice = 0
print('Welcome to the Brain Games!')
name = input('May I have your name?')
print("Hello", name + '!')
while choice != 1 or choice != 2:
    choice = int(input("Choose 1 for smallest common multiple or 2 for progression:"))
    if choice == 1 or choice == 2:
        break
    else:
        print("Incorrect input, try again.")

i = 0
while i < 3:
    if choice == 1:
        data = lcm.main()
        print('Find the smallest common multiple of given numbers.')
    elif choice == 2:
        data = geometprog.main()
        print('What number is missing in the progression?')
    correcto = data[0]
    print("Question:", data[1])
    ans = int(input())
    print("Your answer:", ans)
    if ans == correcto:
        print("Correct!")
        i += 1
    else:
        print("'" + str(ans) + "'", "is wrong answer ;(. Correct answer was '" + str(correcto) + "'.")
        print("Let's try again", name + "!")
        i = 0
        
if i == 3:
    print("Congratulations,", name + "!")