class Solution {
public:
    int titleToNumber(string s) {
        int result = 0;
        int l = 0;
        
        const int base = 26;
        for (auto iter = s.rbegin(); iter != s.rend(); iter++) {
            int current_value = *iter - 'A' + 1;
            
            result += pow(base, l) * current_value;
            l += 1;
        }
        return result;
    }
};

