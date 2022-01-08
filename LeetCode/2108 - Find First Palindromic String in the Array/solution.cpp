class Solution {
public:
    bool is_word_palindrome(std::string word) {
        if(word.length() == 0 || word.length() == 1) {
            return true;
        }
        else {
            if (word[0] == word[word.length() - 1]) {
                return this->is_word_palindrome(word.substr(1, word.length() - 2));
            }
            else {
                return false;
            }
            
        }
    }
    string firstPalindrome(vector<string>& words) {
        for(string word: words) {
            if(this->is_word_palindrome(word)) {
                return word;
            }
        }
        
        return "";
    }
};
