#for [item] in [lista]:
    #ação

numeros =[1,2,3,4]

for n in numeros:
    print(n)


alvos = [
    {'ip': '192.168.1.1','so': 'mac', 'ativo': True,'portas': [80, 2,2, 21]},
    {'ip': '192.168.1.2','so': 'linux', 'ativo': False,'portas': [80, 2,2, 21]},
    {'ip': '192.168.1.3','so': 'windows', 'ativo': True,'portas': [80, 2,2, 21]},
    {'ip': '192.168.1.4','so': 'mac', 'ativo': False,'portas': [80, 2,2, 21]},
    {'ip': '192.168.1.5','so': 'windows', 'ativo': True,'portas': [80, 2,2, 21]},
]

for alvo in alvos:
    if alvo["ativo"]:
        print(alvo["ip"])
        for porta in alvo['portas']:
            print("atacando porta " + str(porta)) #transformando porta para string para conseguir concatenar no print      
        print("#############")






