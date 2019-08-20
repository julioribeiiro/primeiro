/*
Receber um vetor com 10 numeros e imprimir
a maior sequencia de soma.
Ex:
Entrada: [1, 0, -5, 3, 2, 1, 7, -2, 3, 10]
Saida: [3, 2, 1, 7, -2, 3, 10]


Forma de solucao:
Pegar o primeiro elemento e somar todos os n elementos subsequentes
depois somamos apenas n-1 elementos subsequentes, ate somarmos n-n elementos

sempre verificando se a soma supera a maior_soma.

fazer esta mesma verificacao de 0 / n, e 0+1 / n ate chegarmos em n / n.

criar variaveis de inicio e fim de sequencia

*/

#include <stdio.h>

int main(){

	int tamanho_matriz = 10;
	int vetor[] = {1, 0, -5, 3, 2, 1, 7, -2, -30, 10};
	int inicio, final, somador, inicio_maior, final_maior, i;
	int soma = 0;
	int maior_soma = 0;


	for(inicio=0; inicio<tamanho_matriz; inicio++){//-----COMECA VERIFICANDO A MAIOR SOMA A PARTIR DO PRIMEIRO ELEMENTO
		for(final= tamanho_matriz-1; final>inicio-1; final--){//-----COMECA VERIFICANDO A MAIOR SEQUENCIA DO INDICE INICIAL ATE O FINAL DEPOIS EH RETIRADO 1 DO FINAL E VERIFICA-SE DENOVO A SOMA
			for(somador=inicio; somador<final+1; somador++){
				soma += vetor[somador];

		}


		//VERIFICA SE A SOMA DA SEQUENCIA INICIO ATE FIM EH MAIOR DO QUE A MAIOR SOMA ATE O MOMENTO
		if (soma > maior_soma){
			maior_soma = soma;
			inicio_maior = inicio;
			final_maior = final; //INDICE DO INICIO E DO FIM EH SALVO JUNTO COM A MAIOR SOMA ANTES DE SER INCREMENTADO
			}
		soma = 0;
		}



	}
	printf("Maior Soma: %d\nInicio:%d\nFinal:%d\n", maior_soma, inicio_maior, final_maior);
	printf("Sequencia maior: \n");
	for(i=inicio_maior; i<final_maior+1; i++){
		printf("%d   ", vetor[i]);
	}







printf("\n\n\n");
return 0;	
}
