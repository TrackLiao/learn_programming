#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char * name;
    int age;
} person;

int main() {
    person * myperson = (person *) malloc(sizeof(person));

    myperson->name = "John";
    myperson->age = 27;

    printf("The person is %s age %d \n", myperson->name, myperson->age);

    free(myperson);
    printf("The person is %s age %d \n", myperson->name, myperson->age);





	
	return 0;
}

