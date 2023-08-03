import re

def substituir_ti0168(texto, alvo, nova_string):
    padrao = re.escape(alvo)
    texto_modificado = re.sub(padrao, nova_string, texto)
    return texto_modificado

# Exemplo de uso
texto_original = input("Digite o texto original: ")
alvo = input("Digite a palavra ou texto que deseja substituir: ")
nova_string = input("Digite a nova string de substituição: ")

texto_modificado = substituir_ti0168(texto_original, alvo, nova_string)
print("Texto modificado:")
print(texto_modificado)