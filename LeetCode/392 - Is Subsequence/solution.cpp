class Solution {
public:
    bool isSubsequence(string s, string t) {
        if (s.length() == 0) {
            return true;
        }
        if (t.length() == 0) {
            return false;
        }
       
        char target = s[0];
        std::size_t index = t.find(target);
        
        if (index != std::string::npos) {
            return this->isSubsequence(s.substr(1), t.substr(index + 1));
        }
        else {
            return false;
        }
    }
};
