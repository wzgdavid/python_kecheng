# encoding: utf-8
身高 = 1.75
体重 = 80.5
bmi = 体重 / (身高**2)

if bmi < 18:
    print('过轻')
elif bmi < 25:
    print('zhengchang')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
else:
    print('严重')

