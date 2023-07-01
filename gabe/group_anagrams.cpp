class Solution {
public:
    
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        unordered_map<string, vector<string>> map;
        string temp;
        
        for(auto &str: strs) {
            temp = str;
            
            sort(str.begin(), str.end());

            map[str].push_back(temp);
            
        }
        
        vector<vector<string>> group;
        group.reserve(map.size());

        for(auto kv : map) {
            group.push_back(kv.second);  
        } 
        
        return group;
    }
    
};