from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from time import sleep 

def multiplo(texto):
    while len(texto.encode("utf-8")) % 16 != 0:
        texto += " "
    return texto

# definição pra criptografar 
def criptografar(mensagem, chave):
    mensagem = multiplo(mensagem)
    cifra = AES.new(chave, AES.MODE_CBC)
    cripto = cifra.encrypt(mensagem.encode("utf-8"))
    return cifra.iv + cripto 

# aqui descriptografa
def descriptografar(cripto_hex, chave):
    if isinstance(cripto_hex, str):
        cripto = bytes.fromhex(cripto_hex)
    else:
        cripto = cripto_hex
    iv = cripto[:16]
    cifra = AES.new(chave, AES.MODE_CBC, iv)
    texto_bytes = cifra.decrypt(cripto[16:])
    return texto_bytes.decode("utf-8").rstrip() 

# Área de login 
while True:
    print('-='*15)
    print('ÁREA DE LOGIN'.center(30," "))
    print('-='*15)
    nome_usuario = str(input("Por Favor digite seu nome:")).strip()
    senha_usuario = int(input(f'prezado Sr(a): {nome_usuario} digite sua senha:'))
    print('ANALISANDO...')
    sleep(0.5)
    if senha_usuario == 1234:
        print('ACESSO PERMITIDO!')

        # Cria chave aleatoria/ carrega chave 
        usar_chave = input("Você já tem uma chave anterior? (s/n): ").strip().lower()

        if usar_chave == "s":
            chave_hex = input("Cole a chave antiga em HEX: ").strip()
            chave = bytes.fromhex(chave_hex)
            print("Chave carregada com sucesso!")
        else:
            chave = get_random_bytes(16)
            print("Nova chave gerada!")
            print("Copie e guarde sua chave (em HEX) para usar depois:")
            print(chave.hex())
            
        # Guarda a mensagem criptografada
        mensagem_guardada = " "

        # Menu de escolha 
        while True:
            print('-='*15)
            print('MENU'.center(30," "))
            print('-='*15)
            print('[1] Criptografar\n[2] Descriptografar\n[3] Sair')
            print('-='*15)
            menu = int(input('Digite sua escolha:'))
            if menu == 1:
                mensagem_criptografada = input("Digite sua mensagem: ")
                print('Criptografando... Aguarde!')
                sleep(0.7)
                criptografada = criptografar(mensagem_criptografada, chave)
                mensagem_guardada = criptografada 
                print("Mensagem Criptografada:", criptografada.hex())

            elif menu == 2:
                if mensagem_guardada:
                    entrada = input("Cole a mensagem criptografada em HEX: ").strip()
                    if entrada == "":
                        descriptografada = descriptografar(mensagem_guardada, chave)
                    else:
                        descriptografada = descriptografar(entrada, chave)
                    print('Descriptografando...')
                    sleep(0.5)
                    print("Mensagem descriptografada:", descriptografada)
            elif menu == 3:
                print('FINALIZANDO PROGRAMA...')
                sleep(0.5)
                break
            else:
                print('Opção invalida!')
    else:
        print('ACESSO NEGADO!')
        sleep(1)
        print('PROTOCOLO DE AUTO DESTRUIÇÃO INICIADO!!')       
        print("Contagem regressiva:")
        for i in range(5, 0, -1): 
            print(i)
            sleep(1)
        print('Todos os arquivos apagados!')
        sleep(1)
        break 