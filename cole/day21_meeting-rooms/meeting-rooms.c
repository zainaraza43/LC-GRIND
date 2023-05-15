/**
 * You can create and use dynamic array in your code.
 * You can replace "int" to any other type you want to put in the array, e.g. float, char*, list_node*.
 * Create an empty int array:         int* arr = NULL;
 * Add an element to the back:        cvector_push_back(arr, 42);
 * Remove an element from the back:   cvector_pop_back(arr);
 * Get size of a dynamic array:       cvector_size(arr)
 * For other macros, see https://github.com/eteran/c-vector*
 * Definition of Interval:
 * typedef struct {
 *     int start, end;
 * } interval;
 */

 #include <ctype.h>

void swap(interval *a, interval *b)
{
    interval t = *a;
    *a = *b;
    *b = t;
}

int partition(interval array[], int low, int high)
{
    int pivot = array[high].start;
    int i = (low - 1);
    for (int j = low; j < high; j++)
        if (array[j].start > pivot)
            swap(&array[++i], &array[j]);
    swap(&array[i + 1], &array[high]);
    return (i + 1);
}

void quickSort(interval array[], int low, int high)
{
    if (low < high)
    {
        int pi = partition(array, low, high);
        quickSort(array, low, pi - 1);
        quickSort(array, pi + 1, high);
    }
}
/**
 * @param intervals: an array of meeting time intervals
 * @return: if a person could attend all meetings
 */
bool can_attend_meetings(interval* intervals) {
    const unsigned int size = cvector_size(intervals);
    if (size <= 1)
        return true;
    quickSort(intervals, 0, size - 1);
    for (unsigned int i = 1; i < size; ++i)
        if (intervals[i-1].end > intervals[i].start)
            return false;
    return true;
}