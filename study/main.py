def add(a, b):
    return a + b # 더하기 함수

def devide(a, b):
    return a / b # 나누기 함수

def multiple(a, b):
    return a * b # 곱하기 함수

def sub(a, b):
    return a - b # 빼기 함수

def calc():
    result = 0
    while True:
        expressions = (yield result).split(' ') # expressions에 yield에 받아온 값을 split메서드로 리스트 형식으로 나누기
        result = 0
        oper = add # oper의 기본 값을 더하기로
        for i, e in enumerate(expressions): # enumerate로 반복문 횟수표시 i = 횟수, e = expressions의 값
            if (i % 2) == 0: # 만약 반복횟수가 짝수라면, result의 값을 oper에 저장되어 있는 함수를 실행, 첫번째 인자를 result, 두번째 인자를 정수형으로 바꾼 e로
                result = oper(result, int(e))
            else:
                if e is '+': 
                    oper = add 
                elif e is '-':
                    oper = sub
                elif e is '*':
                    oper = multiple
                else:
                    oper = devide


expressions = input().split(', ')

c = calc()
next(c) # 코루틴 실행

for e in expressions:   
    print(c.send(e))

c.close()

# 사칙연산 코루틴 작성

