#!/usr/bin/python
#-*-coding:iso-8859-1 -*-


def montante_comp(pv, i, n):
    '''Função para cálculo de montante com juros compostos'''
    i = i / 100
    return pv * (1 + i)**n


def montante_simpl(c, i, n):
    '''Função para cálculo de montante  com juros simples (Bom somente para comparação com os compostos)'''
    i = i / 100
    return c * (1 + i * n)


def parcela(pv, i, n):
    '''Função para cálculo do valor de uma parcela de empréstimo'''
    i = i / 100
    return pv * ((i * (1 + i)**n) / (((1 + i)**n) - 1))


linha = '-' * 75
texto1 = ' Matematica Financeira '
c = float(input("Entre com o Capital : "))
i = float(input("Entre com a taxa de juros (a.m) %: "))
n = float(input("Periodo em meses :"))

print(linha)
print(texto1.center(75, '*'))
print(linha)
print('\n')
print("Montante com Juros simples: %0.2f " % (montante_simpl(c, i, n)))
print(linha)
print("Montante com Juros Compostos: %0.2f " % (montante_comp(c, i, n)))
print(linha)
print("Prestacao : %0.2f " % (parcela(c, i, n)))
print(linha)
