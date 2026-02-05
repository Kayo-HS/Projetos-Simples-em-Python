CPF_String = input (str("Coloque seu CPF sem espaço ou pontos (EX:12345678900):"))

lista_num_string = list(CPF_String)

decimo_digito_str = CPF_String[9]
decimo_digito_int = int(decimo_digito_str)

decimo_primeiro_digito_str = CPF_String[10]
decimo_primeiro_digito_int = int(decimo_primeiro_digito_str)

soma_verificador = decimo_primeiro_digito_int + decimo_digito_int

print(f"{lista_num_string} o decimo número é {decimo_digito_int} e o decimo primeiro número é {decimo_primeiro_digito_int}")
print(f"A soma dos verificadores é {soma_verificador}")


