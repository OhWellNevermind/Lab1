alphUk = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюяа12345678901'
input_Str = input()
n = int(input(':'))
for c in input_Str:
   print(alphUk[(alphUk.index(c) + n)], end='')

