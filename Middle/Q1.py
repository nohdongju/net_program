'''
1. 문자열 'Hello, IoT'에 대해 슬라이싱과 함수(메소드 포함)를 이용하여 아래와 같이
수행하는 프로그램을 작성하라. (10점)
A. 문자열의 문자수를 출력하라.
B. 문자열을 5번 반복한 문자열을 출력하라.
C. 문자열의 처음 3문자를 출력하라.
D. 문자열의 마지막 3문자를 출력하라.
E. 문자를 모두 대문자로 변경하여 출력하라.
주의사항 
- 문자열은 별도 입력 받을 필요없이 변수 str에 저장하여 사용
- 반복문 사용 불가
출력 결과 10
Hello, IoTHello, IoTHello, IoTHello, IoTHello, IoT
Hel
IoT
HELLO, IOT
'''
str = 'Hello, IoT'
# A
print(len(str))
# B
print(str*5)
# C
print(str[:3])
# D
print(str[-3:])
# E
print(str.upper())