# Programa que:
# 1.0 - recebe uma quantidade de turmas selecionadas de um conjunto de 8 turmas em uma lista - Feito
# 2.0 - E para cada turma ele recebe um quantidade identerminada de alunos e seus respectivos dados como 
# as 4 notas e a média até que o usuário pare a excecução e proxiga com a proxima turma - feito
# 3.0 - Exiba um data frame de todos os alunos separados por colunas e virgulas - Feito
# 4.0 - descobri quais alunos irão para a prova final e armazenalos em uma lista -Feito
# 5.0 - receber as notas de cada aluno da lista da prova final e calcular sua aprovação pela formula abaixo:
# ((ma *6) + (pf*4)/ 10) == 5
# 6.0 - exibir um data frame dos alunos aprovados e outro dataframe dos alunos reporvados na prova final
from colorama import init
from termcolor import colored

# use Colorama to make Termcolor work on Windows too
init()

from decimal import Decimal, InvalidOperation

lista_de_turmas = ["6a","6b", "7a", "7b", "8a", "8b", "9a", "9b"]
lista_de_turmas_selecionadas = []
lista_de_alunos = []
lista_prova_final = []

while True:
    qt_turmas_selecionadas = input("Digite a quantidade de turmas a serem processadas: ")

    try:
        qt_turmas_selecionadas = Decimal(qt_turmas_selecionadas)
        qt_turmas_selecionadas = int(qt_turmas_selecionadas)
        
        if qt_turmas_selecionadas > 0:
            break
        else:
            print("Por Favor, digite um número maior que 0:\n") 
            
    except InvalidOperation:
        print("Por Favor, digite apenas números:\n")
       

def criarLinha ():
    print("","-"*79)

# Armazenando as turmas selecionadas em uma lista e verificando se ela existe no conjunto total 
for t in range (qt_turmas_selecionadas):
    turma = input ("Digite o ano e turma a ser calculada as médias ex; 6a, 6b (...) 9b: ").lower()
    while (not(turma in lista_de_turmas)):
        turma = input ("Digite o ano e turma a ser calculada as médias ex; 6a, 6b (...) 9b: ").lower()  
    
    lista_de_turmas_selecionadas.append(turma)

def exibirListaDadosAlunos ():
    criarLinha()
    print("     Nome     | Turma | Nota 1 | Nota 2 | Nota 3 | Nota 4 | Média | Prova Final  ")
    criarLinha()
    for aluno in lista_de_alunos:
        for t in lista_de_turmas:
            
            if (aluno[1] == t):
                
                cor_nome = "blue"
                cor_turma = "blue"
                cor_nota = "yellow"
                cor_media = "red"
                cor_prova_final = "green"
                   
                print((colored("{:^15}", cor_nome)+colored("{:^8}", cor_turma)+colored("{:^9.1f}",cor_nota)+colored("{:^9.1f}",cor_nota)+colored("{:^9.1f}",cor_nota)+colored("{:^9.1f}",cor_nota)+colored("{:^9.1f}",cor_media)+colored("{:^11}",cor_prova_final)).format(*aluno))    

def criarListaProvaFinal ():
    for aluno in lista_de_alunos:
        if(aluno[7] == "SIM"):
            lista_prova_final.append(aluno)                

for t in lista_de_turmas_selecionadas:
    criarLinha()
    print(f"    Notas da turma {t}")
    criarLinha()
    
    index = 1
    while(True):
        
        while True:
            nome = input(f"\nDigite o nome do aluno {index}: ")

            try:
                nome = Decimal(nome)
                nome = float(nome)
                print("Por Favor, digite apenas letras:")
                if(nome == ""):
                    print("Erro digite um nome: ")
            except InvalidOperation:
                break
                
                
        turma = t
        
        
        while True:
            nota1 = input(f"\nDigite a nota 1: ")

            try:
                nota1 = Decimal(nota1)
                nota1 = float(nota1)
                break
            except InvalidOperation:
                print("Por Favor, digite um número:")
       
        
        while True:
            nota2 = input(f"\nDigite a nota 2: ")

            try:
                nota2 = Decimal(nota2)
                nota2 = float(nota2)
                break
            except InvalidOperation:
                print("Por Favor, digite um número:")
            
        while True:
            nota3 = input(f"\nDigite a nota 3: ")

            try:
                nota3 = Decimal(nota3)
                nota3 = float(nota3)
                break
            except InvalidOperation:
                print("Por Favor, digite um número:")
        
        while True:
            nota4 = input(f"\nDigite a nota 4: ")

            try:
                nota4 = Decimal(nota4)
                nota4 = float(nota4)
                break
            except InvalidOperation:
                print("Por Favor, digite um número:")
        
        media = (nota1+nota2+nota3+nota4) / 4
        
        if (media < 7):
            provafinal = "SIM"
        else:
            provafinal = "NÃO"
    
        
        lista_de_alunos.append([nome, turma, nota1, nota2, nota3, nota4, media, provafinal])
        
        condicao_para_parar = input("\nDeseja cadastrar mais um aluno (SIM = Digite 'S' + Pressione Enter | NÃO = 'N' e Pressione Enter)?").upper()
        
        while condicao_para_parar != "S" and condicao_para_parar != "N":
            print("Erro Digite apenas S ou R")
            condicao_para_parar = input("\nDeseja cadastrar mais um aluno (SIM = Digite 'S' + Pressione Enter | NÃO = 'N' e Pressione Enter)?").upper()
        
        if (condicao_para_parar == "N"):
            break
        
        index += 1
print("\n Exibindo todos os dados de cada aluno: ")
exibirListaDadosAlunos()
criarListaProvaFinal ()

aprovados = []
repovados = []

print("\n")        
criarLinha()
print("\nCalculo da Prova final para os alunos que não passaram por média:\n ")
criarLinha()
print('\n')
for aluno in lista_prova_final:
    
    criarLinha()
    print(aluno[0],"",aluno[1])
    criarLinha()
    while True:
            nota_prova_final = input("Digite a nota da prova final: ")

            try:
                nota_prova_final = Decimal(nota_prova_final)
                nota_prova_final = float(nota_prova_final)
                break
            except InvalidOperation:
                print("Por Favor, digite um número:")  
                      
    media_das_avaliacoes = aluno[6]
    aprovacao = ((media_das_avaliacoes * 6) + (nota_prova_final * 4)) / 10 >= 5.0
    
    
    if(aprovacao):
        situacao = "Aprovado"
        aprovados.append([aluno[0], aluno[1], nota_prova_final, situacao])
    else:
        situacao = "Reprovado"
        repovados.append([aluno[0], aluno[1], nota_prova_final, situacao])    
        
def exibirListaDadosAlunosAprovadosPF ():
    criarLinha()
    print("  Nome | Turma | Nota - Prova Final | Situação  ")
    criarLinha()
    
    for aluno in aprovados:
        for t in lista_de_turmas:
            
            if (aluno[1] == t):
                
                cor_nome = "blue"
                cor_turma = "blue"
                cor_nota_prova_final = "red"
                cor_situacao = "green"
                
                print((colored("{:^15}", cor_nome) + colored("{:^10}", cor_turma) + colored("{:^20.1f}",cor_nota_prova_final) + colored("{:^14}",cor_situacao)).format(*aluno))                                   

def exibirListaDadosAlunosReprovadosPF ():
    criarLinha()
    print("      Nome      | Turma | Nota - Prova Final | Situação  ")
    criarLinha()
    for aluno in repovados:
        for t in lista_de_turmas:
            
            if (aluno[1] == t):
                
                cor_nome = "blue"
                cor_turma = "blue"
                cor_nota_prova_final = "red"
                cor_situacao = "green"
                
                print((colored("{:^15}", cor_nome) + colored("{:^10}", cor_turma) + colored("{:^20.1f}",cor_nota_prova_final) + colored("{:^14}",cor_situacao)).format(*aluno))                                         


print("\nDados dos alunos que Foram aprovados na Prova Final:")
if(aprovados == [] and repovados == []):
    print("Nenhum aluno realizou a Prova final")
else:
    exibirListaDadosAlunosAprovadosPF()

print("\n\nDados dos alunos que Foram Reprovados na Prova Final:")
if(aprovados == [] and repovados == []):
    print("Nenhum aluno realizou a Prova final")    
else:
    exibirListaDadosAlunosReprovadosPF()    
        
while True:
    sair = input("\n\n\nPrograma finalizado. Digite S e pressione Enter para sair do programa: ").upper()
    if(sair == "S"):
        break
    

    
