inputArray = []
diaCompra = 0
diaVenda = 0
compra = 0
venda = 0

size = int(input("Digite o tamanho do array: "))

for i in range(size):
     numbsArray = int(input("Digite os valores do array: "))

     inputArray.append(numbsArray)

for i in range(len(inputArray)):
    if inputArray[i] == min(inputArray):
        diaCompra = i + 1
        compra = inputArray[i]
        i = diaCompra
    elif i + 1 < size:
        if inputArray[i] > inputArray[i + 1]:
            if compra > 0:
                venda = inputArray[i]
                diaVenda = i + 1

if venda - compra > 0:
    print(venda - compra)
else:
    print(0)

