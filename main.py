import re


def validate_contact_email(contact_email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    is_compatible = re.search(pattern, contact_email)
    if is_compatible is None:
        return False

    return True


def validate_contact_phone(contact_phone):
    pattern = r"^\d{11}$"
    is_compatible = re.search(pattern, contact_phone)
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


def update_contact():
    ...


def remove_contact():
    ...


def favorite_contact():
    ...


contacts = []

# {
#     "name": String, # EXAMPLE - "Taciano"
#     "telephone": Inteiro, # EXAMPLE - 71988963996
#     "email": String, # EXAMPLE - "taciano@gmail.com"
#     "favorite": Boolean, # EXAMPLE - False
# }

while True:
    print("\n***************************************************")
    print("*               Agenda de Contatos                *")
    print("*-------------------------------------------------*")
    print("* 1. Adicionar Novo Contato                       *")
    print("* 2. Ver Todos os Contatos                        *")
    print("* 3. Atualizar Contato                            *")
    print("* 4. Remover Contato                              *")
    print("* 5. Marcar Contato como Favorito                 *")
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
        ...
    elif option_chosen == "4":
        ...
    elif option_chosen == "5":
        ...
    elif option_chosen == "6":
        print("Saindo...")
        break
    else:
        print("\n⚠️ OPÇÃO INVÁLIDA. POR FAVOR, ESCOLHA UMA OPÇÃO VÁLIDA. ⚠️\n")
