#em vez de criar varias variáveis, podemos criar uma lista com varios itens

alvos = ["192.168.10.10","192.168.15.11","192.168.1.2","192.168.20.101"]

#uma lista pode ter varios tipos de dados dentro

exemplo_lista = [10,"string", True, 9.99, ["outra lista",877]]

#IMPRIMIR LISTA

print(alvos) #printar a lista toda

print(alvos[2]) #printa o item 3 da lista. OBS: o primeiro indice da lista é o 0

print(alvos[-2]) #começa a contagem dos indices ao contrario, começando no ultimo elemento

print(alvos[0:2]) #imprime do indice 0 ate o 2

#ADICIONAR ITENS

alvos.append("TDI") #adiciona um item no final da lista

alvos.insert(0, "inicio") #adiciona um item no inicio da lista

#REMOVER ITENS

alvos.remove("192.168.15.11") #remove um item especifico da lista

alvos.pop() #remove o último item da lista e salva pra ele, podendo ser atribuido entao a uma variavel. Ex: ultimo = alvos.pop()

#CONSULTAR LISTA

print(type(alvos))
print(len(alvos)) #imprime o tamanho da lista

print("192.168.10.10" in alvos) #Retorna True se o valor 192.168.10.10 estiver na lista alvos, e False se nao estiver
print("192.168.10.40" not in alvos) #afirmação contraria a de cima, se nao estiver na lista, retorna True