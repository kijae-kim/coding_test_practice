def solution(my_string, is_suffix):
    
    # 1. my_sting 접미사
    word = []
    for i in range(len(my_string)):
        word.append(my_string[i:])
    # 2. 접미사와 is_suffix 비교
    answer = 0
    if is_suffix in word:
        answer += 1
    else:
        answer += 0
        
    return answer