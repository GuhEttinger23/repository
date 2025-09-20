sabores_disponiveis = [
    "chocolate", "morango", "cremoso", "baunilha", "limão", "abacaxi",
    "maracujá", "doce de leite", "coco", "prestígio", "nozes",
    "red velvet", "leite ninho", "trufado de chocolate", "frutas vermelhas"
]

massas_disponiveis = ["chocolate", "branca"]

doces_disponiveis = ["brigadeiro", "beijinho", "bicho de pé"]


def pedir_bolo():
    kilo = float(input("Digite quantos quilos de bolo: "))

    print("\nSabores disponíveis:")
    for sabor in sabores_disponiveis:
        print(f"- {sabor}")
    sabor = input("Digite o sabor do bolo: ").lower()
    if sabor not in sabores_disponiveis:
        print("Sabor inválido! Pedido cancelado.")
        return 0, None, None

    print("\nMassas disponíveis:")
    for massa in massas_disponiveis:
        print(f"- {massa}")
    massa = input("Digite a massa do bolo: ").lower()
    if massa not in massas_disponiveis:
        print("Massa inválida! Pedido cancelado.")
        return 0, None, None

    retirar = input("Digite se irá retirar ou deseja entrega (retirar/entrega): ").lower()
    frete = 0

    if retirar == "entrega":
        km = float(input("Digite a distância da entrega (em km): "))
        if 0 <= km <= 10:
            frete = 15
        elif 10 < km <= 20:
            frete = 30
        elif 20 < km <= 30:
            frete = 40
        else:
            print("Fora da área de entrega, será necessário retirar.")
            frete = 0

    valor = kilo * 90
    return valor + frete, sabor, massa


def pedir_doces():
    print("\nDoces disponíveis:")
    for doce in doces_disponiveis:
        print(f"- {doce}")
    doce = input("Digite o tipo de doce: ").lower()
    if doce not in doces_disponiveis:
        print("Doce inválido! Pedido cancelado.")
        return 0, None, 0

    quantidade = int(input("Digite a quantidade de CENTOS que deseja (1 cento = 100 doces): "))
    valor = quantidade * 150
    return valor, doce, quantidade


def menu():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Apenas bolo")
        print("2 - Apenas doces")
        print("3 - Bolo + doces")
        print("4 - Sair")

        escolha = input("Digite a opção: ")

        if escolha == "1":
            valor_bolo, sabor, massa = pedir_bolo()
            print(f"\nResumo do pedido:\n- Bolo: sabor {sabor}, massa {massa}, valor R$ {valor_bolo:.2f}")

        elif escolha == "2":
            valor_doces, doce, qtd = pedir_doces()
            print(f"\nResumo do pedido:\n- Doces: {qtd} cento(s) de {doce}, valor R$ {valor_doces:.2f}")

        elif escolha == "3":
            valor_bolo, sabor, massa = pedir_bolo()
            valor_doces, doce, qtd = pedir_doces()
            valor_total = valor_bolo + valor_doces
            print("\nResumo do pedido:")
            print(f"- Bolo: sabor {sabor}, massa {massa}, valor R$ {valor_bolo:.2f}")
            print(f"- Doces: {qtd} cento(s) de {doce}, valor R$ {valor_doces:.2f}")
            print(f"Valor total a pagar: R$ {valor_total:.2f}")

        elif escolha == "4":
            print("Saindo do sistema de pedidos. Obrigado!")
            break

        else:
            print("Opção inválida, tente novamente.")


# Executar o sistema
menu()
