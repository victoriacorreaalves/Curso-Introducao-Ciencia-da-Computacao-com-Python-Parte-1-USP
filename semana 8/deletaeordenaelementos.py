
# recebe uma lista, deleta elementos repetidos
# retorna a lista ordenada

def remove_repetidos (lista):
    k=0
    while k< len(lista):
        i= k+1
        while (i< len(lista)):
            if(lista[i]==lista[k]):
                del lista[i]
            else:
                i=i+1
        k=k+1
    return sorted(lista)
    
