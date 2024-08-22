import math
def func (x):
    z=math.exp(x)+math.sqrt(x)
    return z
def sum_n (n):
  n=abs(n)
  return sum(int(digit) for digit in str(n))
x=int(input("Введіть значення x: "))
if x>0:
  print("Значення z= ", func(x))
else:
  print("Під коренем не може бути від'ємного числа")
n=int(input("Введіть значення n: "))
print("Сума цифр числа: ", sum_n(n))
