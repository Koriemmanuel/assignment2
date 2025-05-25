weight = float(input('enter weight in kg: '))
unit = input('enter unit in kilogram (k) or pounds (l): ')
if unit == 'k':
    weight = weight * 2.2046
    unit = 'Lbs'
elif unit == 'l':
    weight = weight / 2.2046
    unit = "Kgs"
else:
    print('not valid!!')
print(f'weight in kg: {weight} {unit}')

