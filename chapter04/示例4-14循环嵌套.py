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
row=eval(input('请输入菱形的行数：'))
while row%2==0:
    print('请重新入菱形的行数：')
    row=eval(input('请输入菱形的行数：'))
top_row=(row+1)//2
for i in range(1,top_row+1):
    for j in range(1,top_row+1-i):
        print(' ',end='')
    for k in range(1,i*2):
        print('*',end='')
    print('')
bottom_row=row//2
for i in range(1,bottom_row+1):
    for j in range(1,i+1):
        print(' ',end='')
    for k in range(1,2*bottom_row-2*i+2):
        print('*',end='')
    print()
