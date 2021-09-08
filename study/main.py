def type_check(a_type, b_type):
    def deco(func):
        def wrapper(a, b):
            if ((type(a) != a_type) or (type(b) != b_type)):
                raise RuntimeError('자료형이 올바르지 않습니다.')
            else:
                return func(a,b)
        return wrapper
    return deco

# 처음에 if 조건을 둘이 같으면 함수 출력으로 했는데 안되서 반대로 했는데 됨;;

@type_check(int, int)
def add(a, b):
    return a + b
 
print(add(10, 20))
print(add('hello', 'world'))