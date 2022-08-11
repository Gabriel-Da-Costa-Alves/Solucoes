# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 12:59:24 2022

@author: Gabriel Alves Candido

3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
"""

import json

with open("dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)
    
    
def media():
    valores=[]
    dias=0
    for i in dados:
        valores.append(i['valor'])
        if i['valor']!=0:
            dias+=1
    media=sum(valores)/dias
    print(round(media,2)) 
    
def menor():
    valores=[]
    
    for i in dados:
        if i['valor']!=0:
            valores.append(i['valor'])
    menor=valores[0]
    for i in valores:
        if i<menor:
            menor=i
    return round(menor,2)

def maior():
    valores=[]
    maior=0
    for i in dados:
        if i['valor']!=0:
            valores.append(i['valor'])
    for i in valores:
        if i>maior:
            maior=i
    return round(maior,2)
    
def medmaior():
    valores=[]
    dias=0
    for i in dados:
        valores.append(i['valor'])
        if i['valor']!=0:
            dias+=1
    media=sum(valores)/dias
    valores=[]
    cont=0
    for i in dados:
        if i['valor']!=0:
            valores.append(i['valor'])
    for i in valores:
        if i>media:
            cont+=1
    return cont  
    
print("• O menor valor de faturamento ocorrido em um dia do mês;\n R$ "+str(menor())+
      "\n• O maior valor de faturamento ocorrido em um dia do mês;\n R$ "+str(maior())+
      "\n• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.\n "+str(medmaior())+" dias")