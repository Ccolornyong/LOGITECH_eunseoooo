def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for l in range(len(numbers)):
            if i != l:
                answer.append(numbers[l]+numbers[i])
    answer = list(set(answer))
    answer.sort()
    
    return answer