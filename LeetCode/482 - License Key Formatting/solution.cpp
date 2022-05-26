class Solution {
public:
    string licenseKeyFormatting(string s, int k) {
        string r = "";
        int i = 0;
        for (auto it=s.rbegin(); it != s.rend(); it++) {
            if (*it != '-') {
                if (i == k) {
                    i = 0;
                    r += '-';
                }
                if (*it >= 'a') {
                    r += (*it) - ('a' - 'A');
                }
                else {
                    r += *it;
                }
                i += 1;
                
            }
            
        }
        
        reverse(r.begin(), r.end());
        return r;
    }
};

