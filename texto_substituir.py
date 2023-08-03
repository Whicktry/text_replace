import re

def substituir_ti0168(texto, nova_string):
    padrao = r'ti0168'
    texto_modificado = re.sub(padrao, nova_string, texto)
    return texto_modificado

# Exemplo de uso
texto_original = "Este é um texto com ti0168 e também ti0168 repetido várias vezes."
nova_string = "substituído"

texto_modificado = substituir_ti0168(texto_original, nova_string)
print(texto_modificado)