/*
A entrada é composta de vários casos de teste. A primeira linha de cada
caso de teste contém dois números inteiros N e P , indicando, respectivamente,
o número de caixas e o número de pilhas (1 ≤ P ≤ N ≤ 1.000). As caixas são
numeradas seqüencialmente de 1 a N.

Cada uma das P linhas seguintes descreve uma pilha. Cada linha 
contém um inteiro Qi, indicando quantas caixas há na pilha i, 
seguido de um espaço em branco, seguido de uma lista de Qi números, 
que são os identificadores das caixas. Os elementos da lista são 
separados por um espaço em branco.

Todas as pilhas contêm pelo menos uma caixa, e todas as caixas 
aparecem exatamente uma vez na entrada. As caixas em cada pilha 
são listadas em ordem, da base até o topo da pilha. Todas as 
caixas têm o mesmo formato.

O final da entrada é indicado por N = P = 0.

A entrada deve ser lida da entrada padrão.

Entrada:
4 3
1 3
2 1 2
1 4
4 3
1 3
2 2 1
1 4
0 0

Saída:
2
0
*/

#include <stdio.h>
#include <stdlib.h>


int **aloca_matrix(int linhas, int colunas){
	int **matrix;
	int i;
	matrix = calloc(linhas+2, sizeof(int*));
	for(i=0; i<linhas+2; i++)
		matrix[i] = calloc(colunas+1, sizeof(int));

	return matrix;
}



int main(){
	int **matrix;
	int caixas;
	int pilhas;
	int n_caixas_na_pilha;
	int n_da_caixa = 0;
	int caixa_1_linha = 0;
	int caixa_1_coluna = 0;
	int acima_do_1 = 0;
	int lado_esquerdo = 0;
	int lado_direito = 0;
	int maior_pilha = 0;
	int i, j;


	scanf("%d", &caixas);
	scanf("%d", &pilhas);
	while(caixas != 0 && pilhas != 0){

		matrix = aloca_matrix(pilhas, caixas);

		for(i=1; i<=pilhas; i++){
			scanf("%d", &n_caixas_na_pilha);
			if (n_caixas_na_pilha > maior_pilha)
				maior_pilha = n_caixas_na_pilha;
			for(j=0; j<n_caixas_na_pilha; j++){
				scanf("%d", &n_da_caixa);
				matrix[i][j] = n_da_caixa;
				if (i == caixa_1_linha)
					acima_do_1++;
				if (n_da_caixa == 1){
					caixa_1_linha = i;
					caixa_1_coluna = j;
				}
			}
		}

//----------------RETIRANDO AS CAIXAS



//-------COM A COLUNA DO LIVRO1 VERIFICO QUAL LADO TEM MAIS LIVROS
		//------CIMA
		for(i=caixa_1_linha-1; i>=0; i--){
			if (matrix[i][caixa_1_coluna] == 0)
				break;
			for(j=caixa_1_coluna; j<=maior_pilha; j++){
				if (matrix[i][j] != 0){
					lado_esquerdo++;
				}
			}
		}


		//-----BAIXO
		for(i=caixa_1_linha+1; i<=pilhas; i++){
			if (matrix[i][caixa_1_coluna] == 0)
				break;
			for(j=caixa_1_coluna; j<=maior_pilha; j++){
				if (matrix[i][j] != 0)
					lado_direito++;
			}
		}

		if (lado_direito > lado_esquerdo){
			printf("%d\n", lado_esquerdo+acima_do_1);
		}
		
		else
			printf("%d\n", lado_direito+acima_do_1);
		
		free(matrix);
		lado_esquerdo = 0;
		lado_direito = 0;
		acima_do_1 = 0;
		maior_pilha = 0;
		n_da_caixa = 0;
		caixa_1_linha = 0;
		caixa_1_coluna = 0;


		scanf("%d", &caixas);
		scanf("%d", &pilhas);
	}


	return 0;

}