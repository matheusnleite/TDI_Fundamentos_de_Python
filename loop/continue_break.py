alvos = [
    {'ip': '192.168.1.1','so': 'mac', 'ativo': True,'portas': [80, 2,2, 21]},
    {'ip': '192.168.1.2','so': 'linux', 'ativo': False,'portas': [80, 2,2, 21]},
    {'ip': '192.168.1.3','so': 'windows', 'ativo': True,'portas': [80, 2,2, 21]},
    {'ip': '192.168.1.4','so': 'mac', 'ativo': False,'portas': [80, 2,2, 21]},
    {'ip': '192.168.1.5','so': 'windows', 'ativo': True,'portas': [80, 2,2, 21]},
]


def encontra_windows(maquinas):
    for maquina in maquinas:
        if maquina['so'] == 'windows':
            print("encontrei um windows")
            print("IP: " + maquina['ip'])
            break   #encerra a execucao do codigo




encontra_windows(alvos)


def encontra_windows(maquinas):
    for maquina in maquinas:
        if maquina['so'] == 'windows':
            print("nao ataquei pois eh windows")
            print("IP: " + maquina['ip'])
            continue #pula para o proximo elemento
        else:
            print("atacando maquina nao windows")
            print("IP: " + maquina['ip'])



encontra_windows(alvos)