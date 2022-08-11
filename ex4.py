# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 15:51:12 2022

@author: Gabriel Alves Candido

4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
"""

sp=67836.43
rj=36678.66
mg=29229.88
es=27165.48
outros=19849.53

soma=sp+rj+mg+es+outros

porsp = ((sp/soma)*100)
porrj = ((rj/soma)*100)
pormg = ((mg/soma)*100)
pores = ((es/soma)*100)
poroutros = ((outros/soma)*100)
print("SP – "+str(round(porsp,2))+"%"+
"\nRJ – "+str(round(porrj,2))+"%"+
"\nMG – "+str(round(pormg,2))+"%"+
"\nES – "+str(round(pores,2))+"%"+
"\nOutros – "+str(round(poroutros,2))+"%")