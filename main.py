from re import search


def validate_contact_email(contact_email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    is_compatible = search(pattern, contact_email)
    if is_compatible is None:
        return False

    return True


def validate_contact_phone(contact_phone):
    pattern = r"^\d{11}$"
    is_compatible = search(pattern, contact_phone)
    if is_compatible is None:
        return False

    return True


def add_new_contact(contact_list, contact_name, contact_phone, contact_email):
    contact = {"name": contact_name,
               "telephone": contact_phone, "email": contact_email, "favorite": False}
    contact_list.append(contact)


def view_all_contacts(contact_list):
    print("\nLISTA DE CONTATOS:\n")
    print("+------+----------------------+----------------------+----------------------+----------------------+")
    print("|  #   |        Nome          |       Telefone       |         Email        |      Favorito        |")
    print("+------+----------------------+----------------------+----------------------+----------------------+")
    for idx, contact in enumerate(contact_list, start=1):
        favorite_mark = "★" if contact["favorite"] else " "
        print(
            f"| {idx:<4} | {contact['name']:<20} | {contact['telephone']:<20} | {contact['email']:^20} | {favorite_mark:<20} |")
    print("+------+----------------------+----------------------+----------------------+----------------------+")


def update_contact(contact_list, contact_index, new_contact_phone, new_contact_email):
    try:
        adjusted_contact_index = int(contact_index) - 1
        contact = contact_list[adjusted_contact_index]

        contact["telephone"] = new_contact_phone
        contact["email"] = new_contact_email
    except IndexError:
        print("\n⚠️ OOOPS! ALGO DEU ERRADO AO ACESSAR UM ÍNDICE NA LISTA. POR FAVOR, VERIFIQUE SUA ENTRADA E TENTE NOVAMENTE. ⚠️\n")
    except ValueError:
        print("\n⚠️ OOOPS! HOUVE UM PROBLEMA AO TENTAR CONVERTER UM VALOR. VERIFIQUE SUA ENTRADA E TENTE NOVAMENTE. ⚠️\n")


def remove_contact(contact_list, contact_index):
    try:
        adjusted_contact_index = int(contact_index) - 1
        contact = contact_list[adjusted_contact_index]

        contact_list.remove(contact)
    except IndexError:
        print("\n⚠️ OOOPS! ALGO DEU ERRADO AO ACESSAR UM ÍNDICE NA LISTA. POR FAVOR, VERIFIQUE SUA ENTRADA E TENTE NOVAMENTE. ⚠️\n")


def favorite_contact(contact_list, contact_index):
    try:
        adjusted_contact_index = int(contact_index) - 1
        contact = contact_list[adjusted_contact_index]
        contact["favorite"] = not contact["favorite"]
    except IndexError:
        print("\n⚠️ OOOPS! ALGO DEU ERRADO AO ACESSAR UM ÍNDICE NA LISTA. POR FAVOR, VERIFIQUE SUA ENTRADA E TENTE NOVAMENTE. ⚠️\n")


contacts = []

while True:
    print("\n***************************************************")
    print("*               Agenda de Contatos                *")
    print("*-------------------------------------------------*")
    print("* 1. Adicionar Novo Contato                       *")
    print("* 2. Ver Todos os Contatos                        *")
    print("* 3. Atualizar Contato                            *")
    print("* 4. Remover Contato                              *")
    print("* 5. Favoritar ou Desfavoritar Contato             *")
    print("* 6. Sair                                         *")
    print("***************************************************")

    option_chosen = input("\nDigite sua escolha: ")

    if option_chosen == "1":
        contact_name = input(
            "Digite o nome do contato: ")
        contact_phone = input(
            "Digite o número do contato: ")
        contact_email = input(
            "Digite o email do contato: ")

        is_email_valid = validate_contact_email(contact_email)
        is_phone_valid = validate_contact_phone(contact_phone)
        if is_email_valid and is_phone_valid:
            add_new_contact(contacts, contact_name,
                            contact_phone, contact_email)
        else:
            print(
                "\n⚠️ INFORMAÇÃO INVÁLIDA. POR FAVOR, INSIRA UM TELEFONE OU E-MAIL VÁLIDO. ⚠️\n")

    elif option_chosen == "2":
        view_all_contacts(contacts)

    elif option_chosen == "3":
        contact_index = input(
            "Digite o índice do contato que você deseja atualizar na sua agenda: ")
        new_contact_phone = input(
            "Digite o novo número do contato: ")
        new_contact_email = input(
            "Digite o novo email do contato: ")

        update_contact(contacts, contact_index,
                       new_contact_phone, new_contact_email)

    elif option_chosen == "4":
        contact_index = input(
            "Digite o índice do contato que você deseja apagar da sua agenda: ")

        remove_contact(contacts, contact_index)

    elif option_chosen == "5":
        contact_index = input(
            "Digite o índice do contato que você deseja favoritar da sua agenda: ")

        favorite_contact(contacts, contact_index)

    elif option_chosen == "6":
        print("Saindo...")
        break

    else:
        print("\n⚠️ OPÇÃO INVÁLIDA. POR FAVOR, ESCOLHA UMA OPÇÃO VÁLIDA. ⚠️\n")
