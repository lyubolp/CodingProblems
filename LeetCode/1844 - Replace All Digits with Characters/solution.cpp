class Solution {
public:
    string replaceDigits(string s) {
        std::string result; 
        
        char prev;
        for(char c: s) {
            
            if ('a' <= c && c <= 'z') {
                prev = c;
                result += c;
            }
            else {
                result += c - '0' + prev;
            }
        }
        
        return result;
    }
};
