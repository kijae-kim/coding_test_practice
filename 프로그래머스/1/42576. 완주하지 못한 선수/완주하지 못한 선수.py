from collections import Counter

def solution(participant, completion):
    # 참가자와 완주자 리스트의 이름 개수를 각각 센다.
    participant_counter = Counter(participant)
    completion_counter = Counter(completion)
    
    # 참가자에서 완주자를 빼면 완주하지 못한 사람이 남는다.
    result = participant_counter - completion_counter
    
    # result는 Counter 객체이며, 하나의 키만 갖고 있음 -> 그 키를 반환
    return list(result.keys())[0]
