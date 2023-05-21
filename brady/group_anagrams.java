class Solution {
  
    // O(nklg(k)) time, O(n) space, where n is the number of strings in strs and k is the length of the longest string in strs
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagramGroupsMap = new HashMap<>();
        for (String str : strs) {
            char[] charArr = str.toCharArray();
            Arrays.sort(charArr);
            String sorted = String.valueOf(charArr);
            if (!anagramGroupsMap.containsKey(sorted)) anagramGroupsMap.put(sorted, new ArrayList<>());
            anagramGroupsMap.get(sorted).add(str);
        }

        return new ArrayList<>(anagramGroupsMap.values());
    }
}
