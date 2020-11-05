#include <stdio.h>
void addone(int *n){
	(*n)++;
}

typedef struct {
	int x;
	int y;
} point;

void move(point * p) {
	p->x++;
	p->y++;
}

int main() {
	point p;
	p.x = 1;
	p.y = 2;

	printf("p is at %d, %d\n", p.x, p.y);

	printf("update\n");

	move(&p);

	printf("p now is at %d, %d\n", p.x, p.y);

	
	return 0;
}

