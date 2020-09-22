def Alvo():
    listaTemp = []
    resultado = []

    target = int(input("Alvo: "))

    total = int(input("Digite o tamanho do array: "))

    for i in range(total):
        numero = int(input("Digite os números: "))

        listaTemp.append(numero)

    listaTemp.sort()

    for i in range(len(listaTemp)):
        if listaTemp[i] + listaTemp[i + 1] == target:
            resultado.append(i)
            resultado.append(i + 1)
            print(f'[{i} , {i+1}]')
            break

Alvo()