## Sistema de Gerenciamento de Figurinhas - Copa 2026 ⚽🏆

Este projeto consiste em um sistema para gerenciamento, organização 
e troca de figurinhas da **Copa do Mundo de 2026**, desenvolvido como 
parte da disciplina de Estrutura de Dados da Fatec Rio Claro.

---

## 🛠️ Requisitos Técnicos Atendidos

Conforme as regras do projeto, não foram utilizadas estruturas prontas do Python
(como `list`, `dict` ou `deque`) para a construção do álbum ou das filas. 

Toda a manipulação de dados foi feita manualmente através de nós encadeados:
* `Álbum Principal`: implementado utilizando uma **Lista Encadeada Simples**.
* `Figurinhas Repetidas e Histórico`: implementados utilizando uma estrutura 
de **Fila FIFO (First-In, First-Out)** própria.

---

## 📦 Arquitetura do Projeto (Modularização)

Para facilitar o estudo, a manutenção do código e permitir entregas incrementais 
claras no GitHub, o projeto foi totalmente dividido em módulos independentes:

* `estruturas.py`: contém os moldes e definições básicas das entidades 
do sistema (`Figurinha`, `NodoLista` e `NodoFila`).
* `album.py`: gerencia a lógica da **Lista Encadeada** que representa o álbum 
principal (inserção, remoção, exibição e buscas por ID, jogador ou seleção).
* `filas.py`: contém a implementação da estrutura de **Fila FIFO** utilizada 
para armazenar as figurinhas repetidas e para gerenciar o histórico.
* `persistencia.py`: responsável por salvar e carregar os dados automaticamente em um arquivo 
de texto (`meu_album.txt`), garantindo que os dados não sejam perdidos ao fechar o programa.
* `main.py`: o arquivo central que une todos os módulos e roda o menu interativo no terminal.

---

## 🚀 Funcionalidades Principais Implementadas

1. **Gerenciamento do Álbum**: inserção de figurinhas, remoção e visualização do álbum completo.
2. **Progresso da Coleção**: cálculo em tempo real da porcentagem concluída do álbum.
3. **Controle de Repetidas**: armazenamento automático e contagem de figurinhas 
repetidas usando Fila FIFO.
4. **Sistema de Buscas**: busca de figurinhas por número (ID), por nome do jogador 
ou por seleção (país).
5. **Troca Automática**: simulação de propostas de troca, validando se o 
usuário já possui a figurinha e registrando a ação no **Histórico de Trocas**.
6. **Persistência de Dados**: carregamento automático ao iniciar e 
salvamento ao sair através de arquivo TXT.

---

## 🏃 Como Executar o Projeto

Certifique-se de ter todos os arquivos (`estruturas.py`, `album.py`, `filas.py`, 
`persistencia.py` e `main.py`) na mesma pasta. No terminal, execute:

```bash
python main.py
```