import random

def main():
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
    return correcto, (str(numbers))[1:-1]
        
