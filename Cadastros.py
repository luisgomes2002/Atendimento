#------------MENU------------
import math 
from time import sleep #timer
from playsound import playsound #play music
import ajuda #colocar linhas
from lib.inter import * #menu
from lib.arquivo import * #importar arquivo 

arq = 'Dados dos clientes'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['já tenho uma conta', 'Criar uma conta', 'Sair do Sistema!'])#se já tem uma conta pular a parte do cadastro e colocar para "entrar"
    if resposta == 1:
        ajuda.lin()
        print('\033[1m', 'Bem vindo ao atendimento on-line!', '\033[m')
        #sleep(1)
        print('Responda as peruntas abaixo para colocarmos você na fila de espera.')
        #sleep(1)

        meu_nome = 'Alex'
        print('Dígite seu NOME')
        #sleep(1)
        ajuda.lin()

        name = input('Coloque o seu nome: ').strip().title()
        #sleep(1)
        #sobrenome = input('Coloque o seu sobrenome: ').strip().capitalize()

        apresentação = name #or f'Sr. {sobrenome}'
        print(f'Olá {apresentação}. Meu nome é {meu_nome}!')
        #sleep(1)
        print('Agora digite sua idade')
        #sleep(1)
        idade = int(input('Dígite sua idade: '))

        dados = apresentação, idade

        ajuda.lin()
        print('Certo, você está na lista de espera, essa é a lista.')
        #sleep(1)
        print('Com ela você pode ver sua posição na fila e quais e quantas pessoas estão em sua frente.')
        #sleep(1)

        lista_de_espera = lerArquivo(arq)

        '''[['Lucas',  19], ['Caio', 19], ['Ana', 18], ['João',  19], ['Pedro',  19]]
        lista_de_espera.append(dados)
        for c in lista_de_espera:
            print(c[0])#colocar a idade''' 
        #sleep(1)

        ajuda.lin()
        #len --> quantidade de itens em uma lista 
        #print(f'Sua possição é {len(lerArquivo(arq))}°.')

        #sleep(1)
        #playsound('ex021.mp3')
        #ajuda.lin()

        print('Chegou a sua vez!')
        #sleep(1)
        print('Para continuarmo, termine de preencher o seu cadastros!')
        #sleep(1)
        print('Digite Sim para Contunuar ou Não para ir para o proximo!')
        #sleep(1)
        ajuda.lin()


        #------------PARTE 1 DA PERGUNTAS------------
        seguir = 'Sim'
        proximo = 'Não'
        pergunta_principal = print('\033[1m', 'O seu problema é com algum produto nosso?', '\033[m')
        escolha = input('Dígite : ').title()
        while escolha != 'Sim' and escolha != 'Não':
            escolha = input('Não entendi poderia repetir, o seu problema é com algum produto nosso? ').title()
        else:
            if escolha == seguir:
                print('Qual é o seu problema?')
                lista_de_problemas = ( 
                    {'opção': '(0)Veio quebrado.'} ,
                    {'opção': '(1)Veio violado.'},
                    {'opção': '(2)Defeito de fabrica.'},
                    {'opção': '(3)Não era o que você queria.'},
                    {'opção': '(4)Voltar.'},     
                )
                #sleep(1)
                ajuda.lin()
                print(lista_de_problemas[0]['opção'])
                print(lista_de_problemas[1]['opção'])
                print(lista_de_problemas[2]['opção'])
                print(lista_de_problemas[3]['opção'])
                print(lista_de_problemas[4]['opção'])
                ajuda.lin()
                print('escolha das opção a cima de 0 até 4')
                #sleep(1)
                lista_de_problemas = escolha2 = int(input('Escreva a sua opção: '))
                print(f'Você escolheu: {escolha2}.')
                #Pergunta 4
                while escolha2 == 4:
                    escolha2 = print('Voltando para as perguntas!!')
                #Pergunta 0
                if lista_de_problemas == 0:
                    print('Espere 1 minuto.')
                    #sleep(1)
                    proximo2 = 'Sim'
                    proximo3 = 'Não'
                    p1 = input('Gostaria de tocar o produto? ').capitalize()
                    while p1 != 'Sim' and p1 != 'Não':
                        input('Não entendi poderia repetir: ')
                    else:
                        if p1 == proximo2:
                            input('Coloque o seu endereço: ')
                            int(input('Coloque o seu número de telefone: '))
                            print('Fim da ocorreência, um e-mail foi enviado para você!!')
                        if p1 == proximo3:
                            print('Fim da ocorrência!!!')
                #Pergunta 1            
                elif lista_de_problemas == 1:
                    print('Espere 1 minuto.')
                    #sleep(1)
                    proximo2 = 'Sim'
                    proximo3 = 'Não'
                    input('Gostaria de tocar o produto? ').capitalize()
                    p2 = input('Tem alguma forma de provar que foi violado? ').capitalize()
                    while p2 != 'Sim' and p2 != 'Não':
                        input('Não entendi poderia repetir: ')
                    else:
                        if p2 == proximo2:
                            input('Coloque o seu endereço: ')
                            int(input('Coloque o seu número de telefone: '))
                            print('Fim da ocorreência, um e-mail foi enviado para você!!')
                            print('Por favor mandar as fotos da caixa para o e-mail enviado para o senhor(a).')
                        elif p2 == proximo3:
                            print('Fim da ocorrência!!!')
                #Pergunta 2            
                elif lista_de_problemas == 2:
                    print('Espere 1 minuto.')
                    #sleep(1)
                    proximo2 = 'Sim'
                    proximo3 = 'Não'
                    p3 = input('Gostaria de ser ressarcido? ')
                    while p3 != 'Sim' and p3 != 'Não':
                        input('Não entendi poderia repetir: ')
                    else:
                        if p3 == proximo2:
                            input('Coloque o seu endereço: ')
                            int(input('Coloque o seu número de telefone: '))
                            print('Fim da ocorreência, um e-mail foi enviado para você!!')
                            print('Por favor mandar as fotos da caixa e do defeito do produto para o e-mail enviado para o senhor(a).')
                        elif p3 == proximo3:
                            print('Fim da ocorrência!!!')
                #Pergunta 3 
                elif lista_de_problemas == 3:
                    print('Espere 1 minuto.')
                    #sleep(1)
                    proximo2 = 'Sim'
                    proximo3 = 'Não'
                    p4 = input('Gostaria de trocar por outro produto? ')
                    while p4 != 'Sim' and p4 != 'Não':
                        input('Não entendi poderia repetir: ')
                    else:
                        if p4 == proximo2:
                            input('Coloque o seu endereço: ')
                            int(input('Coloque o seu número de telefone: '))
                            input('O produto ainda esta em tempo de devolução? ')
                            print('Fim da ocorreência, um e-mail foi enviado para você!!')
                        elif p4 == proximo3:
                            print('Fim da ocorrência!!!')
                #Pergunta NENHUMA
                else:
                    print('Não encontramos o que você queria =-=*, poderia digitar novamente?')
                    #Fazer um loop
            if escolha == proximo:
                print('\033[1m', 'Problema com o atendimento?', '\033[1m')
                lista_de_problemas2 = ( 
                    {'opção': '(0)Problema com um atendente.'} ,
                    {'opção': '(1)Atendimento ruim.'},
                    {'opção': '(2)Atendente falou uma coisa e era outra.'},
                    {'opção': '(3)Atendente não informal das taxas.'},
                    {'opção': '(4)Voltar.'}, '\033[m'
                    )  
                    #sleep(1)      
                ajuda.lin()
                print(lista_de_problemas2[0]['opção'])
                print(lista_de_problemas2[1]['opção'])
                print(lista_de_problemas2[2]['opção'])
                print(lista_de_problemas2[3]['opção'])
                print(lista_de_problemas2[4]['opção'])
                ajuda.lin()
                print('escolha das opção a cima de 0 até 4')
                #sleep(1)
                lista_de_problemas2 = escolha3 = int(input('Escreva a sua opção: '))
                print(f'Você escolheu: {escolha3}.')
                #Pergunta 4
                while escolha3 == 4:
                    escolha3 = print('Voltando para as perguntas!!')
                    #Pergunta 0
                    if lista_de_problemas2 == 0:
                        print('Espere 1 minuto.')
                        #sleep(1)
                        proximo2 = 'Sim'
                        proximo3 = 'Não'
                        p1 = input('... ').capitalize()
                        while p1 != 'Sim' and p1 != 'Não':
                            input('Não entendi poderia repetir: ')
                        else:
                            if p1 == proximo2:
                                input('... ')
                                input(int('... '))
                                print('Fim da ocorreência, um e-mail foi enviado para você!!')
                            if p1 == proximo3:
                                print('Fim da ocorrência!!!')           
                    #Pergunta 1
                    elif lista_de_problemas2 == 1:
                        print('Espere 1 minuto.')
                        #sleep(1)
                        proximo2 = 'Sim'
                        proximo3 = 'Não'
                        p2 = input('O seu problema não foi resolvido? ').capitalize()
                        while p2 != 'Sim' and p2 != 'Não':
                            input('Não entendi poderia repetir: ')
                        else:
                            if p2 == proximo2:
                                input('... ')
                                input(int('... '))
                                print('Fim da ocorreência, um e-mail foi enviado para você!!')
                            if p2 == proximo3:
                                print('Fim da ocorrência!!!') 
                    #Pergunta 2
                    elif lista_de_problemas2 == 2:
                        print('Espere 1 minuto.')
                        #sleep(1)
                        proximo2 = 'Sim'
                        proximo3 = 'Não'
                        p3 = input('... ').capitalize()
                        while p3 != 'Sim' and p3 != 'Não':
                            input('Não entendi poderia repetir: ')
                        else:
                            if p3 == proximo2:
                                input('... ')
                                input(int('... '))
                                print('Fim da ocorreência, um e-mail foi enviado para você!!')
                            if p3 == proximo3:
                                print('Fim da ocorrência!!!')
                    #Pergunta 3
                    elif lista_de_problemas2 == 3:
                        print('Espere 1 minuto.')
                        #sleep(1)
                        proximo2 = 'Sim'
                        proximo3 = 'Não'
                        p4 = input('... ').capitalize()
                        while p4 != 'Sim' and p4 != 'Não':
                            input('Não entendi poderia repetir: ')
                        else:
                            if p4 == proximo2:
                                input('... ')
                                input(int('... '))
                                print('Fim da ocorreência, um e-mail foi enviado para você!!')
                            if p4 == proximo3:
                                print('Fim da ocorrência!!!')
                    #Pergunta NENHUMA
                    else:
                        print('Não encontramos o que você queria =-=*, poderia digitar novamente?')
                    #Fazer um loop

                    #if -> elif(infinito) -> else

        #------------PARTE 2 DA PERGUNTAS------------
        print('\033[1m', 'Olá tudo bem? \nSeu problema foi resolvido? ', '\033[m')
        seguir = 'Sim'
        proximo = 'Não'
        escolha = input('Gostaria continuar comprando? ')
        while escolha != 'Sim' and escolha != 'Não':
            escolha = input('Não entendi poderia repetir, gostaria de comprar algum produto nosso? ').capitalize().strip
        else:
            if escolha == 'Sim':
                print('Ok, vamos para as compras.')
                lista_de_produtos = (
                    #Colocar os produtos e seus valores, depois colocar a opçao de quantidade valor de cada item, e somar tudo no carrinho
                    {'opção': '(0)..., valor R$70'},
                    {'opção': '(1)..., valor R$8.9'},
                    {'opção': '(2)..., valor R$100'},
                    {'opção': '(3)..., valor R$247'},
                    {'opção': '(4)..., valor R$12.65'},
                    {'opção': '(5)..., valor R$7.43'},
                    {'opção': '(6)..., valor R$820'},
                    {'opção': '(7)..., valor R$2047'},
                    {'opção': '(8)..., valor R$13'},
                )
                #sleep(1)
                ajuda.lin()
                print(lista_de_produtos[0]['opção']) 
                print(lista_de_produtos[1]['opção']) 
                print(lista_de_produtos[2]['opção'])
                print(lista_de_produtos[3]['opção'])
                print(lista_de_produtos[4]['opção'])
                print(lista_de_produtos[5]['opção'])
                print(lista_de_produtos[6]['opção'])
                print(lista_de_produtos[7]['opção'])
                print(lista_de_produtos[8]['opção'])
                ajuda.lin()
    
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        ajuda.lin()
        print('\033[1m', 'Bem vindo ao atendimento on-line!', '\033[m')
        #sleep(1)
        print('Responda as peruntas abaixo para colocarmos você na fila de espera.')
        #sleep(1)

        meu_nome = 'Alex'
        #print('Dígite seu NOME')
        #sleep(1)
        ajuda.lin()

        #name = input('Coloque o seu nome: ').strip().title()
        #sleep(1)
        #sobrenome = input('Coloque o seu sobrenome: ').strip().capitalize()

        #apresentação = name #or f'Sr. {sobrenome}'
        #print(f'Olá {apresentação}. Meu nome é {meu_nome}!')
        #sleep(1)
        #print('Agora digite sua idade')
        #sleep(1)
        #idade = int(input('Dígite sua idade: '))

        #dados = apresentação, idade

        ajuda.lin()
        print('Certo, você está na lista de espera, essa é a lista.')
        #sleep(1)
        print('Com ela você pode ver sua posição na fila e quais e quantas pessoas estão em sua frente.')
        #sleep(1)

        lista_de_espera = lerArquivo(arq)

        '''[['Lucas',  19], ['Caio', 19], ['Ana', 18], ['João',  19], ['Pedro',  19]]
        lista_de_espera.append(dados)
        for c in lista_de_espera:
            print(c[0])#colocar a idade''' 
        #sleep(1)

        ajuda.lin()
        #len --> quantidade de itens em uma lista 
        #print(f'Sua possição é {len(lerArquivo(arq))}°.')

        #sleep(1)
        #playsound('ex021.mp3')
        #ajuda.lin()

        print('Chegou a sua vez!')
        #sleep(1)
        print('Para continuarmo, termine de preencher o seu cadastros!')
        #sleep(1)
        print('Digite Sim para Contunuar ou Não para ir para o proximo!')
        #sleep(1)
        ajuda.lin()


        #------------PARTE 1 DA PERGUNTAS------------
        seguir = 'Sim'
        proximo = 'Não'
        pergunta_principal = print('\033[1m', 'O seu problema é com algum produto nosso?', '\033[m')
        escolha = input('Dígite : ').title()
        while escolha != 'Sim' and escolha != 'Não':
            escolha = input('Não entendi poderia repetir, o seu problema é com algum produto nosso? ').title()
        else:
            if escolha == seguir:
                print('Qual é o seu problema?')
                lista_de_problemas = ( 
                    {'opção': '(0)Veio quebrado.'} ,
                    {'opção': '(1)Veio violado.'},
                    {'opção': '(2)Defeito de fabrica.'},
                    {'opção': '(3)Não era o que você queria.'},
                    {'opção': '(4)Voltar.'},     
                )
                #sleep(1)
                ajuda.lin()
                print(lista_de_problemas[0]['opção'])
                print(lista_de_problemas[1]['opção'])
                print(lista_de_problemas[2]['opção'])
                print(lista_de_problemas[3]['opção'])
                print(lista_de_problemas[4]['opção'])
                ajuda.lin()
                print('escolha das opção a cima de 0 até 4')
                #sleep(1)
                lista_de_problemas = escolha2 = int(input('Escreva a sua opção: '))
                print(f'Você escolheu: {escolha2}.')
                #Pergunta 4
                while escolha2 == 4:
                    escolha2 = print('Voltando para as perguntas!!')
                #Pergunta 0
                if lista_de_problemas == 0:
                    print('Espere 1 minuto.')
                    #sleep(1)
                    proximo2 = 'Sim'
                    proximo3 = 'Não'
                    p1 = input('Gostaria de tocar o produto? ').capitalize()
                    while p1 != 'Sim' and p1 != 'Não':
                        input('Não entendi poderia repetir: ')
                    else:
                        if p1 == proximo2:
                            input('Coloque o seu endereço: ')
                            int(input('Coloque o seu número de telefone: '))
                            print('Fim da ocorreência, um e-mail foi enviado para você!!')
                        if p1 == proximo3:
                            print('Fim da ocorrência!!!')
                #Pergunta 1            
                elif lista_de_problemas == 1:
                    print('Espere 1 minuto.')
                    #sleep(1)
                    proximo2 = 'Sim'
                    proximo3 = 'Não'
                    input('Gostaria de tocar o produto? ').capitalize()
                    p2 = input('Tem alguma forma de provar que foi violado? ').capitalize()
                    while p2 != 'Sim' and p2 != 'Não':
                        input('Não entendi poderia repetir: ')
                    else:
                        if p2 == proximo2:
                            input('Coloque o seu endereço: ')
                            int(input('Coloque o seu número de telefone: '))
                            print('Fim da ocorreência, um e-mail foi enviado para você!!')
                            print('Por favor mandar as fotos da caixa para o e-mail enviado para o senhor(a).')
                        elif p2 == proximo3:
                            print('Fim da ocorrência!!!')
                #Pergunta 2            
                elif lista_de_problemas == 2:
                    print('Espere 1 minuto.')
                    #sleep(1)
                    proximo2 = 'Sim'
                    proximo3 = 'Não'
                    p3 = input('Gostaria de ser ressarcido? ')
                    while p3 != 'Sim' and p3 != 'Não':
                        input('Não entendi poderia repetir: ')
                    else:
                        if p3 == proximo2:
                            input('Coloque o seu endereço: ')
                            int(input('Coloque o seu número de telefone: '))
                            print('Fim da ocorreência, um e-mail foi enviado para você!!')
                            print('Por favor mandar as fotos da caixa e do defeito do produto para o e-mail enviado para o senhor(a).')
                        elif p3 == proximo3:
                            print('Fim da ocorrência!!!')
                #Pergunta 3 
                elif lista_de_problemas == 3:
                    print('Espere 1 minuto.')
                    #sleep(1)
                    proximo2 = 'Sim'
                    proximo3 = 'Não'
                    p4 = input('Gostaria de trocar por outro produto? ')
                    while p4 != 'Sim' and p4 != 'Não':
                        input('Não entendi poderia repetir: ')
                    else:
                        if p4 == proximo2:
                            input('Coloque o seu endereço: ')
                            int(input('Coloque o seu número de telefone: '))
                            input('O produto ainda esta em tempo de devolução? ')
                            print('Fim da ocorreência, um e-mail foi enviado para você!!')
                        elif p4 == proximo3:
                            print('Fim da ocorrência!!!')
                #Pergunta NENHUMA
                else:
                    print('Não encontramos o que você queria =-=*, poderia digitar novamente?')
                    #Fazer um loop
            if escolha == proximo:
                print('\033[1m', 'Problema com o atendimento?', '\033[1m')
                lista_de_problemas2 = ( 
                    {'opção': '(0)Problema com um atendente.'} ,
                    {'opção': '(1)Atendimento ruim.'},
                    {'opção': '(2)Atendente falou uma coisa e era outra.'},
                    {'opção': '(3)Atendente não informal das taxas.'},
                    {'opção': '(4)Voltar.'}, '\033[m'
                )  
                    #sleep(1)      
                ajuda.lin()
                print(lista_de_problemas2[0]['opção'])
                print(lista_de_problemas2[1]['opção'])
                print(lista_de_problemas2[2]['opção'])
                print(lista_de_problemas2[3]['opção'])
                print(lista_de_problemas2[4]['opção'])
                ajuda.lin()
                print('escolha das opção a cima de 0 até 4')
                #sleep(1)
                lista_de_problemas2 = escolha3 = int(input('Escreva a sua opção: '))
                print(f'Você escolheu: {escolha3}.')
                #Pergunta 4
                while escolha3 == 4:
                    escolha3 = print('Voltando para as perguntas!!')
                    #Pergunta 0
                if lista_de_problemas2 == 0:
                    print('Espere 1 minuto.')
                    #sleep(1)
                    proximo2 = 'Sim'
                    proximo3 = 'Não'
                    p1 = input('... ').capitalize()
                    while p1 != 'Sim' and p1 != 'Não':
                        input('Não entendi poderia repetir: ')
                    else:
                        if p1 == proximo2:
                            input('... ')
                            input(int('... '))
                            print('Fim da ocorreência, um e-mail foi enviado para você!!')
                        if p1 == proximo3:
                            print('Fim da ocorrência!!!')           
                #Pergunta 1
                elif lista_de_problemas2 == 1:
                    print('Espere 1 minuto.')
                    #sleep(1)
                    proximo2 = 'Sim'
                    proximo3 = 'Não'
                    p2 = input('O seu problema não foi resolvido? ').capitalize()
                    while p2 != 'Sim' and p2 != 'Não':
                        input('Não entendi poderia repetir: ')
                    else:
                        if p2 == proximo2:
                            input('... ')
                            input(int('... '))
                            print('Fim da ocorreência, um e-mail foi enviado para você!!')
                        if p2 == proximo3:
                            print('Fim da ocorrência!!!') 
                #Pergunta 2
                elif lista_de_problemas2 == 2:
                    print('Espere 1 minuto.')
                    #sleep(1)
                    proximo2 = 'Sim'
                    proximo3 = 'Não'
                    p3 = input('... ').capitalize()
                    while p3 != 'Sim' and p3 != 'Não':
                        input('Não entendi poderia repetir: ')
                    else:
                        if p3 == proximo2:
                            input('... ')
                            input(int('... '))
                            print('Fim da ocorreência, um e-mail foi enviado para você!!')
                        if p3 == proximo3:
                            print('Fim da ocorrência!!!')
                #Pergunta 3
                elif lista_de_problemas2 == 3:
                    print('Espere 1 minuto.')
                    #sleep(1)
                    proximo2 = 'Sim'
                    proximo3 = 'Não'
                    p4 = input('... ').capitalize()
                    while p4 != 'Sim' and p4 != 'Não':
                        input('Não entendi poderia repetir: ')
                    else:
                        if p4 == proximo2:
                            input('... ')
                            input(int('... '))
                            print('Fim da ocorreência, um e-mail foi enviado para você!!')
                        if p4 == proximo3:
                            print('Fim da ocorrência!!!')
                #Pergunta NENHUMA
                else:
                    print('Não encontramos o que você queria =-=*, poderia digitar novamente?')
                #Fazer um loop

        #if -> elif(infinito) -> else

        #------------PARTE 2 DA PERGUNTAS------------
        print('\033[1m', 'Olá tudo bem? \nSeu problema foi resolvido? ', '\033[1m')
        seguir = 'Sim'
        proximo = 'Não'
        escolha = input('\033[1m', 'Gostaria continuar comprando? ', '\033[1m')
        while escolha != 'Sim' and escolha != 'Não':
            escolha = input('Não entendi poderia repetir, gostaria de comprar algum produto nosso? ').capitalize().strip
        else:
            if escolha == 'Sim':
                print('Ok, vamos para as compras.')
                lista_de_produtos = (
                    #Colocar os produtos e seus valores, depois colocar a opçao de quantidade valor de cada item, e somar tudo no carrinho
                    {'opção': '(0)..., valor R$70'},
                    {'opção': '(1)..., valor R$8.9'},
                    {'opção': '(2)..., valor R$100'},
                    {'opção': '(3)..., valor R$247'},
                    {'opção': '(4)..., valor R$12.65'},
                    {'opção': '(5)..., valor R$7.43'},
                    {'opção': '(6)..., valor R$820'},
                    {'opção': '(7)..., valor R$2047'},
                    {'opção': '(8)..., valor R$13'},
                )
                #sleep(1)
                ajuda.lin()
                print(lista_de_produtos[0]['opção']) 
                print(lista_de_produtos[1]['opção']) 
                print(lista_de_produtos[2]['opção'])
                print(lista_de_produtos[3]['opção'])
                print(lista_de_produtos[4]['opção'])
                print(lista_de_produtos[5]['opção'])
                print(lista_de_produtos[6]['opção'])
                print(lista_de_produtos[7]['opção'])
                print(lista_de_produtos[8]['opção'])
                ajuda.lin()
        
                #adicionar um FOR para poder somar o valor dos produtos
                s = 0
                for c in range(10):
                 n =  int(input('Digite o número dos produtos: '))
                s += n #s = s + n (é a mesma coisa em python)
                print('O valor final ficou {}'.format(s))
        
        
                '''print('escolha das opção a cima de 0 até 8')
                    e1 = int(input('Digite a sua opção: '))
                    print(f'{e1}')'''

                '''if escolha == 'Não':
                    print('Obrigado volte sempre!!')''' 

    elif resposta == 3:
        print('Saindo do sistema!')
        print('...3')
        #sleep(...1)
        print('...2')
        #sleep(1)
        print('...1')
        break
    else:
        print('\033[31mERRO! Digite uma opção valida\033[m')

