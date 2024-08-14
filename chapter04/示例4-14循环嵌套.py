print('打印矩形')
for i in range(1,4):
    for j in range(1,5):
        print('*',end='')
    print()

print('打印三角形')
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='')
    print()

print('打印倒三角形')
for i in range(1,6):
    for j in range(1,7-i):
        print('*',end='')
    print()

print('打印等腰三角形')
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end='')
    for k in range(1,i*2):
        print('*',end='')
    print('')

print('打印菱形')
row=input('请输入菱形的行数：')
while row%2==0:
    print('请重新入菱形的行数：')
    row=eval(input('请输入菱形的行数：'))