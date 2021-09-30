import os
os.system('cls')

def solution(name):
    current = 0
    cnt = list(map(lambda x : min(ord(x) - ord('A'), ord('Z') - ord(x) + 1), name))

    for i in range(len(cnt)) :
        if cnt[i] != 0: 
            current, answer = i, i; 
            break;
            
    while True :
        answer += cnt[current]
        cnt[current]=0

        if all(i == 0 for i in cnt) :
            break;

        left, right = current -1, (current +1) % len(name)
        dist_left, dist_right = 1,1

        while cnt[left] == 0 : 
            dist_left += 1; 
            left -= 1;
        while cnt[right] == 0 : 
            dist_right +=1; 
            right = (right+1) % len(name);


        if dist_left > dist_right : 
            current = right
            answer += dist_right
        else : 
            current = len(name) + left if left < 0 else left
            answer += dist_left

    return answer

print(solution('ABAAAAAAAAABB'))

print(solution('ZAAAZZZZZZZ'))
print(solution("JAN"))
print(solution("JAZ"))
print(solution("JEROEN"))