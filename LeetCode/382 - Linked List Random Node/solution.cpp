/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    Solution(ListNode* head) {
        this->head = head;
        this->last_node = head;
        this->last_index = 0;
        this->length = this->get_length(head);
        
        this->gen = std::mt19937(123);
        this->distr = std::uniform_int_distribution<>(0, this->length);
    }
    
    int getRandom() {
        int index = this->distr(this->gen);
        
        if (index >= last_index) {
            int val = this->get_node(index - this->last_index);
            this->last_index = index;
            return val;
        }
        else {
            this->last_node = this->head;
            return this->get_node(index);
        }
    }
    
    int get_node(const int offset) {
        for (int i = 0; i < offset; i++) {
            this->last_node = this->last_node->next;
            
            if (this->last_node == nullptr) {
                this->last_node = this->head;
            }
        }
        return this->last_node->val;
    }
private:
    int get_length(const ListNode* head) {
        if (head == nullptr) {
            return 0;
        }
        else {
            return 1 + this->get_length(head->next);
        }
    }
    ListNode* head;
    ListNode* last_node;
    int last_index;
    int length;
    
    std::mt19937 gen; 
    std::uniform_int_distribution<> distr;
    
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head);
 * int param_1 = obj->getRandom();
 */

