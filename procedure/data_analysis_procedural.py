import openpyxl
from normal_dist import *

def get_data_from_excel(filename):
    '''
    get_data_from_excel(filename) -> {'name1' : 'score1', 'name2' : 'score2', ....}
    엑셀 파일에서 데이터를 가져옵니다.
    반환 값은 key가 학생 이름이고 value가 점수인 딕셔너리입니다. 
    '''
    dic = {}
    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    g = ws.rows

    for name, score in g:
        dic[name.value] = score.value

    return dic

def evaluateClass(avrg, total_avrg, std_dev):
    '''
    evaluateClass(avrg, total_avrg, std_dev) -> None
    avrg : 반 성적 평균
    total_avrg : 학년 전체 성적 평균
    std_dev : 반의 표준 편차 
    '''
    if avrg <total_avrg and std_dev >20:
        print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
    elif avrg > total_avrg and std_dev >20:
        print("성적은 평균이상이지만 학생들 실력 차이가 크다. 주의 요망!")
    elif avrg < total_avrg and std_dev <20:
        print("학생들간 실력차는 나지 않으나 성적이 너무 저조하다. 주의 요망!")
    elif avrg > total_avrg and std_dev <20:
        print("성적도 평균 이상이고 학생들의 실력차도 크지 않다.")

#학년 전체 학생의 평균 : 50점 

if __name__ == "__main__":
    raw_data = get_data_from_excel('class_1.xlsx')
    scores = list(raw_data.values())
    
    avrg = average(scores)
    variance = variance(scores, avrg)
    standard_deviation = std_dev(variance)

    print("평균 :{0}, 분산 : {1}, 표준 편차 : {2}".format(
        avrg, variance, standard_deviation))
    evaluateClass(avrg, 50, standard_deviation)

