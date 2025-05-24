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

def main():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    correcto = int(lcm(a, b))
    stringoutput = str(a) + " " + str(b)
    return correcto, stringoutput