#define MAX(a, b) (a > b ? a : b)

int lengthOfLongestSubstring(char * s) {
    int max = 0, x = 0, len = strlen(s);
    char *start = s;
    char h[256] = {'\0'};
    while (*s) {
        if (h[*s] != '\0') {
            max = MAX(max, s - start);
            while (*start != *s) {
                h[*(start++)] = '\0';
            }
            ++start;
        }
        else h[*s] = *s;
        ++s;
    }
    max = MAX(max, s - start);
    return max;
}
