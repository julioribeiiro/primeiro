#include <stdio.h>

int main(){
	int faltou = 0;
	float nota_1, nota_2, nota_3, segunda, media, final;

	printf("Digite as 3 notas do aluno: ");
	scanf("%f, %f, %f", &nota_1, &nota_2, &nota_3);


	if (nota_1 < 0 || nota_2 < 0 || nota_3 < 0){
		printf("\nDigite a nota da segunda chamada do aluno: ");
		scanf("%f", &segunda);
		faltou = 1;
	}

	//------------CALCULO DE MEDIA CASO ALUNO TENHA FALTADO----
	if (faltou == 1){

		if (nota_1 < 0){
			media = (nota_2 + nota_3 + segunda) / 3;
			faltou++;
		}


		if (nota_2 < 0){
			media = (nota_1 + nota_3 + segunda) / 3;
			faltou++;
		}


		if (nota_3 < 0){
			media = (nota_1 + nota_2 + segunda) / 3;
			faltou++;
		}

	}

	if (faltou > 2){
		printf("\nAluno faltou mais de uma prova e esta reprovado!\n\n");
		return 0;
	}

	else if (faltou == 0){
		media = (nota_1 + nota_2 + nota_3) / 3;
	}




//----------------AVALIANDO SITUACAO DO ALUNO--------------
	if (media >= 7){
		printf("\nAluno aprovado por media\nMedia: %.2f", media);
	}

	else if (media < 7){
		printf("\nAluno nao passou por media\nMedia: %.2f\nDigite a nota da final: ", media);
		scanf("%f", &final);
		media = (media+final) / 2;
		if (media >= 5){
			printf("\nAluno aprovado na final!\nMedia: %.2f\n\n", media);
		}
		else{
			printf("\nAluno reprovado!\nMedia: %.2f\n\n", media);
		}
	}



return 0;





















}