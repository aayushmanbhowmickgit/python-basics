//PROGRAM TO PRINT ALL NUMBERS FROM 1 TO n USING FOR LOOP
#include<stdio.h>
void main() {
    int num, i;
    printf("Enter a positive integer: ");
    scanf("%d", &num);
    for(i = 1; i <= num; ++i) 
    {
        printf("%d ", i);
    }
}