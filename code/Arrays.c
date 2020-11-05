#include <stdio.h>

int main()
{
    /* define an array of 10 integers */
    int numbers[10];
    /* in C, the index is zero-based */
    /* populate the array */
    numbers[0] = 10;
    numbers[1] = 20;
    numbers[2] = 30;
    numbers[3] = 40;
    numbers[4] = 50;
    numbers[5] = 60;
    numbers[6] = 70;
    /* print the 7th number from the array, which has index of 6 */
    printf("The 7th number in the array is %d\n", numbers[6]);
    return 0;
}

