typedef struct node
{
    int val;
    int min;
    struct node* next;
} node;

typedef struct
{
    node *head;
} MinStack;

MinStack *minStackCreate()
{
    MinStack *m = calloc(1, sizeof(MinStack));
    if (!m)
        exit(1);
    return m;
}

void minStackPush(MinStack *obj, int val)
{
    if (obj->head == NULL)
    {
        node *n = malloc(sizeof(node));
        if (!n)
            exit(2);
        n->val = val;
        n->min = val;
        n->next = NULL;
        obj->head = n;
    }
    else
    {
        node *n = malloc(sizeof(node));
        if (!n)
            exit(2);
        n->val = val;
        n->min = val < obj->head->min ? val : obj->head->min;
        n->next = obj->head;
        obj->head = n;
    }
}

void minStackPop(MinStack *obj)
{
    node *n = obj->head;
    obj->head = obj->head->next;
    free(n);
}

int minStackTop(MinStack *obj)
{
    return obj->head->val;
}

int minStackGetMin(MinStack *obj)
{
    return obj->head->min;
}

void minStackFree(MinStack *obj)
{
    node *n;
    while (n = obj->head)
    {
        obj->head = n->next;
        free(n);
    }
    free(obj);
}

/**
 * Your MinStack struct will be instantiated and called as such:
 * MinStack* obj = minStackCreate();
 * minStackPush(obj, val);

 * minStackPop(obj);

 * int param_3 = minStackTop(obj);

 * int param_4 = minStackGetMin(obj);

 * minStackFree(obj);
*/