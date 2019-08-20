'''
QUESTAO 14

URL VALIDA

Para o propósito desta questão, uma URL válida é definida da seguinte forma:
● Começa com o string do protocolo: “http://”
● Após o protocolo, o URL deve conter um nome de domínio. O nome de domínio
consiste em uma série de Strings separadas por pontos. Um nome de domínio deve
conter pelo menos duas Strings separadas por um único ponto, mas pode conter mais
de duas. Por exemplo:
http://www.cesar.org.br # válida
http://cesar.school # válida
http://cesar # inválida
http://portalacademico.cesar.edu.br # válida
Sua função deve aceitar uma URL de teste como ARGUMENTO (String) e RETORNAR um
valor de status (booleano). Sua função não deve pedir ao usuário para fornecer qualquer
entrada. Veja um exemplo de programa que usa sua função:
print ( valid_url("http://www.cesar.edu") ) # True
print ( valid_url("http://files.cesar.edu") ) # True
print ( valid_url("http://www.myweb.cesar.edu") ) # True

'''

def url_valida(link):
	if link[:7] == "http://":
		link = link.split('.')
		if len(link) >= 2:
			return True
		else:
			return False
	else:
		return False


print(url_valida('http://cesar.school'))


