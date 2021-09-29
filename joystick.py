import os
os.system('cls')

def solution(name):
    path = [0]
    length = 0
    cnt = list(map(lambda x : abs(ord('A') - ord(x)), name))
    for i in range(len(name)) :
        if cnt[i] != 0 :
            path.append(i)
            length += min(path[-1] + path[-2], len(name)-1 - path[-1])
        print(path, length)
        len_from_current = len(name) - 1 - i
    answer = 0
    return answer

print(solution("JAN"))
print(solution("JAZ"))
print(solution("JEROEN"))