temps = [233, 235, 272, 231, -9999, 231, -9999, 291]

new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]
print(new_temps)

array1 = [i*2 for i in [1, -2, 10] if i>0]
print(array1)
array2 = [i*2 if i>0 else 0 for i in [1, -2, 10]]
print(array2)