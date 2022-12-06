# primeiro desafio xor - em cima de uma palavra label aplicar um codigo 13
s = 'label'
z = ''
for i in s:
    z = z + chr(ord(i)^13)
print('crypto{'+z+'}')
