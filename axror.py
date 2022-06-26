rub_to_som = 197.81
k = 0.01
p = 0.021
usdt = float(input('usdt: '))
rub = (usdt*(1+k+p))/rub_to_som
print(rub)
