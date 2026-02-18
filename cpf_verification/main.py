def str_to_int(cpf):
    cpf_number_list = []
    for letter in cpf:
        cpf_number = int(letter)
        cpf_number_list.append(cpf_number)

    print(cpf_number_list)
    
    return cpf_number_list

def take_the_last_digit(rest):
    rest_str = str(rest)
    length = len(rest_str)
    last_digit = rest_str[length - 1]
    last_digit = int(last_digit)

    return last_digit

def verify_first_digit(cpf_number_list):
    first_verify = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    slice_cpf = cpf_number_list[:9]
    verify_digit = cpf_number_list[9]
    result = 0
    for index, number_cpf in zip(first_verify, slice_cpf):
        result = result + (index*number_cpf)

    rest = result % 11

    if rest >= 10:
        rest = take_the_last_digit(rest)

    if rest == verify_digit:
        return True
    else:
        return False


def verify_second_digit(cpf_number_list):
    first_verify = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    slice_cpf = cpf_number_list[:10]
    verify_digit = cpf_number_list[10]
    result = 0
    for index, number_cpf in zip(first_verify, slice_cpf):
        result = result + (index*number_cpf)

    rest = result % 11

    if rest >= 10:
        rest = take_the_last_digit(rest)

    if rest == verify_digit:
        return True
    else:
        return False

print('''
      Bem vindo ao verificador de CPF
      Para iniciar basta digitar o seu CPF abaixo SEM traços e pontos
      Exemplo: Para o CPF: 123.456.789-10 digite: 12345678910
      ''')

try:
    cpf =  input("Digite o seu cpf: ")
    cpf = cpf.strip()
    

    for letter in cpf:
        int(letter)
    
    cpf_number_list = str_to_int(cpf)

    if verify_first_digit(cpf_number_list) and verify_second_digit(cpf_number_list):
        print("CPF válido!")
    else:
        print("CPF inválido!")

except:
    print('''
          Por favor digite apenas números como no exemplo abaixo
          Para o CPF: 123.456.789-10 digite: 12345678910
          ''')

