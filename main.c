#include <stdio.h>
int main()
{
    int num1, num2;
    char op;
    scanf("%d", &num1);
    scanf("%d", &num2);
     scanf(" %c", &op);
    switch(op)
    {
        case '+':
        printf("result :%d\n", num1 + num2);
        break;
        case '-':
        printf("result :%d\n", num1 - num2);
        break;
        case '*':
        printf("result:%d\n", num1 * num2);
        break;
        case '/':
        if(num2 == 0) 
       {
           printf("undefined\n");
       }
       else{
           printf("resulst:%d", num1 / num2);
       }
        break;
        case '%':
        if(num2 == 0)
        {
             printf("undefined.\n"); 
        }
        else{
        printf("result:%d\n", num1 % num2);
        }
        break;
        default:
        printf("Invalid operator");
        break;
       
        
    }
 return 0;

}