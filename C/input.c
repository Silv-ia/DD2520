#include <stdio.h>

int main()
{
    char input;
    
    scanf("%c", &input);
    
    char* pointer = &input;
    
    printf("%c", pointer[0]);
        
    return 0;
}