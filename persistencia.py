from estruturas import Figurinha
from album import Album, Fila  

def salvar_no_arquivo(album, repetidas):
    # Abre (ou cria) o arquivo "meu_album.txt" no modo de escrita ('w')
    with open("meu_album.txt", "w", encoding="utf-8") as f:        
        f.write("ALBUM\n")
        atual = album._cabeca
        
        while atual is not None:
            fig = atual.figurinha
            f.write(f"{fig.id},{fig.nome},{fig.pais},{fig.posicao},{fig.raridade}\n")
            atual = atual.proximo
            
        # Cria um cabeçalho identificando a seção das repetidas
        f.write("REPETIDAS\n")
        atual_rep = repetidas._inicio
        
        while atual_rep is not None:
            fig = atual_rep.figurinha
            f.write(f"{fig.id},{fig.nome},{fig.pais},{fig.posicao},{fig.raridade}\n")
            atual_rep = atual_rep.proximo

def carregar_do_arquivo(album, repetidas):
    try:
        # Abre o arquivo para leitura ('r')
        with open("meu_album.txt", "r", encoding="utf-8") as f:
            secao = None
            for linha in f:
                linha = linha.strip() # Remove quebras de linha (\n) e espaços invisíveis
                if linha == "ALBUM":
                    secao = "ALBUM"
                    continue
                elif linha == "REPETIDAS":
                    secao = "REPETIDAS"
                    continue
                
                if linha:
                    # Quebra a linha de texto pelas vírgulas, gerando uma lista com 5 partes
                    dados = linha.split(",")
                    if len(dados) == 5:
                        # Recria o objeto Figurinha a partir dos dados do texto lido
                        fig = Figurinha(dados[0], dados[1], dados[2], dados[3], dados[4])
                        # Insere o objeto de volta na estrutura correspondente indicada pela seção
                        if secao == "ALBUM":
                            album.adicionar(fig)
                        elif secao == "REPETIDAS":
                            repetidas.enqueue(fig)
    except FileNotFoundError:
        # Caso o arquivo txt não exista ainda (como na primeira execução), o programa ignora o erro e inicia vazio
        pass