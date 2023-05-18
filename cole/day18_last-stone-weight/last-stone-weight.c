void heapify(int *arr, int n, int i)
{
    int largest = i, left = 2 * i + 1, right = 2 * i + 2;
    if (left < n && arr[left] > arr[largest])
        largest = left;
    if (right < n && arr[right] > arr[largest])
        largest = right;
    if (largest != i)
    {
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;
        heapify(arr, n, largest);
    }
}

void buildheap(int *arr, int n)
{
    int i = n / 2 - 1;
    while (i >= 0)
    {
        heapify(arr, n, i);
        i--;
    }
}

int twosort(int *ab)
{
    int *b = ab + 1;
    if (*ab < *b)
    {
        int c = *b;
        *b = *ab;
        *ab = c;
    }
    return *ab;
}

#define ABS(x) (x < 0 ? (-x) : x)

int lastStoneWeight(int *stones, int stonesSize)
{
    for (int i = 0; i < stonesSize - 2; ++i)
    {
        buildheap(stones + i, stonesSize - i);
        stones[i + 1] = ABS(stones[i] - twosort(stones + i + 1));
    }
    if (stonesSize > 1)
    {
        twosort(stones + stonesSize - 2);
        stones[stonesSize - 1] = stones[stonesSize - 2] - stones[stonesSize - 1];
    }
    return stones[stonesSize - 1];
}
