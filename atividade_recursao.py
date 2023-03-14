# Análise e Projeto de Algoritmos
# AC1: Ciência da Computação
#
# Email Impacta: juliana.rocha@aluno.faculdadeimpacta.com.br


def somatorio(n):
    if n == 0:
        return 0
    else:
        return n + somatorio(n-1)
    pass   

	
	

def potencia_de_2(n):
    if n == 1:
        return True
    elif n % 2 == 1:
        return False
    else:
        return potencia_de_2(n // 2)
    pass  

	
	
    


def qtd_digitos(n):
    if n == 0:
        return 0
    else:
        return 1 + qtd_digitos(n//10)
    pass

	


def soma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + soma_digitos(n // 10)
    pass


	

def soma_lista(lista, i):
    if i >= len(lista):
        return 0
    else:
        return lista[i] + soma_lista(lista, i+1)
    pass

	
	
