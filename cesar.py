#numero da chave
chave = 3

# Informar a mensagem a ser codificada ou decodificada
mensagem = input("Digite a mensagem: ")
#mensagem = "Hoje eu estou muito feliz"

# número das letras nas extremidades do alfabeto
nA = ord('A')
nZ = ord('Z')
na = ord('a')
nz = ord('z')

# Variavel responsavel por influenciar 
opcao = input("Deseja codificar digite 'C' ou decodificar digite 'D': ")

cifrada = ""
if( opcao == "C"):
    for caracter in mensagem:
        # achar no alfabeto a letra que esteja chave posições a frente
        ind = ord(caracter)
        # Se estiver no intervalo de letras maiúsculas
        if nA <= ind <= nZ:
            nova_letra = chr((ind + chave)%(nZ+1) + ((ind + chave)//(nZ+1))*nA)
            # substituir na mensagem a letra pela nova_letra
            cifrada = cifrada + nova_letra
        # Outra forma de verificar se esta no intervalo de letras (agora) minúsculas
        # lembrar que range gera intervalos da forma [a, b), portanto somamos 1
        elif ind in range(na, nz + 1):
            nova_letra = chr((ind + chave)%(nz+1) + ((ind + chave)//(nz+1))*na)
            cifrada = cifrada + nova_letra
        # Se não for letra
        else:
            cifrada = cifrada + caracter
    print("-------------------------------") 
    print("Mensagem Original: ", mensagem)
    print("Criptografada: ", cifrada)
elif ( opcao == "D"):
    descripto = ''
    for i in mensagem:
        if 'A' <= i <= 'Z':
            if ord(i) - chave < ord('A'):
                descripto += chr(ord('Z') - (chave - (ord(i) + 1 - ord('A'))))
            else:
                descripto += chr(ord(i) - chave)
        elif 'a' <= i <= 'z':
            if ord(i) - chave < ord('a'):
                descripto += chr(ord('z') - (chave - (ord(i) + 1 - ord('a'))))
            else:
                descripto += chr(ord(i) - chave)
        else:
            descripto += i 
    print("-------------------------------")        
    print("Mensagem Original: ", mensagem)
    print("Descriptografada: ", descripto)
else:
    print("Opção invalida")