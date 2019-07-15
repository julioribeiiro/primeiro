"""
Crie uma implementação da cifra rotacional, às vezes também chamada de cifra de César. A cifra de César é uma simples cifra de deslocamento
que se baseia na transposição de todas as letras do alfabeto usando uma chave inteira entre 0 e 26. O uso da chave 0 ou 26 sempre produzirá a mesma saída devido à aritmética modular.
A letra é deslocada para tantos valores quanto o valor da chave.

A notação geral para cifras rotacionais é ROT + <chave>. A cifra rotacional mais comumente usada é a ROT13.

Um ROT13 no alfabeto latino seria o seguinte:
Normal: abcdefghijklmnopqrstuvwxyz
Cifrado: nopqrstuvwxyzabcdefghijklm

Exemplos:
Entrada: ROT5 omg
Saída: trl
Entrada: ROT0 c
Saída: c
Entrada: ROT26 Cool
Saída: Cool
Entrada: ROT13 The quick brown fox jumps over the lazy dog.
Saída: Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
Entrada: ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
Saída: The quick brown fox jumps over the lazy dog.

Se um valor de entrada inválido for digitado, a seguinte mensagem deve ser impressa: 'Erro'.
Entradas inválidas podem ser entradas que contém códigos de rotações inválidos ou mensagens contendo caracteres que não estão no alfabeto.
Exemplos:
Entrada: RARA abc Saída: Erro
Entrada: ROT5 c99 Saída: Erro

As entradas devem ser sempre compostas por ROT + <chave> + ' ' + 'mensagem', ou seja, a cifra rotacional e a mensagem a ser cifrada separados por vírgula.

Aluno: Júlio César Ribeiro de Moraes
"""
alfabeto = "abcdefghijklmnopqrstuvwxyz"

#indice = alfabeto.find("t")

entrada = input('Digite a entrada no formato ROT<chave> "texto": ')
entrada_aux = str()
i=0


while i != len(entrada):
	if entrada[i] != ' ':
		entrada_aux += entrada[i]
	i += 1
print(entrada_aux)


saida = str()

espaco = ' '

#----------VERIFICAÇÃO DA ENTRADA---------------------------

if entrada[:3] != "ROT":
	print("Erro 1")

elif entrada[3].isalnum() == False:
	print("Erro 2 ")

elif entrada[4] != ' ' and entrada[4].isalnum() == False:
	print("Erro 3", entrada[4])

elif entrada[4] == " " and entrada_aux[4:].isalpha() == False:
	print("Erro 4")

elif entrada[5] == " " and entrada_aux[5:].isalpha() == False:
	print("Erro 5")

else:
	numero = str()
	numero = numero+entrada[3]
	tamanho = len(entrada)
	i = 5
	if entrada[4] != ' ':
		numero = numero+entrada[4]
		i = 6
	numero = int(numero)
	
	while i != tamanho:
		if entrada[i] != ' ':
			posicao = alfabeto.find(entrada[i].lower())
			if posicao + numero > 25:
				saida = saida+alfabeto[posicao + numero - 26]
			else:
				saida = saida+alfabeto[posicao + numero]
		else:
			saida = saida + ' '
		i += 1

print(saida)

