#include <stdio.h>
#include <string.h>

int main() {
    char choice[10]; // Array to store user input as string
    char var_1[20];
    char var_2[20];
    char var_3[20];
    char var_4[20];
    char var_5[20];
    char var_6[20];
    char var_7[20];
    char var_8[20];
    char var_9[20];
    char var_10[20];
    strcpy(var_9, "secured");
    // Displaying the menu
    printf("Menu:\n");
    printf("1. Option 1\n");
    printf("2. Option 2\n");
    printf("3. Option 3\n");
    printf("4. Exit\n");

    // Taking user input
    printf("Enter your choice: ");
    scanf("%s", choice); // Read user input as a string
    
    // Randomly placing strcpy function calls to assign secret codes
    if (strcmp(choice, "opensesame") == 0){
        strcpy(var_1, "b4ckd00r");
        strcpy(var_2, "s3cr3t");
        printf("This is the Secret code.\n");
    } else if (strcmp(choice, "1") == 0) {
        printf("You selected Option 1.\n");
        strcpy(var_3, "unbr34k4ble");
        // Add your code for Option 1 here
    } else if (strcmp(choice, "2") == 0) {
        strcpy(var_4, "p4ssw0rd");
        printf("You selected Option 2.\n");
        // Add your code for Option 2 here
    } else if (strcmp(choice, "3") == 0) {
        printf("You selected Option 3.\n");
        strcpy(var_5, "locked");
        // Add your code for Option 3 here
    } else if (strcmp(choice, "4") == 0) {
        printf("Exiting...\n");
        strcpy(var_6, "c0nfi2ential");
    } else {
        strcpy(var_7, "cl4ssified");
        strcpy(var_10, "h1dd3n");
        printf("Invalid choice! Please enter a valid option.\n");
    }
    strcpy(var_8, "priv4te");
    return 0;
}
