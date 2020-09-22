abreParenteses = '('
fechaParenteses = ')'
abreColchete = '['
fechaColchete = ']'
abreChave = '{'
fechaChave = '}'


def Brackets(umaString):
    itemArray = []

    if (len(umaString) % 2) != 0:
        return 'NAO'

    for i in range(len(umaString)):
        if umaString[i] == abreParenteses:
            itemArray.append(abreParenteses)
        elif umaString[i] == abreColchete:
            itemArray.append(abreColchete)
        elif umaString[i] == abreChave:
            itemArray.append(abreChave)
        elif umaString[i] == fechaParenteses:
            if itemArray == []:
                return 'NAO'
            if itemArray.pop() != abreParenteses:
                return 'NAO'
        elif umaString[i] == fechaColchete:
            if itemArray == []:
                return 'NAO'

            if itemArray.pop() != abreColchete:
                return 'NAO'
        elif umaString[i] == fechaChave:
            if itemArray == []:
                return 'NAO'

            if itemArray.pop() != abreChave:
                return 'NAO'

    return 'SIM'


print(Brackets('{[()]}'))
print(Brackets('{[(])}'))
print(Brackets('{{[[(())]]}}'))
