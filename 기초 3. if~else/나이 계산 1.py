b, g = input().split()  # 생년월일, 성별코드
g = int(g)

age = 0

if g == 1 or g == 2:
    age = 2013-(1900+int(b[:2]))

elif g == 3 or g == 4:
    age = 2013-(2000+int(b[:2]))

print(age)
