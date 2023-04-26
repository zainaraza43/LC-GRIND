// ANOTHER 100% SOLUTION LES GOOOOOO
// (im doing c instead of cpp now because all my interviews will be in C)

typedef unsigned int uint;

bool isValid(char *s)
{
    // uint len = strlen(s);
    // char s[10000];
    uint top = 0;
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