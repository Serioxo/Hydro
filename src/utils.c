#include "../include/util.h"

char *read_ascii_file(const char *path)
{
    // Creates File
    FILE* file = fopen(path, "r");

    if(!file){
        printf("File not Recognised... `%s`\n", path);
        //breaks code
        return NULL;
    }

    // Getting File Size
    fseek(file,0, SEEK_END);
    int size = ftell(file);
    fseek(file,0,SEEK_SET);

    //Buffer
    char* buffer = (char*) malloc(sizeof(char) * (size + 1)); // +1 byte to buffer size for safety
    //Dedicates buffer size
    fread(buffer, 1, size, file);
    buffer[size] = '\0'; // Default buffer size
    fclose(file);

    return buffer;
}