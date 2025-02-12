def solution(common):
    answer = 0
    n = len(common) # n 값
    r = 0
    
    if common[0] != 0:
        r = common[1]//common[0]
    
    if common[0]*r*r == common[2]: # 공비
        answer = common[0]*(r**(n))
    else:
        d = common[1]-common[0] # 공차
        answer = common[0]+(n)*d
        
    return answer