class Solution {
public:
    int isAlphanumeric(char ch)
    {
        if(ch >= 'a' && ch <= 'z')   
            return 1;
        if(ch >= 'A' && ch <= 'Z')   
            return 2;
        if(ch >= '0' && ch <= '9')  
            return 1;
        return 0;
    }
    bool isPalindrome(string s) {
        int i = 0, from_end = s.length() - 1 - i;
        int flag, flag2;
        while (i < from_end) {
            flag = isAlphanumeric(s[i]);
            flag2 = isAlphanumeric(s[from_end]);
            if ( !flag ) {
                i++;
            } else if ( !flag2 ) {
                from_end--;
            } else if ( !((s[i] == s[from_end]) || (flag2==2 && (s[i] == 32 + s[from_end])) || (flag==2 && (s[i] + 32 ==  s[from_end]))) ) {
                return false;
            } else {
                i++;
                from_end--;
            }
        }
        return true;
    }
};
