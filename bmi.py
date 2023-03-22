#bmi測試程式練習
high = input('請輸入身高(單位:公尺): ')
kg = input('體重: ')
high = float(high)
kg = float(kg)
BMI = kg / (high*high)
print('您的BMI為: ', BMI)
if BMI < 18.5:
    print('體重過輕')
elif BMI >= 18.5 and BMI< 24:
    print('健康體位')
elif BMI >= 24 and BMI< 27:
    print('過重')
elif BMI >= 27 and BMI < 30:
    print('輕度肥胖')
elif BMI >=30 and BMI < 35:
    print('中度肥胖')
else:
    print('重度肥胖')