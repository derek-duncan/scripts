import os
import re
import pickle
from urllib.request import urlopen


def multiples():
    """
        The problem is to get the sum of multiples of 3 & 5 that are under 1000.
    """
    threes = [x * 3 for x in range(1000) if x * 3 < 1000]
    fives = [x * 5 for x in range(1000) if x * 5 < 1000]

    return (sum(threes) + sum(fives))


def fibo(start, end):
    st = [start, start + start]
    while not st[-1] >= end:
        x = st[-2:]
        st.append(sum(x))
        even = [i for i in st if i % 2 == 0]

    return even


def replaceL(string):
    string2 = "map"
    slist = list(string)
    for iii, lll in enumerate(slist):
        lil = [chr(x) for x in range(97, 123)]
        if lll in lil:
            x = 0
            it = ord(lll)
            while x < 2:
                if it <= 121:
                    it += 1
                else:
                    it = 96 + 1
                x += 1
            slist[iii] = chr(it)
        string = "".join(slist)
    return(string)


def replaceLLL():
    with open(os.path.join(os.path.dirname(__file__), 'encrypt.txt'), "r") as xxx:
        f = xxx.read()
        a = "".join(x for x in f if x.isalpha())
    return a


def findBodyGuards():
    with open(os.path.join(os.path.dirname(__file__), 'encrypt.txt'), "r") as xxx:
        f = xxx.read()
    m = re.findall(r'((?<=[a-z])[A-Z]{3}[a-z][A-Z]{3}(?=[a-z]))', f)
    sL = [n for x in m for n in x if not n.istitle()]
    return "".join(sL)


def findURL():
    key1 = 12345
    key = 16044 / 2
    while True:
        f = urlopen(
            'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % key)
        x = f.read().decode('utf-8')
        regex = re.findall(r'\b[0-9].*?\b', x)
        if bool(regex) is True:
            key = regex[-1]
            print (x, '\n', int(key) / 2)
        else:
            key = "".join(regex)
            print (x, '\n', key)
            break


def pronounceIt():
    obj = pickle.load(
        urlopen('http://www.pythonchallenge.com/pc/def/banner.p'))
    for line in obj:
        print(''.join(map(lambda x: x[0] * x[1], line)))


def zip(text):
    let = list(text)
    num = []
    for iii in let:
        num.append(str(ord(iii)))
    return ', '.join(num)

print(zip('zip'))
