/*
1 - criar todas as combinacoes possiveis do primeiro numero da primeira lista
com todos os numeros da segunda lista

2 - salvar cada soma numa lista de duplas, onde a soma total fica salva na variavel
soma e os numeros utilizados ficam salvos num array de inteiros


input:
5 9
1 2 6 7

return:
6
2
6 7
1 2 6
7
1 2

5 + "6" = 11
9 + "2" = 11
5 + "7" = 12
9 + "1 + 2" = 12



2 listas serao criadas
uma para o primeiro numero e outra para o segundo numero contendo todas as combinacoes

cada elemento de uma lista ira conter
soma = (TOTAL DA SOMA DA COMBINACAO)
numeros = (NUMEROS USADOS NA COMBINACAO, SEM O PRIMEIRO ELEMENTO)





*/



#include <stdio.h>
#include <stdlib.h>


typedef struct lista{

	int soma;//12
	int numeros[100];//1, 2
	struct lista *proximo;

}tupla;


int main(){

	FILE* arquivo;
	char dados[100];
	int informacoes[2][100];
	int i = 0;
	int numeros = 0;
	int i_arquivo = 0;
	int soma = 0;


	tupla *primeiro = malloc(sizeof(tupla));
	tupla *segundo = malloc(sizeof(tupla));

	primeiro->proximo = NULL;
	segundo->proximo = NULL;

	arquivo = fopen("arquivo_dados.txt", "r");
	if (arquivo == NULL)
		return -1;

	//PEGANDO INFORMACOES DO ARQUIVO COMO STRING
	do{
		char c = fgetc(arquivo);

		if(feof(arquivo))
			break;

		dados[i] = c;
		i++;

	}while(1);

	i=0;
	int j=0;

	//TRANSFORMANDO STRING DE NUMEROS EM ARRAY DE INT
	while (dados[i] != '\0'){
		if(dados[i] == '\n'){
			j++;
			i_arquivo=0;
		}
		if (dados[i] != ' ' && dados[i] != '\n'){
			informacoes[j][i_arquivo] = atoi(&dados[i]);
			i_arquivo++;

			if (j==1)
				numeros++;//PEGANDO QUANTIDADE DE NUMEROS NA SEGUNDA LINHA
		}

		i++;
	}

	//1,2,6,7
	tupla *navegador = primeiro;
	int indice_numeros = 0;
	//COMECO DAS COMBINACOES AQUI PARA PRIMEIRO NUMERO
	for(int inicio = 0; inicio<numeros; inicio++){
		for(int final = inicio; final<numeros; final++){

			while(navegador->proximo != NULL)
				navegador = navegador->proximo;

			navegador->proximo = malloc(sizeof(tupla));
			navegador = navegador->proximo;
			navegador->proximo = NULL;


			for(int i =inicio; i<=final; i++){
				soma += informacoes[1][i];
				navegador->numeros[indice_numeros] = informacoes[1][i];
				indice_numeros++;
			}

			navegador->numeros[indice_numeros] = -99;
			soma += informacoes[0][0];
			navegador->soma = soma;
			indice_numeros = 0;//recomeca o indice dos numeros que sao salvos no array
			soma=0;//recomeca a soma para a proxima combinacao

		}
	}

	navegador = segundo;
	//COMECO DAS COMBINACOES AQUI PARA SEGUNDO NUMERO
	for(int inicio = 0; inicio<numeros; inicio++){
		for(int final = inicio; final<numeros; final++){

			while(navegador->proximo != NULL)
				navegador = navegador->proximo;

			navegador->proximo = malloc(sizeof(tupla));
			navegador = navegador->proximo;
			navegador->proximo = NULL;


			for(int i =inicio; i<=final; i++){
				soma += informacoes[1][i];
				navegador->numeros[indice_numeros] = informacoes[1][i];
				indice_numeros++;
			}

			navegador->numeros[indice_numeros] = -99;
			soma += informacoes[0][1];
			navegador->soma = soma;
			indice_numeros = 0;//recomeca o indice dos numeros que sao salvos no array
			soma=0;//recomeca a soma para a proxima combinacao

		}
	}


// PRINTS PRA TESTES

	navegador = primeiro->proximo;
	i=0;
	while(navegador != NULL){
		while(navegador->numeros[i] != -99){
			printf("%d ", navegador->numeros[i]);
			i++;
		}
		printf("\n");
		printf("SOMA: %d\n", navegador->soma);
		navegador = navegador->proximo;
		i=0;
	}

	printf("\n\n");


	navegador = segundo->proximo;
	i=0;
	while(navegador != NULL){
		while(navegador->numeros[i] != -99){
			printf("%d ", navegador->numeros[i]);
			i++;
		}
		printf("\n");
		printf("SOMA: %d\n", navegador->soma);
		navegador = navegador->proximo;
		i=0;
	}


	navegador = primeiro->proximo;
	tupla *navegador2 = segundo->proximo;
	i=0;

	while(navegador != NULL){
		while(navegador2 != NULL){

		if(navegador->soma == navegador2->soma){
			while(navegador->numeros[i] != -99){
				printf("%d ", navegador->numeros[i]);
				i++;
			}
			printf("\n");
			i=0;
			while(navegador2->numeros[i] != -99){
				printf("%d ", navegador2->numeros[i]);
				i++;
			}
			i=0;
			printf("\n");
		}
		navegador2 = navegador2->proximo;
		}
		navegador2 = segundo->proximo;
		navegador = navegador->proximo;
	}

	return 0;
}