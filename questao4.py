def getRetencao(mapaElevacao):
    retencao = 0
    esq = 0
    dir = len(mapaElevacao) - 1
    maxEsq = 0
    maxDir = 0

    while esq < dir:
        if mapaElevacao[esq] < mapaElevacao[dir]:
            if mapaElevacao[esq] >= maxEsq:
                maxEsq = mapaElevacao[esq]
            else:
                retencao += (maxEsq - mapaElevacao[esq])

            esq += 1
        else:
            if mapaElevacao[dir] >= maxDir:
                maxDir = mapaElevacao[dir]
            else:
                retencao += (maxDir - mapaElevacao[dir])

            dir -= 1

    return retencao

teste = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(getRetencao(teste))
