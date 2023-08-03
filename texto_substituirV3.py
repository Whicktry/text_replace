import fileinput
import os
import shutil
import zipfile

def substituir_em_arquivo(nome_arquivo, alvo, nova_string):
    try:
        with fileinput.FileInput(nome_arquivo, inplace=True, backup='.bak') as arquivo:
            for linha in arquivo:
                linha_modificada = linha.replace(alvo, nova_string)
                print(linha_modificada, end='')

        # Remover o arquivo de backup criado automaticamente pelo fileinput
        os.remove(f"{nome_arquivo}.bak")

        print(f"Substituição em '{nome_arquivo}' concluída.")
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")

def substituir_em_zip(arquivo_zip, alvo, nova_string):
    try:
        # Criar a pasta versão2bk se não existir
        if not os.path.exists("versão2bk"):
            os.mkdir("versão2bk")

        # Extrair arquivos do .zip
        with zipfile.ZipFile(arquivo_zip, 'r') as zip_ref:
            zip_ref.extractall("versão2bk/")

        # Realizar a substituição nos arquivos extraídos
        for raiz, _, arquivos in os.walk("versão2bk/"):
            for arquivo in arquivos:
                caminho_arquivo = os.path.join(raiz, arquivo)
                substituir_em_arquivo(caminho_arquivo, alvo, nova_string)

        # Compactar os arquivos modificados de volta ao .zip
        with zipfile.ZipFile("versão2bk_modificado.zip", 'w') as zip_ref:
            for raiz, _, arquivos in os.walk("versão2bk/"):
                for arquivo in arquivos:
                    caminho_arquivo = os.path.join(raiz, arquivo)
                    caminho_arquivo_relativo = os.path.relpath(caminho_arquivo, "versão2bk/")
                    zip_ref.write(caminho_arquivo, caminho_arquivo_relativo)

        print(f"Substituições concluídas e arquivos modificados recompactados em 'versão2bk_modificado.zip'.")
    except FileNotFoundError:
        print(f"O arquivo '{arquivo_zip}' não foi encontrado.")

def substituir_em_arquivo_generico(nome_arquivo, alvo, nova_string):
    # Verificar se o arquivo é um .zip
    if nome_arquivo.lower().endswith('.zip'):
        substituir_em_zip(nome_arquivo, alvo, nova_string)
    else:
        substituir_em_arquivo(nome_arquivo, alvo, nova_string)

# Exemplo de uso
nome_arquivo = input("Digite o nome do arquivo: ")
alvo = input("Digite a palavra ou texto que deseja substituir: ")
nova_string = input("Digite a nova string de substituição: ")

substituir_em_arquivo_generico(nome_arquivo, alvo, nova_string)
