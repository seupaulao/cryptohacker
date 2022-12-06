from pwn import xor

# descubra qual a senha, sem saber qual a chave

def minhasolucao_copiada():
    # parte 1
    s = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
    m = bytes.fromhex(s)
    # x ^ y = z
    # x ^ z = y
    # msg ^ segredo = chave
    # msg ^ chave = segredo
    # segredo = 'myXORke'
    # somo 'y' para que segredo = 'myXORkey' - tem mais sentido
    # parte 2
    p = xor("crypto{", m[0:7])
    p = p.decode() + 'y'
    # parte 3
    c = (p * ( len(m) // len(p) + 1))[:len(m)]
    flag = xor(m, c)
    print(flag.decode)


