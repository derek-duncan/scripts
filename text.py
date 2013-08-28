def tC():
    print('%.1f' % ((5 / 9) * (choice - 32)))
def tF():
    print('%.1f' % ((9 / 5) * choice + 32))
def fail():
    return "Fail!"
choice = int(input("Please Enter a Temperature: "))
temp = input("Please Enter a Type Conversion.  (F)arenheit or (C)elcius: ")
values = {
    'F': tF,
    'C': tC
}
values.get(temp, fail())()
