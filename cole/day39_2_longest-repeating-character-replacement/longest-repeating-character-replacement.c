/**
 * 1. for each endpos in the sliding window
 *      i. update the counts of each character in the window
 *     ii. update the max count of any character in the window, which can only possibly be the new element so we check one pos
 *    iii. if there is not enough blanks in the window to replace with k, we need to shrink the window until we can fit k blanks
 *     iv. update the max, if there is a new one found
 * 2. return the max window size, maxlen is the length of the longest window that was encountered
 */

#define MAX(a, b) (a < b ? b : a)

int characterReplacement(char *s, int k)
{
    uint len = strlen(s);
    int count[26] = {0};
    int start = 0, maxcnt = 0, maxlen = 0;
    int x, curlen;
    for (int end = 0; end < len; ++end)
    {
        x = ++count[s[end] - 'A'];
        maxcnt = MAX(maxcnt, x);
        while ((curlen = end - start + 1) - maxcnt > k)
        {
            --count[s[start] - 'A'];
            ++start;
        }
        maxlen = MAX(maxlen, curlen);
    }
    return maxlen;
}