#include <stdio.h>

/* integer type, char, int, short, long, long long */
/* unsigned integer type, unsighed char, unsigned int ....... */
/* floating point numbers-real numbers, float, double */

/* C does not have a boolean type */
#define BOOL char
#define FALSE 0
#define TRUE 1

int main()
{
    int foo;
    int bar = 1;

    int a = 0, b = 1, c = 2, d = 3, e = 4;
    a = b - c + d * e;
    printf("result: %d\n", a);
    return 0;
}

