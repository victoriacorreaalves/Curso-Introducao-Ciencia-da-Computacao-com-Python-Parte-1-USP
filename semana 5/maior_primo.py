# recebe um número e retorna o maior primo <= aquele número
def eh_primo (n):
    teste= True
    aux1= 2
    while not (aux1==n):
        if(n%aux1==0):
            teste= False
        aux1=aux1+1
    return teste

def maior_primo (n):
    test= eh_primo(n)
    if not (test== True):
        while not (eh_primo(n)==True):
            test= eh_primo(n)
            n=n-1
    return n






