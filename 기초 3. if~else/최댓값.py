a, b = map(int, input().split())

s1 = a+b
s2 = a-b
s3 = b-a
s4 = a*b
s5 = a/b
s6 = b/a
s7 = a ** b
s8 = b ** a

sl = [s1, s2, s3, s4, s5, s6, s7, s8]

print('%.6f' % max(sl))
