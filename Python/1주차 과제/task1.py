'''
1. 회문
앞으로 읽으나 뒤로 읽으나 동일한 문장을 말한다.
예를 들어서 "mom", "civic", "dad" 등이 회문의 예이다.
사용자로부터 문자열을 입력받고 회문인지를 검사하는 프로그램을 작성하세요.

힌트) 파이썬에서 문자열을 조작하는 방법은?
'''

# sentence = input();

# if(sentence == sentence[::-1]):
#     print("회문입니다")
# else:
    # print("회문이 아닙니다.")

# if(sentence == reversed(sentence)):
#     print("회문입니다")
# else:
#     print("회문이 아닙니다.")

'''
2. mbti의 검사결과는 아래와 같이 16가지 유형이 있다.
'ISTJ'
'ISFJ'
'INFJ'
'INTJ'
'ISTP'
'ISFP'
'INFP'
'INTP'
'ESTP'
'ESFP'
'ENFP'
'ENTP'
'ESTJ'
'ESFJ'
'ENTJ'

이때, 200명의 mbti 검사결과를 random 하게 만드는 함수를 작성해보세요

출력 조건) 200명의 검사 결과는 list로 담는다 
힌트) 문자열을 랜덤하게 출력하는 코드는 아래와 같습니다.
import random

hint = "ABCDEFGH"
random.choice(hint)
'''
from gettext import find
import random

def shuffle():
    MBTI = ['ISTJ','ISFJ','INFJ','INTJ','ISTP','ISFP','INFP','INTP','ESTP','ESFP','ENFP','ENTP','ESTJ','ESFJ','ENTJ']
    result = []

    for _ in range(200):
        result.append(random.choice(MBTI))
    return result

result = shuffle()
print(result)

'''
3. 200명의 검사 결과가 각 16가지의 유형별 몇 명이 있는지 구하기

출력 조건) 딕셔너리 형식( {'mbti유형': 총 명수})
출력 예시) {'ESFP':17, 'INFJ': 13...}
힌트) 각각의 mbti 유형을 세는 법(counting)을 생각해보자.
'''
MBTI = ['ISTJ','ISFJ','INFJ','INTJ','ISTP','ISFP','INFP','INTP','ESTP','ESFP','ENFP','ENTP','ESTJ','ESFJ','ENTJ']

counting_result = {}

for i in MBTI:
    counting_result[i]=result.count(i)

print(counting_result)

'''
4. mbti 유형을 딕셔너리의 key로 입력했을 경우, value로 몇 명이 해당 mbti에 속해있는지 출력하는 함수를 작성
출력 조건) 알파벳 입력시 대,소문자는 결과에 영향을 미치지 않도록 코드를 작성할 것 
'''

yourmbti = input()

def findmbti(yourmbti):
    return counting_result[yourmbti.upper()]

print( findmbti(yourmbti), "명 포함")

'''
 5. 1992년 멋사는 300만원을 가지고 있었다.
 친구 A는 은행에 돈을 맡겨 매년 이자로 8.5%씩 받는 것을 추천하였고,
 친구 B는 매매가 300만원인 한정판 시계를 구매하라고 추천하였다.
 2022년 기준 한정판 시계의 가격은 3500만원이 되었고, 1992년 은행에 300만원을 넣었을 경우 2022년에는 얼마가 있을지 계산하여 친구 A와 친구 B 중 누구의 말을 듣는 것이 이득이었을지 판단해보자
 
추가 조건) 상수와 변수의 정의를 이용해 작성해볼 것 
출력 예시) "? 원 차이로 친구 ?가 맞았습니다."
'''

def count_interest(money,year):
    RATE = 1.085

    for _ in range(year):
        money *= RATE

    return int(money)

result = count_interest(300,30)-3500

if(result > 0):
    print(abs(result),"만원 차이로 친구 A가 맞았습니다.")
else:
    print(abs(result),"만원 차이로 친구 B가 맞았습니다.")

