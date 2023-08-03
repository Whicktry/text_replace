# text_replace
Mostraremos aqui como substituir nomes específicos dentro de uma pasta (zip ou não) usando um script feito em python que ajudará automatizar a edição de arquivos grandes ou pequenos reduzindo horas de trabalho manual.

Importação de Bibliotecas:

No início do código, importamos as bibliotecas necessárias para o funcionamento do programa.
fileinput: Usada para realizar a substituição de palavras em um arquivo.
os: Usada para operações do sistema, como criar diretórios e obter caminhos absolutos.
shutil: Usada para operações de cópia e remoção de arquivos.
zipfile: Usada para lidar com arquivos .zip.
Função substituir_em_arquivo:

Essa função realiza a substituição de uma palavra ou texto (alvo) por uma nova string em um arquivo.
Abre o arquivo usando o fileinput em modo de edição (inplace=True), o que permite que façamos a substituição de linhas diretamente no arquivo.
Itera pelas linhas do arquivo, substituindo o texto alvo pela nova string.
Imprime a linha modificada no arquivo.
Remove o arquivo de backup criado automaticamente pelo fileinput.
Função substituir_em_zip:

Essa função lida com o arquivo .zip fornecido, realizando a substituição de palavras em todos os arquivos presentes dentro do .zip.
Cria a pasta "versão2bk" caso ela não exista, onde serão armazenados os arquivos extraídos do .zip.
Extrai todos os arquivos do .zip para a pasta "versão2bk" usando o zipfile.ZipFile.
Itera por todos os arquivos extraídos e chama a função substituir_em_arquivo para realizar a substituição em cada arquivo individual.
Compacta os arquivos modificados de volta em um novo arquivo .zip chamado "versão2bk_modificado.zip".
Função substituir_em_arquivo_generico:

Esta função verifica se o arquivo fornecido é um arquivo .zip ou não.
Se for um arquivo .zip, chama a função substituir_em_zip, caso contrário, chama a função substituir_em_arquivo.
Permite que o script lide com diferentes tipos de arquivos.
Exemplo de uso:

O código solicita ao usuário o nome do arquivo, a palavra ou texto a ser substituído e a nova string de substituição.
Chama a função substituir_em_arquivo_generico com os parâmetros fornecidos pelo usuário.
O programa realiza as substituições no arquivo ou nos arquivos dentro do .zip e imprime mensagens informando sobre o andamento do processo.
Considerações finais:

O código cuida do cenário em que o arquivo .zip contém outros arquivos, permitindo que as substituições sejam realizadas em todos eles.
O backup é feito para garantir que o arquivo original não seja perdido ou modificado acidentalmente durante o processo de substituição.
O código é interativo e fácil de usar, permitindo que o usuário insira as informações necessárias durante a execução.
Lembre-se de que é sempre importante verificar e fazer backups dos arquivos importantes antes de executar qualquer código que faça alterações neles. Esse código é um exemplo básico de como realizar substituições em arquivos e .zip em Python, e pode ser adaptado para diferentes situações e necessidades específicas.
