#include <stdio.h>
#include <stdlib.h>

int main()
{
    char input;
    
    scanf("%c", &input);
        
    return 0;
}


/* Input format: 
128 bits, 16 bytes -- key (fixed size 128, other too?)
blocks to encode -- 16 bytes
output -- each encrypted block, 128 bits, 16 bytes
 */

 // 4 functions, called in same order, except first and last round different. 


// succesfully compiles. 

/* 
char notes:
char name[20]; x must be 1 larger than the length, for \0, null.

scanf("%19s", name);

for example. 

this works: 
char input[129];
scanf("%128c", &input);
*/