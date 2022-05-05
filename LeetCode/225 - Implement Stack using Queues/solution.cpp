class MyStack {
private:
    queue<int> queue1;
    queue<int> queue2; 
public:
    MyStack() {
        
    }
    
    void push(int x) {
        this->queue1.push(x);
    }
    
    int pop() {
        while (this->queue1.size() > 1) {
            int item = this->queue1.front();
            this->queue1.pop();
            
            this->queue2.push(item);
        }
        
        int result = this->queue1.front();
        this->queue1.pop();
        
        while(this->queue2.size() > 0) {
            int item = this->queue2.front();
            this->queue2.pop();
            this->queue1.push(item);
        }
        
        return result;
    }
    
    int top() {
        while (this->queue1.size() > 1) {
            int item = this->queue1.front();
            this->queue1.pop();
            
            this->queue2.push(item);
        }
        
        int result = this->queue1.front();
        this->queue1.pop();
        
        this->queue2.push(result);
        
        while(this->queue2.size() > 0) {
            int item = this->queue2.front();
            this->queue2.pop();
            this->queue1.push(item);
        }
        
        return result;
    }
    
    bool empty() {
        return this->queue1.empty();   
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */

