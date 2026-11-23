from datetime import datetime

estoque = [
  
    {"nome": "Camiseta", "tamanho": "P", "cor": "Preta", "categoria": "Camisetas", "qtd": 20},
    {"nome": "Camiseta", "tamanho": "M", "cor": "Preta", "categoria": "Camisetas", "qtd": 25},
    {"nome": "Camiseta", "tamanho": "G", "cor": "Preta", "categoria": "Camisetas", "qtd": 23},
    {"nome": "Camiseta", "tamanho": "P", "cor": "Branca", "categoria": "Camisetas", "qtd": 15},
    {"nome": "Camiseta", "tamanho": "M", "cor": "Branca", "categoria": "Camisetas", "qtd": 17},
    {"nome": "Camiseta", "tamanho": "G", "cor": "Branca", "categoria": "Camisetas", "qtd": 5},
    
   
    {"nome": "Calça", "tamanho": "P", "cor": "Cinza", "categoria": "Calças", "qtd": 25},
    {"nome": "Calça", "tamanho": "M", "cor": "Cinza", "categoria": "Calças", "qtd": 20},
    {"nome": "Calça", "tamanho": "G", "cor": "Cinza", "categoria": "Calças", "qtd": 22},
    {"nome": "Calça", "tamanho": "P", "cor": "Preta", "categoria": "Calças", "qtd": 15},
    {"nome": "Calça", "tamanho": "M", "cor": "Preta", "categoria": "Calças", "qtd": 18},
    {"nome": "Calça", "tamanho": "G", "cor": "Preta", "categoria": "Calças", "qtd": 10},
    
    
    {"nome": "Jaqueta", "tamanho": "P", "cor": "Azul", "categoria": "Jaquetas", "qtd": 20},
    {"nome": "Jaqueta", "tamanho": "M", "cor": "Azul", "categoria": "Jaquetas", "qtd": 25},
    {"nome": "Jaqueta", "tamanho": "G", "cor": "Azul", "categoria": "Jaquetas", "qtd": 22},
    {"nome": "Jaqueta", "tamanho": "P", "cor": "Preta", "categoria": "Jaquetas", "qtd": 25},
    {"nome": "Jaqueta", "tamanho": "M", "cor": "Preta", "categoria": "Jaquetas", "qtd": 20},
    {"nome": "Jaqueta", "tamanho": "G", "cor": "Preta", "categoria": "Jaquetas", "qtd": 18}
    
]

def mostrar_menu():
    print("1 - Mostrar Estoque")
    print("2 - Cadastrar Nova Peça")
    print("3 - Adicionar Quantidade")
    print("4 - Remover Quantidade")
    print("5 - Buscar por Categoria")
    print("0 - Sair")


def mostrar_item(item):
    print(f"{item['nome']} | Tam: {item['tamanho']} | Cor: {item['cor']} | "
          f"Categoria: {item['categoria']} | Qtd: {item['qtd']}")

def buscar_item(nome, tamanho, cor):
    for item in estoque:
        if (item["nome"].lower() == nome.lower()
                and item["tamanho"].lower() == tamanho.lower()
                and item["cor"].lower() == cor.lower()):
            return item
    return None

     
def mostrar_estoque():
        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("---Estoque Atual " + data_atual + "---")

        if not estoque: 
            print("Estoque vazio.")
            return

        for item in estoque:
            mostrar_item(item)

        total = sum(item["qtd"] for item in estoque)
        print(f"\n Total de peças: {total}")

def cadastrar_peca():

     print("\nCADASTRAR PEÇA: ")
     nome = input("Nome da peça: ()").strip()
     if not nome:
        print("O nome não pode ficar vazio.")
        return
     
     tamanho = input("Tamanho: ").strip()
     cor = input("Cor: ").strip()
     categoria = input("categoria: [Calças/ Camisetas/ Jaquetas]").strip()

     if buscar_item(nome, tamanho, cor):
        print("Essa peça (mesmo nome, tamanho e cor) já está cadastrada!")
        return

     try:
        qtd = int(input("Quantidade: "))
     except ValueError:
        print("Quantidade inválida.")
        return

     if qtd <= 0:
         print("Quantidade inválida.")
         return

     
     estoque.append({
         "nome": nome,
         "tamanho": tamanho,
         "cor": cor,
         "categoria": categoria,
         "qtd": qtd
     })

     print(f"{nome} ({tamanho}/{cor}) cadastrada com {qtd} unidades!")


def adicionar_estoque():
    print("\nADICIONAR AO ESTOQUE: ")
    
    nome = input("Nome da Peça: ").strip()
    nome_item_procurado = [item for item in estoque if item["nome"].lower() == nome.lower()]

    if not nome_item_procurado:
        print(f"Nenhuma peça chamada '{nome}' está cadastrada.")
        return

    print(f"\nPeças disponíveis com o nome '{nome}':")
    for item in nome_item_procurado:
        print(f"  Tam: {item['tamanho']} | Cor: {item['cor']} | Qtd: {item['qtd']}")

    
    tamanho = input("Tamanho: ").strip()
    cor = input("Cor: ").strip()

    item = buscar_item(nome, tamanho, cor)

    if item is None:
        print("Essa combinação (nome/tamanho/cor) não foi encontrada.")
        return

    try:
        qtd_add = int(input(f"Quantidade a adicionar em {item['nome']} ({item['tamanho']}/{item['cor']}): "))
    except ValueError:
        print("Quantidade inválida.")
        return

    if qtd_add <= 0:
        print("Quantidade inválida.")
        return

    item["qtd"] += qtd_add
    print(f"{item['nome']} ({item['tamanho']}/{item['cor']}) agora tem {item['qtd']} unidades.")

def remover_do_estoque():
    print("\nREMOVER QUANTIDADE: ")
    nome = input("Nome da peça: ").strip()
    nome_item_procurado = [item for item in estoque if item["nome"].lower() == nome.lower()]

    if not nome_item_procurado:
        print(f"Nenhuma peça chamada '{nome}' está cadastrada.")
        return

    print(f"\nPeças disponíveis com o nome '{nome}':")
    for item in nome_item_procurado:
        print(f"  Tam: {item['tamanho']} | Cor: {item['cor']} | Qtd: {item['qtd']}")

    tamanho = input("Tamanho: ").strip()
    cor = input("Cor: ").strip()

    item = buscar_item(nome, tamanho, cor)
    if item is None:
        print("Peça não encontrada.")
        return

    try:
        qtd_rem = int(input(f"Quantidade a remover de {item['nome']} ({item['tamanho']}/{item['cor']}): "))
    except ValueError:
        print("Quantidade inválida.")
        return

    if qtd_rem <= 0:
        print("Quantidade inválida.")
        return

    if qtd_rem > item["qtd"]:
        print(f"Não é possível remover! Há somente {item['qtd']} unidades em estoque.")
        return

    item["qtd"] -= qtd_rem
    print(f"{item['nome']} ({item['tamanho']}/{item['cor']}) agora tem {item['qtd']} unidades.")


def buscar_por_categoria():
    print("\nBUSCAR POR CATEGORIA")
    print("CATEGORIAS: [Calças/ Camisetas/ Jaquetas]")
    categoria = input("Categoria: ").strip()

    encontrados = [item for item in estoque if item["categoria"].lower() == categoria.lower()]

    if not encontrados:
        print("Categoria não cadastrada.")
        return

    print(f"\nPeças em '{categoria}':")
    for item in encontrados:
        mostrar_item(item)


def main():

    print("--------------------------")
    print("---ESTOQUE DE UNIFORMES---")
    print("--------------------------")

    while True:

        print()
        mostrar_menu()

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            mostrar_estoque()
        elif opcao == "2":
            cadastrar_peca()
        elif opcao == "3":
            adicionar_estoque()
        elif opcao == "4":
            remover_do_estoque()
        elif opcao == "5":
            buscar_por_categoria()
        elif opcao == "0":
            print("Sistema Encerrado.")
            break
        else:
            print("Opção inválida.")
     
main()