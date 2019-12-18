#include <stdio.h>
#include <string.h>

void anagrama(char *pont1,char *pont2, int len1)
{
  int i;
  int j;
  int cont=0;
      for(i=0; i<len1;i++)
      {
        for(j=0;j<len1;j++)
        {
          if(pont1[i]==pont2[j])
          {
            cont++;
            pont1[i]= '1';
            pont2[j]= '6';
          }

        }
      }
      if (cont==len1)
        {
          printf("1\n");
        }
      else
        printf("0\n");
}


int main (int argc, char *argv[])
{
    char *pont1;
    char *pont2;

    pont1 = argv[1] ;
    pont2 = argv[2] ;
    int len1;
    int len2;

    if (argc<3)
    {
        return -1;
    }
    
    else{
        len1 = strlen(argv[1]);
        len2 = strlen(argv[2]);
        
        if (len1!=len2)
        {
            printf("0");
        }
        else
        {
          anagrama(argv[1],argv[2],len1);   
        }
        
        
    }
}