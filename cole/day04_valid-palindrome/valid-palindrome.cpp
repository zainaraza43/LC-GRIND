// BEATS 100% TAKE THAT PLEBS

#include <string>
using namespace std;
class Solution
{
public:
    bool isPalindrome(string s)
    {
        if (s.empty())
        {
            return true;
        }
        if (s.size() == 1)
        {
            return true;
        }
        auto it = s.begin();
        auto itr = s.rbegin();
        int start = 0, end = s.size() - 1;
        while (start < end)
        {
            if (!isalnum(*it))
            {
                it++;
                start++;
                continue;
            }
            if (!isalnum(*itr))
            {
                itr++;
                end--;
                continue;
            }
            if (tolower(*it) != tolower((*itr)))
            {
                return false;
            }
            it++;
            itr++;
            start++;
            end--;
        }
        return true;
    }
};


#include <iostream>
int main(void)
{
    // print(s.isPalindrome('zainniaz'))
    // print(s.isPalindrome('A man, a plan, a canal: Panama'))
    // print(s.isPalindrome(' '))

    Solution s;
    std::cout << s.isPalindrome("zainniaz") << std::endl;
    std::cout << s.isPalindrome("A man, a plan, a canal: Panama") << std::endl;
    std::cout << s.isPalindrome(" ") << std::endl;
}