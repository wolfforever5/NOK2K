import random

def gcd(a, b):
    max = 1
    if a > b:
        for i in range(2, a):
            if a % i == 0 and b % i == 0:
                max = i
    else:
        for i in range(2, b):
            if a % i == 0 and b % i == 0:
                max = i
    return max



def lcm(a, b):
    return (abs((a * b))/gcd(a, b))


print('Welcome to the Brain Games!')
name = input('May I have your name?')
print("Hello", name + '!')
print('Find the smallest common multiple of given numbers.')
i = 0
while i < 3:
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    correcto = int(lcm(a, b))
    print("Question:", a, b)
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