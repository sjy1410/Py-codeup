 n = int(input())

s = []
for i in range(n):
    p = list(input().split())
    p[1] = int(p[1]) #배열의 2번째 위치를 정수형으로 변환해준다.
    s.append(p)

s.sort(key=lambda x: x[1], reverse=True) #숫자 정렬한 후 내림차순
print(s[2][0]) #성적이 3번째로 높은(s[2]) 학생 이름(p[0])출력
