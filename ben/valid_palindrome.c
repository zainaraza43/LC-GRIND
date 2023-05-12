#include <stdbool.h>
#include <ctype.h>
#include <string.h>

bool isPalindrome(char * s){
    char* start = s;
    char* end = &s[strlen(s)] - 1;

    while (start < end) {
        if (!isalnum(*start)) {
            ++start;
            continue;
        }
        if (!isalnum(*end)) {
            --end;
            continue;
        }

        if (tolower(*start) != tolower(*end)) {
            return false;
        }
        ++start;
        --end;
    }
    return true;
}