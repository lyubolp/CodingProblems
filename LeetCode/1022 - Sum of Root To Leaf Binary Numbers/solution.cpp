/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int sumRootToLeaf(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        
        std::stack<std::pair<TreeNode*, std::string>> s;
        
        s.push({root, ""});
        
        std::vector<std::string> result;
        while (s.size() > 0) {
            std::pair<TreeNode*, std::string> current = s.top();
            s.pop();
            
            std::string next_number = current.second + std::to_string(current.first->val);
            
            if (current.first->left == nullptr && current.first->right == nullptr) {
                result.push_back(next_number);
            }
            else if (current.first->left == nullptr && current.first->right != nullptr) {
                s.push({current.first->right, next_number});
            }
            else if (current.first->left != nullptr && current.first->right == nullptr) {
                s.push({current.first->left, next_number});
            }
            else {
                s.push({current.first->left, next_number});
                s.push({current.first->right, next_number});
            }
        }
        
        int sum = 0;
        for (auto item: result) {
            sum += std::stoi(item, nullptr, 2);
        }
        return sum;
    }
};
