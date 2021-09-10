def calc():
    result = 0
    while True:
        string = (yield result)
        a = string.split(' ')
        if '+' in a[1]:
            result = int(a[0]) + int(a[2])
        elif '-' in a[1]:
            result = int(a[0]) - int(a[2])
        elif '*' in a[1]:
            result = int(a[0]) * int(a[2])
        elif '/' in a[1]:
            result = float(a[0]) / float(a[2])
        else:
            result = "연산자를 바르게 입력하여 주십시오"

expressions = input().split(', ')
c = calc()
next(c)
 
for e in expressions:
    print(c.send(e))
 
c.close()

# 사칙연산 코루틴 작성