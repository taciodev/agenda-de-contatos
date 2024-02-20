# Desafio da Agenda de Contatos em Python

Este é um desafio prático para reforçar os conceitos aprendidos no módulo de introdução ao Python. A aplicação consiste em uma agenda para salvar, editar, deletar e marcar contatos como favoritos, com interface de linha de comando.

## Sobre o Desafio

Desenvolvemos uma aplicação de agenda que permite ao usuário realizar as seguintes operações:

- Adicionar um contato
- Visualizar a lista de contatos cadastrados
- Editar um contato
- Marcar/desmarcar um contato como favorito
- Ver uma lista de contatos favoritos
- Apagar um contato

## Como Usar

1. **Clonar o Repositório:**

## Como Usar

1. **Clonar o Repositório:**

   ```bash
   git clone https://github.com/taciodev/agenda-de-contatos.git
   ```

2. **Criar e Ativar um Ambiente Virtual (opcional):**

   ```bash
   python -m venv venv
   source venv/bin/activate # No Windows: venv\Scripts\activate
   ```

3. **Executar o Programa:**

   ```bash
   python main.py
   ```

4. **Interagir com a Aplicação:** Siga as instruções na interface de linha de comando para realizar as operações desejadas na agenda de contatos.

## Exemplos de Uso

- Adicionar um novo contato:

  ```python
  Digite sua escolha: 1
  Digite o nome do contato: João
  Digite o número do contato: 123456789
  Digite o email do contato: joao@example.com
  ```

  - Visualizar lista de contatos:

  ```python
  Digite sua escolha: 2
  ```

- Marcar um contato como favorito:

  ```python
  Digite sua escolha: 5
  Digite o índice do contato que você deseja favoritar da sua agenda: 1
  ```

## Contribuindo

Contribuições são bem-vindas! Se você tiver sugestões de melhorias, abra uma issue para discutir suas ideias ou envie um pull request com suas alterações.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT). Sinta-se à vontade para usar, modificar e distribuir o código conforme necessário.
