#deposit = 11000000
rub_to_som = 193
usdt = float(input('usdt price: '))
rub = float(input('rub: '))
rub *= 0.995
output = (rub*rub_to_som) - usdt
#print(output)
print(output>0)
print(output/usdt*100,'%')
#print((1+output/usdt)*deposit)
