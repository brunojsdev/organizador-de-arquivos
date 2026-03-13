# Organizador de Arquivos

## Descrição
Um script Python automatizado para organizar arquivos bagunçados em diretórios. Ele classifica os arquivos em subpastas específicas (Imagens, Documentos, Áudio, Vídeo, etc.) com base em suas extensões.

## Funcionalidades
- Separação automática de arquivos por categoria.
- Proteção contra sobrescrita: evita substituir arquivos com o mesmo nome adicionando um timestamp.
- Geração de relatório final detalhado com tempo de execução e contagem de itens movidos.

## Pré-requisitos
- Python 3.x
- Bibliotecas padrão do Python (os, shutil, pathlib, datetime, time). Nenhuma instalação externa é necessária.

## Como Usar
1. Execute o script no seu terminal ou IDE.
2. Digite o caminho da pasta que deseja organizar (ou pressione Enter para usar o diretório atual).
3. Confirme a operação digitando `s` quando solicitado.
