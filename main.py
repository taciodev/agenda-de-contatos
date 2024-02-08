
def add_new_contact(contact_list, contact_name, contact_phone, contact_email):
    ...


def view_all_contacts():
    ...


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
        ...
    elif option_chosen == "2":
        ...
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
