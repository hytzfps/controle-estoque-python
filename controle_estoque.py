# Sistema de Controle de Estoque
# Projeto para iniciantes em Python

produtos = []

while True:

    print("\n====== MENU ======")
    print("1 - Adicionar produto")
    print("2 - Atualizar produto")
    print("3 - Excluir produto")
    print("4 - Visualizar estoque")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    # -------- ADICIONAR PRODUTO --------
    if opcao == "1":
        nome = input("Digite o nome do produto: ")

        if nome == "":
            print("O nome não pode ficar vazio.")
        else:
            try:
                preco = float(input("Digite o preço do produto: "))
                quantidade = int(input("Digite a quantidade: "))

                produto = {
                    "nome": nome,
                    "preco": preco,
                    "quantidade": quantidade
                }

                produtos.append(produto)
                print("Produto cadastrado com sucesso!")

            except:
                print("Erro: Digite apenas números no preço e quantidade.")

    # -------- ATUALIZAR PRODUTO --------
    elif opcao == "2":
        nome_busca = input("Digite o nome do produto para atualizar: ")
        encontrado = False

        for produto in produtos:
            if produto["nome"].lower() == nome_busca.lower():
                try:
                    novo_preco = float(input("Digite o novo preço: "))
                    nova_quantidade = int(input("Digite a nova quantidade: "))

                    produto["preco"] = novo_preco
                    produto["quantidade"] = nova_quantidade

                    print("Produto atualizado com sucesso!")
                    encontrado = True
                    break
                except:
                    print("Erro: valor inválido.")

        if encontrado == False:
            print("Produto não encontrado.")

    # -------- EXCLUIR PRODUTO --------
    elif opcao == "3":
        nome_busca = input("Digite o nome do produto para excluir: ")
        encontrado = False

        for produto in produtos:
            if produto["nome"].lower() == nome_busca.lower():
                produtos.remove(produto)
                print("Produto excluído com sucesso!")
                encontrado = True
                break

        if encontrado == False:
            print("Produto não encontrado.")

    # -------- VISUALIZAR ESTOQUE --------
    elif opcao == "4":
        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")
        else:
            print("\n--- ESTOQUE ---")
            for produto in produtos:
                print("Nome:", produto["nome"])
                print("Preço: R$", produto["preco"])
                print("Quantidade:", produto["quantidade"])
                print("----------------")

    # -------- SAIR DO SISTEMA --------
    elif opcao == "5":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
