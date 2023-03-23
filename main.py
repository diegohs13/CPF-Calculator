cpf_digitado = input("Digite seu CPF sem pontuações:")

digito_1 = int(cpf_digitado[0])
digito_2 = int(cpf_digitado[1])
digito_3 = int(cpf_digitado[2])
digito_4 = int(cpf_digitado[3])
digito_5 = int(cpf_digitado[4])
digito_6 = int(cpf_digitado[5])
digito_7 = int(cpf_digitado[6])
digito_8 = int(cpf_digitado[7])
digito_9 = int(cpf_digitado[8])
digito_10 = int(cpf_digitado[9])
digito_11 = int(cpf_digitado[10])

resto_primeiro_digito_verificador = (digito_1 * 10 + digito_2 * 9 + digito_3 * 8 + digito_4 * 7 + digito_5
                                     * 6 + digito_6 * 5 + digito_7 * 4 + digito_8 * 3 + digito_9 * 2) % 11

if resto_primeiro_digito_verificador == 0:
    primeiro_digito_verificador = 0

elif resto_primeiro_digito_verificador == 1:
    primeiro_digito_verificador = 0

else:
    primeiro_digito_verificador = 11 - resto_primeiro_digito_verificador

resto_segundo_digito_verificador = (digito_2 * 10 + digito_3 * 9 + digito_4 * 8 + digito_5 * 7 + digito_6
                                    * 6 + digito_7 * 5 + digito_8 * 4 + digito_9 * 3 +
                                    primeiro_digito_verificador * 2) % 11

if resto_segundo_digito_verificador == 0:
    segundo_digito_verificador = 0

elif resto_segundo_digito_verificador == 1:
    segundo_digito_verificador = 0

else:
    segundo_digito_verificador = 11 - resto_segundo_digito_verificador

if digito_10 == primeiro_digito_verificador and digito_11 == segundo_digito_verificador:
    print(f'Seu CPF é {True}')
else:
    print(f'Seu CPF é {False}')
