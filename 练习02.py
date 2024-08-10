# f = float(input('请输入华氏温度: '))
# c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))


f = int(input('请输入华氏温度: '))
c = (f - 32) // 1.8
# print("{}华氏度 = {}摄氏度".format(f,c))

# print("{f}华氏度 = {c}摄氏度".format(f=f,c=c))

print(f"{f}华氏温度={c}摄氏温度")