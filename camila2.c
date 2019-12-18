#include <stdio.h>
#include <stdlib.h>

//eu criei a estrutura pessoa (o num é o número que representa a pessoa na fila) e um ponteiro que aponta para a próxima pessoa da fila
struct pessoa {
    int num;
    struct pessoa *proximo; 
};

//eu criei a estrtura fila e criei os ponteiros que indica o início, o fim e o tamanho (len) da fila
struct fila {
    struct pessoa *inicio;
    struct pessoa *fim;
    int len;
};

//função main e to criando a variável (que é um ponteiro do tipo fila) e dizendo que o início e o fim apontam para o nada e o tamanho da fila é 0
int main() {
    struct fila *fila_ingressos;
    
    int num_total;
    int ident;
    int num_saida;
    struct pessoa *aux;
    //o ponteiro aux aponta para uma pessoa e vai auxiliar apontando para cada uma das pessoas e imprimindo os valores das pessoas na fila
    
    fila_ingressos = malloc(sizeof(struct fila));
    fila_ingressos->inicio = NULL;
    fila_ingressos->fim = NULL;
    fila_ingressos->len = 0;
    
    scanf("%d", &num_total);
    
    //criei um inteiro que começa em 0 e vai rodar enquanto ele for menor que o númrero total de pessoas na fila
    for(int i = 0; i<num_total; i++){
        scanf("%d", &ident);
        
        //criei uma pessoa para ser a primeira pessoa da fila mas ela não ta na fila ainda
        struct pessoa *novo;
        novo = malloc(sizeof(struct pessoa));
        novo->num = ident;
        
        //alocar um espaço para a primeira pessoa da fila
        //novo é a pessoa e eu to acessando o identificador dela na fila
        if(i==0){
         novo->proximo = NULL;
         fila_ingressos->inicio = novo;
         fila_ingressos->fim = novo;
         fila_ingressos->len++;
    
        }
        
        else{
        //o ponteiro "proximo" do antigo último elemento agora aponta para o novo elemento
        fila_ingressos->fim->proximo = novo;
        //o ponteiro fim vai agora apontar para o novo elemento da fila
        fila_ingressos->fim = novo;
        fila_ingressos->len++;
        novo->proximo = NULL;
        
        }
        
} 
        aux = fila_ingressos->inicio;
       // ponteiro auxiliar aponta para o início da fila
        
        
        for(int i = 0; i<fila_ingressos->len; i++){
            printf("%d  ", aux->num);
            aux = aux->proximo;
        }
        

        
        
    return 0;

    
}