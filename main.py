import os
import shutil
from pathlib import Path
from datetime import datetime
import time

class OrganizadorArquivos:
    """
    Classe responsável por organizar arquivos de um diretório em subpastas
    baseadas em suas extensões.
    """

    # Configuração de extensões e suas respectivas pastas
    # Você pode adicionar ou remover extensões conforme sua necessidade
    DIRETORIOS = {
        "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
        "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv", ".pptx"],
        "Audio": [".mp3", ".wav", ".flac", ".aac"],
        "Video": [".mp4", ".mkv", ".mov", ".avi"],
        "Compactados": [".zip", ".rar", ".tar", ".gz", ".7z"],
        "Executaveis": [".exe", ".msi", ".bat", ".sh"],
        "Codigos": [".py", ".js", ".html", ".css", ".java", ".cpp"]
    }

    def __init__(self, diretorio_alvo):
        """
        Inicializa o organizador com o diretório alvo.
        """
        self.diretorio_alvo = Path(diretorio_alvo)
        if not self.diretorio_alvo.exists():
            raise FileNotFoundError(f"O diretório '{diretorio_alvo}' não foi encontrado.")
        
        self.log = [] # Armazena logs de operações
        self.stats = {"movidos": 0, "erros": 0, "ignorados": 0}

    def _obter_categoria(self, extensao):
        """
        Retorna a categoria (nome da pasta) baseada na extensão do arquivo.
        Retorna 'Outros' se a extensão não estiver mapeada.
        """
        extensao = extensao.lower()
        for categoria, extensoes in self.DIRETORIOS.items():
            if extensao in extensoes:
                return categoria
        return "Outros"

    def _log_msg(self, mensagem):
        """Adiciona uma mensagem ao log e imprime na tela com timestamp."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        msg_formatada = f"[{timestamp}] {mensagem}"
        print(msg_formatada)
        self.log.append(msg_formatada)

    def organizar(self):
        """
        Executa o processo de organização dos arquivos.
        """
        self._log_msg(f"Iniciando organização em: {self.diretorio_alvo}")
        start_time = time.time()

        # Itera sobre todos os itens no diretório
        for item in self.diretorio_alvo.iterdir():
            # Pula se for um diretório ou se for o próprio script (segurança)
            if item.is_dir() or item.name == os.path.basename(__file__):
                continue

            try:
                # Identifica categoria e define caminhos
                categoria = self._obter_categoria(item.suffix)
                pasta_destino = self.diretorio_alvo / categoria
                
                # Cria a pasta de destino se não existir
                pasta_destino.mkdir(exist_ok=True)
                
                # Caminho final do arquivo
                caminho_final = pasta_destino / item.name

                # Evita sobrescrever arquivos com o mesmo nome
                if caminho_final.exists():
                    timestamp = int(time.time())
                    novo_nome = f"{item.stem}_{timestamp}{item.suffix}"
                    caminho_final = pasta_destino / novo_nome
                    self._log_msg(f"Arquivo duplicado renomeado para: {novo_nome}")

                # Move o arquivo
                shutil.move(str(item), str(caminho_final))
                self.stats["movidos"] += 1
                self._log_msg(f"Movido: {item.name} -> {categoria}/")

            except Exception as e:
                self.stats["erros"] += 1
                self._log_msg(f"ERRO ao mover {item.name}: {str(e)}")

        end_time = time.time()
        self._gerar_relatorio(end_time - start_time)

    def _gerar_relatorio(self, duracao):
        """
        Exibe um relatório final da operação.
        """
        print("\n" + "="*40)
        print(f"RELATÓRIO DE EXECUÇÃO")
        print("="*40)
        print(f"Diretório: {self.diretorio_alvo}")
        print(f"Arquivos Movidos: {self.stats['movidos']}")
        print(f"Erros Encontrados: {self.stats['erros']}")
        print(f"Tempo de Execução: {duracao:.2f} segundos")
        print("="*40 + "\n")

# ==========================================
# EXECUÇÃO DO SCRIPT
# ==========================================
if __name__ == "__main__":
    # Para testar, você pode mudar o caminho abaixo para uma pasta real,
    # por exemplo: "C:/Users/SeuUsuario/Downloads" ou "./pasta_teste"
    
    # Usa o diretório atual onde o script está salvo como padrão
    caminho_padrao = "." 
    
    print("--- Automação de Organização de Arquivos ---")
    caminho_input = input(f"Digite o caminho da pasta para organizar (Pressione Enter para usar '{caminho_padrao}'): ").strip()
    
    pasta_alvo = caminho_input if caminho_input else caminho_padrao

    try:
        organizador = OrganizadorArquivos(pasta_alvo)
        
        confirmacao = input(f"Tem certeza que deseja organizar a pasta '{pasta_alvo}'? (s/n): ").lower()
        if confirmacao == 's':
            organizador.organizar()
        else:
            print("Operação cancelada pelo usuário.")
            
    except Exception as e:
        print(f"Erro fatal: {e}")