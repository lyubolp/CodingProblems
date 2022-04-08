class KthLargest {
public:
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for (int& num: nums) {
            this->q.push(num);
        }
    }
    
    int add(int val) {
        this->q.push(val);
        
        while (this->q.size() > this->k) {
            this->q.pop();
        }
        return this->q.top();
    }
private:
    priority_queue<int, vector<int>, greater<int>> q;
    int k;
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */

