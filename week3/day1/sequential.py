import math
from functools import reduce
from functions import *
#기능별 혹은 절차, 특정 기준에 의해 함수로
#함수 인터페이스 - >signature
#함수 이름(인자목록) -> 반환값

#인터페이스와 구현부를 나누는 거 : 추상화 
raw_data = get_rawdata_from_excel('class_1.xlsx')

scores = []
for score in raw_data.values():
    scores.append(score)

avrg = reduce(lambda a, b: a + b, scores)/len(scores)
#분산 : (s - m) ** 2 다 더함 /학생수
variance = round(
    reduce(lambda a, b: a + b,
                  map(
                      lambda x:
                      (x - avrg)**2, scores))/len(scores),
    1)

standard_deviation = round(math.sqrt(variance), 1)
#print(standard_deviation)

print('평균 : {}, 분산 : {}, 표준편차 : {}'.format(avrg, variance,
                                           standard_deviation))
#학년 전체 평균이 50점 
if avrg <50 and standard_deviation >20:
    print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
elif avrg > 50 and standard_deviation >20:
    print("성적은 평균이상이지만 학생들 실력 차이가 크다. 주의 요망!")
elif avrg < 50 and standard_deviation <20:
    print("학생들간 실력차는 나지 않으나 성적이 너무 저조하다. 주의 요망!")
elif avrg > 50 and standard_deviation <20:
    print("성적도 평균 이상이고 학생들의 실력차도 크지 않다.")
      


















