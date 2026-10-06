from sqlalchemy.orm import Session
from duasclasses import engine, Musica, Cantor

def inserir_musica():
    nome = input("Nome da musica: ")
    genero = input("Gênero: ")
    duracao = input("Duração: ")
    ano = int(input("Ano de lançamento: "))

    musica = Musica(
        nome=nome,
        genero=genero,
        duracao=duracao,
        ano_lancamento=ano
    )

    with Session(engine) as session:
        session.add(musica)
        session.commit()

    print("Musica cadastrada com sucesso!")

#inserir_musica()

def inserir_cantor():
    nome = input("Nome do cantor: ")
    ano = int(input("Ano de início da carreira: "))
    genero = input("Gênero musical: ")
    pais = input("País de origem: ")

    cantor = Cantor(
        nome=nome,
        ano_inicio_carreira=ano,
        genero_musical=genero,
        pais_origem=pais
    )

    with Session(engine) as session:
        session.add(cantor)
        session.commit()

    print("Cantor cadastrado!")

inserir_cantor()

def listar_musicas():
    with Session(engine) as session:
        musicas = session.scalars(select(Musica)).all()

        for musica in musicas:
            print("--------------------")
            print("ID:", musica.id)
            print("Nome:", musica.nome)
            print("Gênero:", musica.genero)
            print("Duração:", musica.duracao)
            print("Ano:", musica.ano_lancamento)


def listar_cantores():
    with Session(engine) as session:
        cantores = session.scalars(select(Cantor)).all()

        for cantor in cantores:
            print("--------------------")
            print("ID:", cantor.id)
            print("Nome:", cantor.nome)
            print("Início:", cantor.ano_inicio_carreira)
            print("Gênero:", cantor.genero_musical)
            print("País:", cantor.pais_origem)


def excluir_musica():
    id_musica = int(input("Digite o ID da música: "))

    with Session(engine) as session:
        musica = session.get(Musica, id_musica)

        if musica:
            session.delete(musica)
            session.commit()
            print("Música excluída!")
        else:
            print("Música não encontrada.")


def excluir_cantor():
    id_cantor = int(input("Digite o ID do cantor: "))

    with Session(engine) as session:
        cantor = session.get(Cantor, id_cantor)

        if cantor:
            session.delete(cantor)
            session.commit()
            print("Cantor excluído!")
        else:
            print("Cantor não encontrado.")


def inserir():
    print("\n1 - Música")
    print("2 - Cantor")

    opcao = input("Escolha: ")

    if opcao == "1":
        inserir_musica()
    elif opcao == "2":
        inserir_cantor()


def listar():
    print("\n1 - Músicas")
    print("2 - Cantores")

    opcao = input("Escolha: ")

    if opcao == "1":
        listar_musicas()
    elif opcao == "2":
        listar_cantores()


def excluir():
    print("\n1 - Música")
    print("2 - Cantor")

    opcao = input("Escolha: ")

    if opcao == "1":
        excluir_musica()
    elif opcao == "2":
        excluir_cantor()


def menu():
    while True:
        print("\n===== MENU =====")
        print("1 - Inserir")
        print("2 - Listar")
        print("3 - Excluir")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            excluir()
        elif opcao == "4":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida.")


menu()