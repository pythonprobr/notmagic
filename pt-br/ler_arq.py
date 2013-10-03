
with open('exemplo.txt', encoding='utf-8') as arq:
    for linha in arq:
        linha = linha.rstrip()
        if linha:
            print(linha)
