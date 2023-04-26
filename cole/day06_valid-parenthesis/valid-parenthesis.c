// beats 100% runtime 99.71% memory

typedef unsigned int uint;
#include <stdint.h>

bool isValid(char *s)
{
    uint16_t top = 0;
    for (char *ss = s; *ss; ++ss)
    {
        if (*ss == '(' || *ss == '[' || *ss == '{')
        {
            s[top++] = *ss;
        }
        else
        {
            if (top == 0)
            {
                return false;
            }
            if (*ss == ')' && s[top - 1] != '(')
            {
                return false;
            }
            if (*ss == ']' && s[top - 1] != '[')
            {
                return false;
            }
            if (*ss == '}' && s[top - 1] != '{')
            {
                return false;
            }
            --top;
        }
    }
    return top == 0;
}