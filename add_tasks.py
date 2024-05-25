def squar_number(val_int):
    n = []
    for i in range(val_int):
        if i % 2 == 0 and i != 0:
            n.append(i ** 2)
    return n


while 1 == 1:
    val_int = input('Введите число:')
    if val_int.isdigit():
        break
    else:
        print('сломались хоть и не должны')
list_n = squar_number(int(val_int))
print(*list_n)
######################2222222####################################
import random

list_n = [9567, 9661, 6541, 4146, 534, 5627, 6900, 5803, 7794, 1174, 2365, 9759, 355, 2071, 5053, 1252, 4063, 3068,
          9552, 9895, 5642, 3286, 5740, 9318, 1684, 8758, 9520, 9420, 9799, 2893, 728, 891, 1560, 5006, 8043, 5106,
          3597, 9990, 191, 3098, 5996, 6295, 7755, 4077, 6759, 2929, 2424, 6006, 8318, 565, 9482, 2015, 8580, 8314,
          8422, 9978, 4655, 4768, 3722, 1119, 4712, 9834, 754, 1688, 6179, 9648, 5841, 2007, 574, 9245, 4881, 9429,
          3683, 6205, 4985, 2147, 5614, 928, 6040, 2273, 8337, 2872, 6867, 104, 879, 7092, 4409, 7872, 4650, 9063, 236,
          4685, 3156, 1208, 5550, 4944, 6325, 7783, 626, 285, 7074, 864, 1464, 4313, 8082, 6920, 8045, 4141, 9063, 1035,
          8285, 9379, 5298, 6683, 7944, 1003, 3065, 3515, 5225, 4705, 8792, 8791, 7277, 9477, 3771, 1097, 8472, 9925,
          1456, 2177, 4675, 8933, 7047, 3803, 4044, 9532, 1181, 7097, 773, 41, 5211, 9132, 1179, 470, 7000, 8710, 5184,
          9928, 2711, 3412, 5705, 5179, 3091, 6340, 5273, 8896, 1253, 2014, 3535, 4067, 6499, 8594, 581, 8314, 78, 9107,
          1821, 7032, 1267, 6406, 7933, 6472, 4437, 867, 3251, 9073, 2813, 4111, 7759, 158, 6482, 2444, 6931, 9917,
          6325, 8541, 8535, 7060, 2782, 6913, 9085, 6724, 9380, 4257, 6210, 7325, 7213, 8028, 3958, 3319]
#print(len(list_n))

while 1 == 1:
    k_number = input(f'Введите число между {max(list_n)} and {min(list_n)} :')
    if k_number.isdigit():
        k_number = int(k_number)
        break
list_n.sort()
#print(list_n)
n=[]
for i in list_n:
    if k_number > i:
        n.append(round(i**0.5,3))
        continue
    else:
        break
print(*n)

############*****************************22222****************
list_n=[]
for k in range(10000):
    list_n.append(random.randint(1,20000))

cratno_5=[]
for i in list_n:
    if i%5 == 0:
       cratno_5.append(i)

arithmetic_mean = round(sum(cratno_5)/len(cratno_5),3)
print(f'Список кратных 5 чисел {cratno_5}')
print(f'Среднеарифметическое чисел кратных 5 :{arithmetic_mean}')

list_n.sort(reverse=True)
list_b = []
for i in list_n:
    if i > arithmetic_mean:
        list_b.append(round(i**0.5,3))
    else:
        break
print(f'корни элементов из списка ,которые больше "Среднеарифметического числа кратных 5"')
print(*list_b)
##################################33333333**************
list_n = []
for k in range(50):
    list_n.append(random.randint(100, 1000))

list_n.append(41 * 15)  # а то вдруг не выпадет ))
list_n.sort()
max_n = list_n[-1]
min_n = list_n[0]
arithmetic_mean = (max_n + min_n) / 2

num_2 = 0
for i in list_n:
    if (i % 41 == 0) and (i > arithmetic_mean):
        num_2 += 1
print("Ищем элементы кратные 41  случайный список из 50 элементов")
print(f'выявили  {num_2} ')

###################################        44
text_1 = 'Наутро Буратино проснулся веселый и здоровый как ни в чем не бывало.'
print(text_1,"Исходный текст")
text_list = text_1.split()

for i in range(len(text_list)):
    n=random.randint(1, len(text_list)-1)
    # подготовим испорченный текст
    if  text_list[n][0] != '*':
         text_list[n] = '*'+ text_list[n][1:]
         #print(text_list[n])

text_2 = ' '.join(text_list)
text_list=text_2.split()
print(text_list,"Портим его случайным образом")
# список подготовили ))
text_2 = ""
for i in text_list:

    if i[0] != '*':
        text_2 +=" "+ i

print(text_2,f' "Выводим только неиспорченные".')

########################## 55  алгоритм Евклида
list_5=[[5, 7], [21, 111], [63, 49]]

def nod_1(a_,b_):
    if a_ < b_:
        a_, b_ = b_, a_
    if b_ == 0:
        return a_
    else:
        print(a_%b_,a_,b_)
        #return nod_1(b_,a_-b_)  # первый вариант
        return nod_1(b_,a_%b_)   #  второй вариант меньше циклов
for list_par in list_5:
    c = nod_1(*list_par)
    print(c)
##################################    6

def convert(L):
    list_6=[]
    for i in L:
        list_6.append(int(i))
    return list_6
print(convert([1, 2, '3', '4', '5', 6]))