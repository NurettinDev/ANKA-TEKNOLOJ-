print('\n')

vize1 = float(input('1. vize: '))
vize2 = float(input('2. vize: '))
final = float(input('final : '))

ortalama = (((vize1 + vize2) / 2) * 0.4) + (final * 0.6)

print(f'not ortalamanız : {ortalama} ve dersten geçme durumunuz: {ortalama>=50}')
print('\n')
