import os # estou importando esse módulo para limpar a tela do console
import datetime
# Variáveis
saldo = 0
limite = 500
numero_saque = 0
LIMITE_SAQUE = 3
LIMITE_TRANSACAO = 10
transacao = 0
hora_atual = datetime.datetime.strftime(datetime.datetime.today(),"%H:%M")
data_atual = datetime.datetime.strftime(datetime.datetime.today(),"%d/%m/%Y")
tipo_operacao =""

# Layouts 

menu = f'''
==================== SISTEMA BANCÁRIO ==================== 
|                                                        |
|                    [1] - Depositar                     | 
|                    [2] - Sacar                         |
|                    [3] - Extrato                       |
|                    [0] - Sair                          |
|                                                        |
|========================================================|
|  Data : {data_atual}               Hora :  {hora_atual}         |
=============================================== V1.1 =====
'''

layout_deposito = '''
==================== SISTEMA BANCÁRIO ====================
|                                                        |
|                    DEPÓSITO BANCÁRIO                   | 
|                                                        |
============================================= V1.1 ======='''

layout_saque = '''
==================== SISTEMA BANCÁRIO ====================
|                                                        |
|                     SAQUE BANCÁRIO                     | 
|                                                        |
============================================= V1.1 ======='''


# Funções 

def depositar(dep):
    global saldo,tipo_operacao,transacao,LIMITE_TRANSACAO
    if dep > 0:
        if transacao < LIMITE_TRANSACAO:
            saldo += dep
            hora_atual=datetime.datetime.today()
            tipo_operacao+=f"{data_atual} - {hora_atual.strftime("%H:%M")} : Depósito realizado no valor de : R$ {dep:.2f}.  \n"
            transacao+=1
        else:
            print("Quantidade de Transação diária atingida!!")         
            hora_atual=datetime.datetime.today()
            tipo_operacao+=f"{data_atual} - {hora_atual.strftime("%H:%M")} : Quantidade de Transação diária atingida! \n"
            print("Precione uma tecla para prosseguir...")
            input()                               
    else: 
        print("Valor para depósito inválido!! precione uma tecla para prosseguir...")
        hora_atual = datetime.datetime.today()
        tipo_operacao+= f"{data_atual} - {hora_atual.strftime("%H:%M")} : Depósito negado, Valor inválido!!!\n"
        input()
    
    
# Fim Função depositar

def sacar(saq):
    global saldo,limite,numero_saque,LIMITE_SAQUE,tipo_operacao,transacao,LIMITE_TRANSACAO
    if saq>0:    
        if saldo >= saq:    
            if numero_saque < LIMITE_SAQUE: 
                if transacao < LIMITE_TRANSACAO:
                    if saq <= 500:        
                        saldo -=saq
                        hora_atual = datetime.datetime.today()
                        tipo_operacao+=f"{data_atual} - {hora_atual.strftime("%H:%M")} : Saque realizado no valor de    : R$ {saq:.2f}.  \n"
                        numero_saque +=1
                        transacao+=1
                    else: 
                        print("Valor acima do permitido, apenas R$ 500,00 por dia!")
                        hora_atual=datetime.datetime.today()
                        tipo_operacao+=f"{data_atual} - {hora_atual.strftime("%H:%M")} : Saque Negado, valor acima do permitido por dia!    \n"  
                        print("Precione uma tecla para prosseguir...")
                        input()                    
                else:
                    print("Quantidade de Transação diária atingida!!")         
                    hora_atual=datetime.datetime.today()
                    tipo_operacao+=f"{data_atual} - {hora_atual.strftime("%H:%M")} : Quantidade de Transação diária atingida! \n"
                    print("Precione uma tecla para prosseguir...")
                    input()                   
            else: 
                print("O Número de Saque diário foi atingido!!")
                hora_atual=datetime.datetime.today()
                tipo_operacao+=f"{data_atual} - {hora_atual.strftime("%H:%M")} : Saque Negado, limite diário atingido!  \n "
                print("Precione uma tecla para prosseguir...")
                input()                    
        else: 
            print("Saldo Insuficiente!!!")                
            hora_atual=datetime.datetime.today()
            tipo_operacao+=f"{data_atual} - {hora_atual.strftime("%H:%M")} : Saque Negado, Saldo Insuficiente!    \n"
            print("Precione uma tecla para prosseguir...")
            input()                    
    else:
        print("Valor para saque Inválido!!!, precione uma tecla para prosseguir...")                
        input()
        hora_atual=datetime.datetime.today()
        tipo_operacao+=f"{data_atual} - {hora_atual.strftime("%H:%M")} : Saque Negado, Valor para Saque inválido  \n"
    


    
#Fim Função sacar


def extrato_bancario():
    global saldo,tipo_operacao
    extrato = '''
========================= SISTEMA BANCÁRIO =========================
                                                        
                          EXTRATO BANCÁRIO      

--------------------------------------------------------------------
Data         Hora    Movimentação              
'''
    print(extrato)
    print(tipo_operacao)
    print("=====================================================================")
    print(f"                O Saldo atual é de R$ {saldo:.2f}             ")
    print("======================================================== V1.1 =======")

# Fim Função  extrato_bancario

while True:

    opcao = int(input(menu))
    if opcao == 1:
        os.system('cls')
        print(layout_deposito)
        depositar(int(input("Informe o valor do Depósito :")))  
        os.system('cls')      
    elif opcao == 2:
        os.system('cls')
        print(layout_saque)
        sacar(int(input("Informe o valor do Saque :")))
        os.system('cls')        
    elif opcao == 3:
        os.system('cls')        
        extrato_bancario()
        input()
        os.system('cls')        
    elif opcao == 0:
        print("Você está saindo do Sistema Bancário!")
        break
    else:    
        print("Opção inválida!! selecione uma opção Válida!!!")
        print("Precione uma tecla para prosseguir...")
        input()                    
        os.system('cls')

