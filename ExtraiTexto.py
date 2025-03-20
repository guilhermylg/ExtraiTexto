import pdfplumber

# Caminho para o arquivo PDF
pdf_path = ""
txt_path = "textoPDF.txt"  # Caminho para o arquivo de saída

# Abrir o PDF e extrair todas as páginas
with pdfplumber.open(pdf_path) as pdf:
    all_text = ""  # Variável para armazenar todo o texto
    
    for page in pdf.pages:
        text = page.extract_text()
        if text:  #adiciona texto se houver conteúdo extraído
            all_text += text + "\n\n"  #Adiciona um espaçamento entre páginas

# Salvar todo o texto extraído em um arquivo TXT
with open(txt_path, mode="w", encoding="utf-8") as file:
    file.write(all_text)

print(f"Texto extraído salvo em {txt_path}")
