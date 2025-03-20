Extração de Texto de um PDF com pdfplumber

Este repositório contém um script em Python que utiliza a biblioteca pdfplumber para extrair texto de um arquivo PDF e salvá-lo em um arquivo de texto (.txt).

Descrição do Código

O script executa as seguintes etapas:

Importação da Biblioteca:

Importa pdfplumber para manipular arquivos PDF.

Definição dos Caminhos dos Arquivos:

pdf_path: Caminho do arquivo PDF de entrada.

txt_path: Caminho do arquivo de saída onde o texto extraído será salvo.

Abertura e Extração do Texto do PDF:

Abre o arquivo PDF usando pdfplumber.open(pdf_path).

Inicializa uma variável all_text para armazenar o conteúdo extraído.

Percorre todas as páginas do PDF e extrai o texto de cada uma.

Se houver conteúdo extraído, adiciona-o à variável all_text, separando as páginas com duas quebras de linha (\n\n).

Salvamento do Texto Extraído:

Abre um arquivo .txt em modo de escrita ("w") com codificação UTF-8.

Escreve todo o texto extraído no arquivo de saída.

Mensagem de Conclusão:

Exibe no terminal a mensagem informando que o texto foi salvo com sucesso.

Requisitos

Para executar este código, certifique-se de ter o Python instalado e a biblioteca pdfplumber instalada. Você pode instalar a biblioteca com o seguinte comando:

Como Usar

Substitua pdf_path pelo caminho do arquivo PDF que deseja processar.

Execute o script em um ambiente Python.

O texto extraído será salvo no arquivo especificado em txt_path.

Exemplo de Uso

Isso gerará um arquivo textoPDF.txt contendo todo o conteúdo textual do PDF processado.
