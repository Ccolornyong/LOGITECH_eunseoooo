def nested_loop(current, zerofive, depth, result_list):
    if depth == 0:
        result = ''.join(current)
        result_list.append(int(result))
        return
    for char in zerofive:
        nested_loop(current + [char], zerofive, depth - 1, result_list)

def solution(l, r):
    answer = []
    zerofive = ["0", "5"]
    depth = len(str(r))
    
    nested_loop([], zerofive, depth, answer)
    
    result = [i for i in answer if l<=i<=r]
    return result if len(result)!=0 else [-1]