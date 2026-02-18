🇧🇷 [PT-BR] Validador de CPF em Python
📌 Sobre o Projeto

Este projeto é um validador de CPF desenvolvido em Python, criado como parte da disciplina Formação Profissional em Computação – UNIVESP.

O programa verifica se um CPF informado pelo usuário é válido, com base no cálculo oficial dos dois dígitos verificadores.

🚀 Funcionalidades

- Conversão de string para lista de inteiros

- Validação do primeiro dígito verificador

- Validação do segundo dígito verificador

- Tratamento de erros para entradas inválidas

- Interface simples via terminal

🧠 Como funciona a validação?

O CPF possui 11 dígitos:

- 9 primeiros números

- 2 dígitos verificadores

O algoritmo:

- Multiplica os 9 primeiros dígitos por seus respectivos índices.

- Soma os resultados.

- Calcula o resto da divisão por 11.

- Se o resto for maior ou igual a 10, considera apenas o último dígito.

- Compara o resultado com o dígito verificador.

- Repete o processo para o segundo dígito.

▶️ Como executar o projeto

- Certifique-se de ter o Python instalado (versão 3.x).

- Clone o repositório ou copie o código.

- Execute o arquivo:

      python nome_do_arquivo.py


- Digite o CPF sem pontos ou traços.

Exemplo:

    Para o CPF: 123.456.789-10
    Digite: 12345678910

⚠️ Observações

- O CPF deve ser digitado apenas com números.

- O programa realiza validação de formato básico (somente números).

- O código foi desenvolvido com foco educacional.

📚 Objetivo Acadêmico

Projeto desenvolvido para prática de:

- Estruturas de repetição

- Manipulação de listas

- Tratamento de exceções

- Funções em Python

- Lógica de validação matemática

🇺🇸 [EN-US] CPF Validator in Python
📌 About the Project

This project is a CPF validator developed in Python, created as part of the course Professional Training in Computing – UNIVESP.

The program verifies whether a CPF entered by the user is valid, based on the official check digit calculation algorithm.

🚀 Features

- String to integer list conversion

- First check digit validation

- Second check digit validation

- Error handling for invalid inputs

- Simple terminal-based interface

🧠 How does the validation work?

A CPF has 11 digits:

- First 9 digits

- 2 check digits

The algorithm:

- Multiplies the first 9 digits by their respective indexes.

- Sums the results.

- Calculates the remainder of division by 11.

- If the remainder is greater than or equal to 10, only the last digit is considered.

- Compares the result with the check digit.

- Repeats the process for the second digit.

▶️ How to run the project

- Make sure you have Python installed (version 3.x).

- Clone the repository or copy the code.

- Run the file:

      python filename.py


- Enter the CPF without dots or hyphens.

Example:

    For CPF: 123.456.789-10
    Type: 12345678910

⚠️ Notes

- The CPF must contain numbers only.

- The program performs basic format validation.

- The code was developed for educational purposes.
