'''
4. 2개의 복소수를 저장하는 MyComplex 클래스를 정의하고자 한다. 클래스의 멤버 변수로
첫번째 복소수의 실수 부분을 나타내는 real_1과 허수 부분을 나타내는 imaginary_1,
두번째 복소수의 실수 부분을 나타내는 real_2과 허수 부분을 나타내는 imaginary_2를
가진다. 지원하는 연산은 곱셈이다. 2개의 복소수 a=3-4i, b=-5+2i를 클래스에 저장하고,
a x b의 결과를 출력하는 프로그램을 작성하라. (10점)
주의사항 
- 파이썬에 내장되어 있는 복소수 클래스 사용 불가
- 곱셈 연산을 클래스 내 메소드로 구현하고, 해당 메소드 내에서 결과를 출력하도록 함
- (a + bi) x (c + di) = ac – bd + (ad + bc)i
출력 결과 -7+26i
'''
# class MyComplex:
#     def __init__(self, real_1 , imaginary_1, real_2, imaginary_2):
#         self.real_1 = real_1
#         self.imaginary_1 = imaginary_1
#         self.real_2 = real_2
#         self.imaginary_2 = imaginary_2

#     def multiply(self):
#         real_result = self.real_1 * self.real_2 - self.imaginary_1 * self.imaginary_2
#         imaginary_result = self.real_1 * self.imaginary_2 + self.imaginary_1 * self.real_2
#         if imaginary_result == 0:
#             s = real_result
#         elif real_result == 0:
#             s = str(imaginary_result) + 'i'
#         elif imaginary_result > 0:
#             s = str(real_result) + '+' + str(imaginary_result) + 'i'
#         else:
#             s = str(real_result) + str(imaginary_result) + 'i' 
#         return s

# c = MyComplex(3,-4,-5,2)
# print(c.multiply())



# class MyComplex:
#     def __init__(self, complex1, complex2):
#         self.real_1, self.imaginary_1 = self.divide(complex1)
#         self.real_2, self.imaginary_2 = self.divide(complex2)
#     def divide(self, c):
#         c = c.replace('i','')
#         if '+' in c[1:]:
#             real, img = c.split('+')
#         elif '-' in c[1:]:
#             idx = c[1:].index('-') + 1
#             real,img = c[:idx], c[idx:]
#         return int(real), int(img)
#     def multiply(self):
#         real_result = self.real_1 * self.real_2 - self.imaginary_1 * self.imaginary_2
#         imaginary_result = self.real_1 * self.imaginary_2 + self.imaginary_1 * self.real_2
#         if imaginary_result == 0:
#             s = real_result
#         elif real_result == 0:
#             s = str(imaginary_result) + 'i'
#         elif imaginary_result > 0:
#             s = str(real_result) + '+' + str(imaginary_result) + 'i'
#         else:
#             s = str(real_result) + str(imaginary_result) + 'i' 
#         return s

# c = MyComplex("3-4i", "-5+2i")
# print(c.multiply())