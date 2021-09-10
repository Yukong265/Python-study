# class MultipleIterator:
#     def __init__(self, stop, multiple):
#         self.stop = stop
#         self.multiple = multiple
#         self.current = 0         
 
#     def __iter__(self):
#         return self
 
#     def __next__(self):
#         self.current += 1
#         if (self.current * self.multiple) < self.stop:
#             return self.current * self.multiple
#         raise StopIteration
                                                     
 
# for i in MultipleIterator(20, 3):
#     print(i, end=' ')
 
# print()
# for i in MultipleIterator(30, 5):
#     print(i, end=' ')

                                 
def find(words):
    result = False # 기본 값을 false로 설정
    while True: 
        line = (yield result) # 문자열을 받아옴
        result = words in line # line안에 words가 있는지 확인 
                                 
f = find('Python') # 코루틴 실행
a = next(f)
print(a)
print(f.send('Hello, Python!')) # send로 문자열 전송
print(f.send('Hello, world!')) 
print(f.send('Python Script'))
 
f.close() # 코루틴 중단