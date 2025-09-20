# ================== GERENCIADOR DE TAREFAS ==================

# Lista global de tarefas
lista_tarefas = []

# Função para adicionar tarefas
def adc_tarefas(nome_tarefa: str, descricao_tarefa: str, prioridade_tarefa: int, categoria_tarefa: int):
    tarefa = {
        "nome": nome_tarefa,
        "descricao": descricao_tarefa,
        "prioridade": prioridade_tarefa,
        "categoria": categoria_tarefa,
        "situacao": False
    }
    lista_tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

# Função para listar tarefas
def listar_tarefas(lista_de_tarefas: list):
    if not lista_de_tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    for indice, dicionario in enumerate(lista_de_tarefas, start=1):
        print("-" * 40)
        print(f"Tarefa {indice}:")
        for chave, valor in dicionario.items():
            print(f"{chave}: {valor}")

# Função para marcar tarefa como concluída
def marcar_concluida(lista_tarefas: list):
    listar_tarefas(lista_tarefas)
    if not lista_tarefas:
        return
    try:
        concluir = int(input("Digite o número da tarefa que deseja concluir: ")) - 1
        if 0 <= concluir < len(lista_tarefas):
            lista_tarefas[concluir]["situacao"] = True
            print("Tarefa concluída com sucesso!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Digite um número válido!")

# Função para exibir tarefas por prioridade
def exibir_por_prioridade(prioridade: int):
    print(f"Tarefas com prioridade {prioridade}:")
    filtradas = [t for t in lista_tarefas if t["prioridade"] == prioridade]
    listar_tarefas(filtradas)

# Função para exibir tarefas por categoria
def exibir_por_categoria(categoria: int):
    print(f"Tarefas da categoria {categoria}:")
    filtradas = [t for t in lista_tarefas if t["categoria"] == categoria]
    listar_tarefas(filtradas)

# -------------------- MENU PRINCIPAL --------------------
def menu():
    while True:
        print("""
        ===== GERENCIADOR DE TAREFAS =====
        1 - Adicionar tarefa
        2 - Listar todas as tarefas
        3 - Marcar tarefa como concluída
        4 - Exibir tarefas por prioridade
        5 - Exibir tarefas por categoria
        6 - Sair
        """)
        
        opcao = input(" Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome da tarefa: ")
            descricao = input("Descrição: ")
            prioridade = int(input("Prioridade (1- Alta, 2- Média, 3- Baixa): "))
            categoria = int(input("Categoria (1- Profissional, 2- Pessoal, 3- Financeira): "))
            adc_tarefas(nome, descricao, prioridade, categoria)
        
        elif opcao == "2":
            listar_tarefas(lista_tarefas)
        
        elif opcao == "3":
            marcar_concluida(lista_tarefas)
        
        elif opcao == "4":
            prioridade = int(input("Digite a prioridade (1, 2 ou 3): "))
            exibir_por_prioridade(prioridade)
        
        elif opcao == "5":
            categoria = int(input("Digite a categoria (1, 2 ou 3): "))
            exibir_por_categoria(categoria)
        
        elif opcao == "6":
            print("Saindo do programa... Até a próxima!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Inicia o programa
menu()
