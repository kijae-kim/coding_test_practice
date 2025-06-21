def solution(intStrs, k, s, l):
    
    answer = []
    
    for ret in intStrs:
        a = ret[s:]
        # l 길이로 출력되게
        if int(a[:l]) > k:
            answer.append(int(a[:l]))
        
    return answer
    
    