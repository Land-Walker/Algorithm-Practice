# LC Q.49 Group Anagrams

2025.07.31. / 08.01 / 08.02

Difficulty: #medium

Type of Algorithm: [Array&Hashing]

Tags: #LeetCode #NeetCodeRoadmap

Start Time: 23:03 (1st try) 23:32 (2nd try) 15:12 (3rd try)

End Time: 23:37 (1st try) 23:52 (2nd try) 16:33 (3rd try)

## My Approaches

### Basic Ideas
1. Utilize Q242 solution 2: Use two for loops
    - one for assigning string s
    - one for assigning string t
    - check one by one if there are anagram set
    - for string t loop, there is a vector to store the same anagram set
    - for string s loop, there is one big vector to store all same anagram set vector
    - for string t loop, there must be a code to remove strings that are in the same anagram set
      - this was wrong, since remove strings will cause index problems

### Submission Code 1 (Failed)
~~~cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::vector<std::vector<std::string>> fullResult = {};
        std::vector<std::string> result = {};
        for (int i{0}; i < strs.size()-1; ++i){
            result.insert(result.end(), strs[i]);
                for (int j{1}; j < strs.size()-1; ++j){
                    std:string s = strs[i];
                    std::string t = strs[j];
                    std::sort(s.begin(), s.end());
                    std::sort(t.begin(), t.end());
                    if (strs[i] == strs[j]) {
                        result.insert(result.end(), strs[j]);
                    }
                }
            fullResult.push_back(result);
            result.clear();
        }
        return fullResult;
    }
};
~~~
- didnt work at all...
- I think the key maybe Q.242 soltion 3.
- using array, this quesiton will be easy & can use hashmap, making necessary searching process much faster

### What I found out to code the approach 1
- how to add vector to vector

### Submission Code 2
~~~cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::vector<std::vector<std::string>> fullResult = {};
        std::vector<std::string> result = {};
        std::vector<int> count(26,0);
        for (int i{0}; i < strs.size(); ++i){
            result.insert(result.end(), strs[i]);
                for (int j{1}; j < strs.size()-1; ++j){
                    std:string s = strs[i];
                    std::string t = strs[j];
                    count[s[i] - 'a']++;
                    count[t[i] - 'a']--;

            fullResult.push_back(result);
            result.clear()
        }
        return fullResult;
        }
    }
};
~~~

### What I found out to code the approach 2
- try to apply solution 3, but thought it wont work as this solution faces the exact same problem as before
- think there will be some technique that I dont know yet.
- Yeah, there was something called hash table & some different kind of algorithm that uses sorting in other way
- will summarize & study solutions tmr. 

## Solutions

### Solution 1 (Sorting)
~~~cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> res;      //it will store sorted string as a key, and a vector of its anagram strings as value 
        for (const auto& s : strs) {                    //detail description below
            string sortedS = s;                         //copy read-only s to sortedS
            sort(sortedS.begin(), sortedS.end());       //sort string in sortedS
            res[sortedS].push_back(s);                  //add sortedS as a key & add s to its value
        }
        vector<vector<string>> result;                  //it will extract values from res to print desired result
        for (auto& pair : res) {                        //detail description below
            result.push_back(pair.second);              //detail despcription below 
        }
        return result;
    }
};
~~~
for (const auto& s : strs):
- const makes s is read-only
- auto allows not to think about data type
- & makes s is a reference to the corresponding element in strs, making sure no copy is made
- s : strs allows to store each element in strs sequentially
- similar for 'for (auto& pair : res)'
- this combination, const auto& or auto& something : someVector is very, very useful

result.push_back(pair.second):
- pair represent each key-value pair in unordered_map (defined in the for loop initialization)
- .first means the key
- .second means the value
- by push_back to result, it stores all values to result from res

Time Complexity: $O(m\times n\log n)$
Space Complexity: $O(m\times n)$

### Solution 2 (Hash Table)
~~~cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> res;
        for (const auto& s : strs) {
            vector<int> count(26, 0);               //build key string
            for (char c : s) {
                count[c - 'a']++;                   //like Q242 solution 3, count frequency of each alphabet
            }
            string key = to_string(count[0]);       //convert datatypes of values in count from int to string
            for (int i = 1; i < 26; ++i) {
                key += ',' + to_string(count[i]);   //add all frequencies of each alphabets to one long string connected with ', '
            }
            res[key].push_back(s);
        }
        vector<vector<string>> result;              //same operation as before
        for (const auto& pair : res) {
            result.push_back(pair.second);
        }
        return result;
    }
};
~~~
Bro, my instinct was right. It uses Q242 solution 3.

Difference between this and solution 1 is how to create the key.
- solution 1: key = sorted string
- solution 2: key = frequency of each alphabet
  - e.g. bac -> 1,1,1,0,...

Time Complexity: $O(m\times n)$
Space Complexity:
- O(m) extra space
- $O(m\times n)$ space for the output list

### Solution 3 (Advanced Hash Table)
If I get more confident with C++, open this and try to learn its technique.
~~~cpp
class Solution {
public:
    string getSignature(const string& s) {
        vector<int> count(26, 0);
        for (char c : s) {
            count[c - 'a']++;
        }

        stringstream ss;
        for (int i = 0; i < 26; i++) {
            if (count[i] != 0) {
                ss << (char)('a' + i) << count[i];
            }
        }
        return ss.str();
    }

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        unordered_map<string, vector<string>> groups;

        for (const string& s : strs) {
            groups[getSignature(s)].push_back(s);
        }

        for (const auto& entry : groups) {
            result.push_back(entry.second);
        }

        return result;
    }
};
~~~