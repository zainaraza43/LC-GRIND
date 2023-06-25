// the "fast" solution with a stack in C

int evalRPN(char ** tokens, int tokensSize) {
    int stack[tokensSize], ptr = 0;
    int x;
    for (int i = 0; i < tokensSize; ++i) {
        if (sscanf(tokens[i], "%d", &x)) { stack[ptr++] = x; continue; }
        switch (*tokens[i]) {
            case '+':
                stack[ptr - 2] += stack[ptr - 1];
                break;
            case '-':
                stack[ptr - 2] -= stack[ptr - 1];
                break;
            case '*':
                stack[ptr - 2] *= stack[ptr - 1];
                break;
            case '/':
                stack[ptr - 2] /= stack[ptr - 1];
                break;
            default:
                perror("what in tarnation");
                exit(1);
        }
        --ptr;
    }
    return stack[0];
}