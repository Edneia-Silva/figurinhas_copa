from estruturas import Figurinha
from colecoes import Album, Fila
import persistencia

def menu():
    meu_album = Album()
    minhas_repetidas = Fila()
    historico_trocas = Fila()
    
    # Carrega os dados usando o módulo de persistência
    persistencia.carregar_do_arquivo(meu_album, minhas_repetidas)

    while True:
        print("\n==================================")
        print("  GERENCIADOR DE FIGURINHAS DA COPA  ")
        print("==================================")
        print("1. Inserir nova figurinha")
        print("2. Ver álbum completo")
        print("3. Ver porcentagem concluída")
        print("4. Ver figurinhas repetidas")
        print("5. Buscar figurinha")
        print("6. Simular proposta de troca")
        print("7. Ver histórico de trocas")
        print("8. Remover figurinha do álbum")
        print("9. Sair (salvar automaticamente)")
        print("==================================")
        
        opcao = input("Escolha uma opção (1-9): ").strip()

        if opcao == "1":
            print("\n--- CADASTRAR FIGURINHA ---")
            try:
                id_fig = int(input("Número (ID): "))
                nome = input("Nome do Jogador: ").strip()
                pais = input("Seleção (País): ").strip()
                posicao = input("Posição (Ex: Goleiro): ").strip()
                raridade = input("Raridade (Comum/Rara): ").strip()
                
                if not nome or not pais:
                    print("\n[ERRO] Nome e Seleção são obrigatórios!")
                    continue
                
                nova_fig = Figurinha(id_fig, nome, pais, posicao, raridade)
                if meu_album.adicionar(nova_fig):
                    print(f"\n[OK] {nome} foi colado com sucesso no álbum!")
                else:
                    minhas_repetidas.enqueue(nova_fig)
                    print(f"\n[REPETIDA] Enviada para a fila de repetidas!")
            except ValueError:
                print("\n[ERRO] O ID precisa ser um número inteiro!")

        elif opcao == "2":
            meu_album.exibir_album()

        elif opcao == "3":
            print(f"\nProgresso atual: {meu_album.calcular_porcentagem()}% concluído.")

        elif opcao == "4":
            print(f"\nTotal de repetidas: {minhas_repetidas.contar_elementos()}")
            minhas_repetidas.exibir_fila()

        elif opcao == "5":
            print("\nComo deseja buscar?")
            print("1. Por número (ID)")
            print("2. Por nome do jogador")
            print("3. Por seleção")
            sub_op = input("Opção: ").strip()
            
            if sub_op == "1":
                try:
                    id_b = int(input("Digite o ID: "))
                    f = meu_album.buscar_por_id(id_b)
                    if f:
                        print(f"\nAchou! {f.nome} | {f.pais}")
                    else:
                        print("\nFigurinha não encontrada.")
                except ValueError:
                    print("ID inválido.")
            elif sub_op == "2":
                nome_b = input("Nome do jogador: ")
                meu_album.buscar_por_jogador(nome_b)
            elif sub_op == "3":
                pais_b = input("Nome da seleção: ")
                meu_album.buscar_por_selecao(pais_b)

        elif opcao == "6":
            print("\n--- SIMULAR TROCA ---")
            oferecida = minhas_repetidas.peek()
            if oferecida is None:
                print("Você não tem repetidas para trocar.")
                continue
                
            print(f"Você oferece: {oferecida.nome} ({oferecida.pais})")
            print("Dados da figurinha que o amigo vai te dar:")
            try:
                id_t = int(input("ID da figurinha do amigo: "))
                nome_t = input("Nome do jogador do amigo: ")
                pais_t = input("Seleção do amigo: ")
                
                if meu_album.buscar_por_id(id_t) is not None:
                    print("\n[RECUSADA] Você já tem essa figurinha no álbum.")
                else:
                    minhas_repetidas.dequeue()
                    nova_amigo = Figurinha(id_t, nome_t, pais_t, "Desconhecida", "Comum")
                    meu_album.adicionar(nova_amigo)
                    
                    texto_troca = Figurinha(0, f"Deu {oferecida.nome} e recebeu {nome_t}", "-", "-", "-")
                    historico_trocas.enqueue(texto_troca)
                    print(f"\n[SUCESSO] Troca realizada!")
            except ValueError:
                print("Dados inválidos.")

        elif opcao == "7":
            print("\n--- HISTÓRICO DE TROCAS REALIZADAS ---")
            historico_trocas.exibir_fila()

        elif opcao == "8":
            try:
                id_r = int(input("Digite o ID para remover: "))
                if meu_album.remover(id_r):
                    print("\nFigurinha removida.")
                else:
                    print("\nNão encontrada.")
            except ValueError:
                print("ID inválido.")

        elif opcao == "9":
            # Salva os dados chamando a função do módulo correspondente
            persistencia.salvar_no_arquivo(meu_album, minhas_repetidas)
            print("\nDados salvos com sucesso! Saindo do sistema... Até logo!")
            break
        else:
            print("\n[OPÇÃO INVÁLIDA] Escolha um número de 1 a 9.")

if __name__ == "__main__":
    menu()