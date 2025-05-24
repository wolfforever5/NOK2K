import random

print('Welcome to the Brain Games!')
name = input('May I have your name?')
print("Hello", name + '!')
print('What number is missing in the progression?')

i = 0
while i < 3:
    numbers = []
    a = random.randint(2, 6)
    a1 = 0
    for j in range(random.randint(5, 10)):
        if j == 0:
            a1 = random.randint(1, 9)
            numbers.append(a1)
            a1 *= a
        else:
            numbers.append(a1)
            a1 *= a
    correctposition = random.randint(0, len(numbers) - 1)
    correcto = numbers[correctposition]
    numbers[correctposition] = ".."
    
    print("Question:", end= " ")
    print((str(numbers))[1:-1])
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
        
