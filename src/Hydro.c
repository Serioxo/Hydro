#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <io.h>
#include <string.h>
#include "../include/util.h"

// command formatting:
// hydro compile file.hyd

int main(int argc, char** argv){

    if (argc < 3){
        printf("give more arguments dipshit");
        return 1;
    }

    if(strcmp(argv[1], "compile") == 0){
        // Read Source File and return characters
        char* sourcefile = read_ascii_file(argv[2]);
        printf("%s\n", sourcefile);
        free(sourcefile);
    }
        
    return 0;
}
