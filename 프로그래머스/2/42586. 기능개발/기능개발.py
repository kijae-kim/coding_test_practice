def solution(progresses, speeds):
    # 1. 각 기능의 완료까지 필요한 일수 계산
    days = [(100 - p + s - 1) // s for p, s in zip(progresses, speeds)]
    
    # 2. 배포 묶음 계산
    answer = []
    current = days[0]  # 첫 배포 기준일
    count = 1          # 현재 배포에 포함된 기능 수
    
    for day in days[1:]:
        if day <= current:
            count += 1  # 앞 기능과 함께 배포
        else:
            answer.append(count)
            current = day
            count = 1
    
    answer.append(count)  # 마지막 묶음
    return answer
