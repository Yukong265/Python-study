def add(a, b):
    return a + b

def devide(a, b):
    return a / b

def multiple(a, b):
    return a * b

def sub(a, b):
    return a - b

def calc():
    result = 0
    while True:
        string = (yield result)
        a = string.split(' ')
        func = add
        for i, b in enumerate(a):
            if (i % 2) == 0:
                result = func(result, int(b))
            else:
                if b is '+':
                    func = add
                elif b is '-':
                    func = sub
                elif b is '*':
                    func = multiple
                else:
                    func = devide

expressions = input().split(', ')
c = calc()
next(c)
 
for e in expressions:
    print(c.send(e))
 
c.close()
