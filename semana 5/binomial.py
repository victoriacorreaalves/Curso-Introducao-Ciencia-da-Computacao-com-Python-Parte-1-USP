# recebe dois números inteiros n e k e calcula o número binomial
# combinação simples de n elementos tomados k a k

def fatorial(n):
        if (n==0):
                fat=1
                return fat
        else:
                fat=1
                while (n>1):
                        fat= fat*n
                        n= n-1
                return fat
    
def numero_binomial (n,k):
    return fatorial(n) / (fatorial (k) * fatorial (n-k) )
