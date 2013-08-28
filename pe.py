# Project Euler Algorithems
#!/usr/bin/python3
import time


def Euler1():
    numbers = [n for n in range(0, 1000) if n % 3 == 0 or n % 5 == 0]
    return sum(numbers)


def Euler2():
    firstSequ = [1, 2]
    for iii, ooo in enumerate(firstSequ):
        if (firstSequ[-1] + firstSequ[-2]) <= 4000000:
            firstSequ.append(firstSequ[-1] + firstSequ[-2])
    evens = [n for n in firstSequ if n % 2 == 0]
    return sum(evens)


def Euler3(n=600851475143):
    for i in range(2, 100000):
        while n % i == 0:
            n //= i
            print("Yay, %d is a factor, now we should test %d" % (i, n))
            if n == 1 or n == i:
                return i


def Euler4():
    return (max(x * y
                for x in range(100, 1000)
            for y in range(100, 1000)
                if str(x * y) == str(x * y)[::-1]))


def Euler5(step, lon):
    items = range(1, step)
    steps = range(2520, lon, 2520)
    good = []
    for x in steps:
        if all(x % y == 0 for y in items):
            good.append(x)
    return good


def Euler6():
    num = range(1, 101)
    natural = []
    for iii in num:
        natural.append(iii ** 2)
    return (sum(num) ** 2) - sum(natural)


def Euler7(n=10000000):
    candidates = list(range(n + 1))
    fin = int(n ** 0.5)
    for i in range(2, fin + 1):
        if not candidates[i]:
            continue
        candidates[2 * i::i] = [None] * (n // i - 1)
    return [i for i in candidates[2:] if i][:1001]
    # Not Solved


def product(list):
    p = 1
    for i in list:
        p *= int(i)
    return p


def Euler8():
    num = str(
        7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)
    x = []
    n = 0
    m = 5
    maxf = []
    while m < len(num) + 1:
        x.append(num[n:m])
        n += 1
        m += 1
    for iii in x:
        maxf.append(product(iii))
    return max(maxf)


def squr(var):
    """Find Square Root"""
    return var ** (1 / 2.0)


def Euler9(var=1000):
    solutions = [a * b * (1000 - b - a) for a in range(1, 501) for b in range(1, 501)
                 if a ** 2 + b ** 2 == (1000 - b - a) ** 2][0]
    return solutions

if __name__ == '__main__':
    start = time.clock()
    print (Euler9())
    print(str(round(time.clock() - start, 3)) + " seconds")
