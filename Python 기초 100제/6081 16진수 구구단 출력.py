n=int(input(), 16) #n=int(input(),x) -> x진수 입력받기

for i in range(1,16): #1~15
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='') #'%X'%n -> n값 16진수로 출력 
