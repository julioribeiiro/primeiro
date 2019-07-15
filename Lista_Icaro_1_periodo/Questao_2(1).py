"""
Um site exige que os usuários insiram nome de usuário e senha para se registrarem. Escreva um programa para verificar se a senha digitada pelos usuários é forte o suficiente.
A seguir estão os critérios para verificar a senha:

1. Pelo menos uma letra entre [a-z]
2. Pelo menos 1 número entre [0-9]
3. Pelo menos uma letra entre [A-Z]
4. Pelo menos 1 caractere de [$ # @]
5. Comprimento mínimo da senha: 6
6. Comprimento máximo da senha: 12

Seu programa deve aceitar uma sequência de senhas separadas por vírgula e as verificará de acordo com os critérios acima. As senhas que correspondem aos critérios devem ser impressas, separadas por uma vírgula.
Exemplo:
Se as seguintes senhas forem fornecidas como entrada para o programa:
ABd1234@1,a F1#,2w3E*,2We3345
Então, a saída do programa deve ser:
ABd1234@1
Aluno: Júlio César Ribeiro de Moraes
"""
def verifica(senha):
	maiusculo = 0
	minusculo = 0
	simbolo = 0
	numero = 0
	comprimento = 0
	if len(senha) >= 6 and len(senha) <= 12:
		comprimento = 1
		for i in range(len(senha)):
			if senha[i] == '$' or senha[i] == '#' or senha[i] == '@' or senha[i] == ' ':
				simbolo = 1
			elif senha[i].isupper() == True:
				maiusculo = 1
			elif senha[i].islower() == True:
				minusculo = 1
			elif senha[i].isdigit() == True:
				numero = 1
	if comprimento == 0:
		print("A senha {} possui numeros de caracteres invalidos".format(senha))
	elif simbolo == 0:
		print("A senha {} nao possui simbolos".format(senha))
	elif maiusculo == 0:
		print("A senha {} nao possui letras maiusculas".format(senha))
	elif minusculo == 0:
		print("A senha {} nao possui letras minusculas".format(senha))
	elif numero == 0:
		print("A senha {} nao possui numeros".format(senha))
	else:
		print("A senha {} eh uma senha valida".format(senha))

		





senhas = input("Digite as senhas separas por virgula: ")
senhas = senhas.split(',')

for i in range(len(senhas)):
	verifica(senhas[i])