# Segunda Lista de exercícios de Algoritmo e Programação
# Redes de Computadores P2
# Professor: Jefferson

# Exercícos

######################################################################################
# 1) Você foi contratado como desenvolvedor do Cinépolis que está com a necessidade
# de avaliar a opinião de 10 (dez) espectadores com relação a qualidade dos filmes
# apresentados em suas salas de cinema. Cada espectador de um cinema respondeu a
# um questionário no qual constava sua opinião em relação ao filme: ótimo – 3, bom –
# 2, regular – 1. Faça um programa utilizando python versão 3.5 que receba a opinião
# dos 10 (dez) espectadores, calcule e mostre:

# a) A quantidade de pessoas que responderam ótimo;
# b) A quantidade de pessoas que responderam bom;
# c) A quantidade de pessoas que responderam regular.
######################################################################################

# Este algoritmo mostra na tela o grau de satisfação dos usuários de um cinema, sobre seus filmes
#
# contador_regular = 0
# contador_bom = 0
# contador_otimo = 0
#
# for i in range(10):
#     grau = int(input('Digite seu grau de satisfação sobre nossos filmes: '))
#
#     if grau == 1:
#         contador_regular = contador_regular + 1
#     elif grau == 2:
#         contador_bom = contador_bom + 1
#     elif grau == 3:
#         contador_otimo = contador_otimo + 1
#     else:
#         print('Conceito inválido!')
#
# print('Quantidade de opinião Regular = %d' % contador_regular)
# print('Quantidade de opinião Bom = %d' % contador_bom)
# print('Quantidade de opinião Ótimo = %d' % contador_otimo)

##################################################################################
# 2) Desenvolva o sistema da questão anterior (questão 1) utilizando algoritmo na
# linguagem “Portugol”.
##################################################################################

# ALGORITMO "Grau de Satisfação"
#
# DECLARE REGULAR, BOM, OTIMO, GRAU INTEIRO
# DECLARE MENSAGEM_CONCEITO_INVALIDO, MENSAGEM_REGULAR, MENSAGEM_BOM, MENSAGEM_OTIMO LITERAL
#
# PARA i <-- 0 ATE 10 FAÇA
#
# SE grau = 1
#   ENTÃO regular <-- regular + 1
# SENÃO SE grau = 2
#   ENTÃO bom <-- bom + 1
# ENTÃO SE grau = 3
#   ENTÃO otimo <-- otimo + 1
# SENÃO
#   ENTÃO ESCREVA MENSAGEM_CONCEITO_INVALIDO <-- "Conceito inválido"
#
# ESCREVA MENSAGEM_REGULAR <-- "regular"
# ESCREVA MENSAGEM_BOM <-- "bom"
# ESCREVA MENSAGEM_OTIMO <-- "otimo"
#
# FIM_ALGORITMO


# Este algoritmo mostra a média aritimética de um aluno

###################################################################################
# 3) Você foi contratado como desenvolvedor do UNIPÊ que está com a necessidade de
# avaliar as 3 (três) notas de um aluno do curso de Redes de Computadores e mostrar
# a média aritmética e a mensagem constante da tabela abaixo baseada na média
# aritmética do aluno. Desenvolva esse programa utilizando python versão 3.5.
# Média Aritmética            Mensagem
# 0,0 até 4,0 (não incluso)   Reprovado
# 4,0 até 7,0 (não incluso)   Prova Final
# 7,0 até 10,0                Aprovado
###################################################################################


# Este algoritmo mostra na tela a média aritmética de um aluno

# nome = input('Por favor, digite seu nome: ')
# n1 = float(input('Digite sua primeira nota: '))
# n2 = float(input('Digite sua segunda nota: '))
# n3 = float(input('Digite sua terceira nota: '))
#
# media = (n1 + n2 + n3)/3
#
# if media >= 7:
#     print('Parabéns %s, você está APROVADO, BOAS FÉRIAS!' %(nome))
# elif media > 3.9 and media < 7.0:
#     print('Você está APTO a fazer PROVA FINAL %s.' %(nome))
# else:
#     print('Infelizmente %s, você está REPROVADO.' %(nome))



###############################################################################
# 4) Desenvolver o sistema da questão anterior (questão 3) utilizando português
# estruturado (Portugol).
###############################################################################

# ALGORITMO "Média Aritmética"
#
# DECLARE N1, N2, N3, MEDIA REAL
# DECLARE MENSAGEM_APROVADO, MENSAGEM_PROVA_FINAL, MENSAGEM_REPROVADO LITERAL
#
# leia N1, N2, N3
#
# MEDIA <-- (N1 + N2 + N3)/3
#
# MENSAGEM_APROVADO <-- "Aprovado"
# MENSAGEM_PROVA_FINAL <-- "Prova Final"
# MENSAGEM_REPROVADO <-- "Reprovado"
#
# se MEDIA >= 7.0
# 	então ESCREVA MENSAGEM_APROVADO "Aprovado"
#
# senão se MEDIA > 3.9 E MEDIA < 7.0
# 	então ESCREVA MENSAGEM_PROVA_FINAL "Prova Final"
#
# senão
# 	então ESCREVA MENSAGEM_REPROVADO "Reprovado"
#
# FIM_ALGORITMO