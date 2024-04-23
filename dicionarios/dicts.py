alvo = {
    'ip': '192.168.1.1', #coloca o nome da chave: o que armazenar na chave e terminar cada elemento com ","
    'so':  'windows',
    'ativo': True,
    'portas': [80, 2,2, 21],
}

#pode ser escrito na mesma linha também:: alvo = {'ip': '192.168.1.1', 'ativo': True,'portas': [80, 2,2, 21],}

print(alvo)
print(alvo['so']) #printar uma chave especifica
print(alvo['ativo'])


#listas com dics

alvos = [
    {'ip': '192.168.1.1','so': 'mac', 'ativo': True,'portas': [80, 2,2, 21]},
    {'ip': '192.168.1.2','so': 'linux', 'ativo': False,'portas': [80, 2,2, 21]},
    {'ip': '192.168.1.3','so': 'windows', 'ativo': True,'portas': [80, 2,2, 21]},
    {'ip': '192.168.1.4','so': 'mac', 'ativo': False,'portas': [80, 2,2, 21]},
    {'ip': '192.168.1.5','so': 'windows', 'ativo': True,'portas': [80, 2,2, 21]},
]

print(alvos[0]['so']) #quero pegar o SO do primeiro elemento da lista

#adicionar / atualizar uma chave e valor

alvo = {'ip': '192.168.1.5','so': 'windows', 'ativo': True,'portas': [80, 2,2, 21]}

print(alvo)
alvo['so'] = 'linux'
print(alvo)

#remover

del alvo['so']
print(alvo)

#mostrar somento os valores

print(alvo.values())

#mostrar somento as chaves

print(alvo.keys())

