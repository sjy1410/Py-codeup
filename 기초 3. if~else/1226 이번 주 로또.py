lotto = list(map(int, input().split()))  # 로또번호
jihye = list(map(int, input().split()))  # 지혜가 찍은 번호

win = lotto[:6]  # 당첨번호
bonus = lotto[-1]  # 보너스번호

bonused = False  # 보너스 포함여부

cnt = 0  # 맞은 번호 수 카운트
for i in jihye:
    if i in win:
        cnt += 1

if bonus in jihye:
    bonused = True

if cnt == 6:
    print(1)
elif cnt == 5:
    if bonus in jihye:
        bonused = True
    if bonused == True:
        print(2)
    else:
        print(3)
elif cnt == 4:
    print(4)
elif cnt == 3:
    print(5)
else:
    print(0)
