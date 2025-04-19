'''
3. 문자열
'https://search.naver.com/search.naver?where=nexearch&ie=utf8&query=iot'가
주어졌을 때, 아래 출력 결과와 같이 딕셔너리를 생성한 후 출력하는 프로그램을 작성하라.
(10점)
주의사항 
- 파이썬에 내장되어 있는 URL 파싱 라이브러리 사용 불가
- 반드시 split 함수를 사용할 것
출력 결과 {'where':'nexearch', 'ie':'utf8', 'query':'iot'}
'''
str = 'https://search.naver.com/search.naver?where=nexearch&ie=utf8&query=iot'.split('?')[1]
lst = str.split('&')
dic = {}
for i in lst:
    k,v = i.split('=')
    dic[k] = v
print(dic)