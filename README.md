# Organizador Automático de Ficheiros – Python

Este projeto é um script de automação desenvolvido em Python para resolver o problema comum de pastas desorganizadas, como a pasta de **Downloads**. O script identifica a extensão de cada ficheiro e move-o automaticamente para a categoria correta.

## 🚀 Funcionalidades

- **Classificação inteligente**: Agrupa ficheiros em categorias como Imagens, Documentos, Vídeos, Códigos, entre outras  
- **Gestão de duplicados**: Caso um ficheiro com o mesmo nome já exista na pasta de destino, o script renomeia o novo ficheiro com um timestamp, evitando perda de dados  
- **Relatório de execução**: Ao final do processo, apresenta um resumo com o tempo gasto, quantidade de ficheiros movidos e erros encontrados  
- **Segurança**: Ignora diretórios e o próprio script durante a execução para evitar loops ou erros de permissão  

## 🛠️ Tecnologias e Conceitos

Este script foi construído utilizando boas práticas de Python:

- **Programação Orientada a Objetos (POO)**: Organização do código em classes para maior modularidade  
- **Biblioteca `pathlib`**: Manipulação moderna e multiplataforma de caminhos de ficheiros  
- **Biblioteca `shutil`**: Operações de alto nível em ficheiros, como mover e copiar  
- **Tratamento de exceções**: Uso de blocos `try/except` para garantir que o script continue a execução mesmo diante de erros  

## 📂 Como Utilizar

1. Certifique-se de que tem o Python 3.x instalado  
2. Coloque o ficheiro `organizador_arquivos.py` na pasta que deseja organizar ou execute-o e informe o caminho completo da pasta quando solicitado  
3. Confirme a operação digitando `s` no terminal  
4. Veja a sua pasta ser organizada automaticamente  

## ⚙️ Configuração

As categorias podem ser personalizadas editando o dicionário `DIRETORIOS` dentro do ficheiro `.py`:

```python
DIRETORIOS = {
    "Imagens": [".jpg", ".png", ".webp"],
    "Trabalho": [".pdf", ".xlsx"]
}
```

Desenvolvido como um exemplo de automação eficiente para tarefas repetitivas.
