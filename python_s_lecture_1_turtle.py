#import os
'''
print("Hello World")
a = 100
b = 2
result = a - b * b
print(f'{a} - b * b = {result}')
c = 39
result = c + a - b
print(f'c + a - b = {result}')
'''
#input()
#os.system("pause")

'''
a = int(input("첫번째 숫자를 입력하세요."))
b = int(input("두번째 숫자를 입력하세요."))
result = a + b
print(f'{a} + {b} = {result}')
result = a * b
print(f'{a} * {b} = {result}')
result = a / b
print(f'a / b = {result}')
print("%d" % 105.4)
print("%d %5d %05d" % (123, 123, 123))
print("{0:d} {2:05d} {1:5d}".format(1, 2, 3))
'''
'''
name = input('이름을 입력하세요 :')
age = int(input('나이를 입력하세요 :'))
print(f'이름은 {name}, 나이는 {age} 입니다.')
print("이름은 %s, 나이는 %d 입니다." % (name, age))
'''
'''
num1 = int(input("첫번째 숫자를 입력하세요 :"))
num2 = int(input("두번째 숫자를 입력하세요 :"))
num3 = int(input("세번째 숫자를 입력하세요 :"))
sum = num1 + num2 + num3
ave = sum//3
fave = sum/3
print("합은 %d 이고, 평균은 %d 입니다." % (num1+num2+num3, (num1+num2+num3)/3))
print(f'합은 {sum} 이고, 평균은 {ave} ({fave}) 입니다.')
'''
'''
##함수 선언 부분##
def myfunc():
    print("함수를 호출함")

##전역 변수 선언 부분 ##
gVar = 100

##메인 코드 부분 ##
if __name__ == '__main__': #__name__:현재 모듈의 이름은 담고 있는 내장 전역변수, main함수인지 판단해라
    print('메인 함수 부분이 실행됩니다.')
else:
    myfunc()
'''
'''
num = input("16진수 한 글자 입력:")

if (num >= '0' and num <= '9') or (num >= 'a' and num <= 'f') or \
   (num >= 'A' and num <= 'F'):
    print("10진수 =>", int(num, 16))
else:
    print("16진수가 아님")
#num10 = int(num, 16) 16진수 문자열을 정수형으로 변환
'''

import turtle as t
#t=turtle.Turtle()
t.shape('turtle')
t.speed(1)
t.pensize(3)
t.pencolor('skyblue')
t.up()
t.setpos(-200,200)
t.down()
t.right(90)
t.forward(200)
t.up()
t.setpos(-200, 100)
t.down()
t.left(90)
t.forward(100)
t.left(90)
t.up()
t.setpos(-100,200)
t.right(180)
t.down()
t.forward(200)
t.up()
t.setpos(0,200)
t.down()
t.forward(200)
t.up()
t.setpos(100,200)
t.down()
t.right(45)
t.forward(100)
t.left(90)
t.forward(100)

