# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 12:04:59 2022

@author: Gabriel Alves Candido

Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor
 sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8
 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado
 um número, ele calcule a sequência de Fibonacci e retorne uma mensagem
 avisando se o número informado pertence ou não a sequência.
 """

fibo=0
nacci=1
soma=0

cont=0
cont=eval(input("Insira um numero para calcular se faz parte da sequência de fibonacci:\n"))
while soma < cont:
    soma = fibo + nacci
    nacci= fibo
    fibo=soma
    if soma ==cont:
        print("Numero pertence a sequência.")
        break
    
if soma!=cont:
    print("Numero não pertence a sequência.")

    

    
    
    