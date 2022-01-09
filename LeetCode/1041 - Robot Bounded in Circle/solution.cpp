struct Position {
    int x;
    int y;
    int direction; //0 - up, 1 - left, 2 - down, 3 - right
    
    Position(const int x, const int y, const int direction) {
        this->x = x;
        this->y = y;
        this->direction = direction;
    }
    
    void do_instruction(const char instruction) {
        if (instruction == 'G') {
            if(direction == 0) {
                this->y += 1;
            }
            else if(direction == 1) {
                this->x += 1;
            }
            else if(direction == 2) {
                this->y -= 1;
            }
            else if(direction == 3) {
                this->x -= 1;
            }
            else {
                throw std::invalid_argument("invalid direction");
            }
        }
        else if (instruction == 'L') {
            int new_direction = this->direction + 1;
            new_direction %= 4;
            
            this->direction = new_direction;
        }
        else if (instruction == 'R') {
            int new_direction = this->direction - 1;
            if (new_direction < 0) {
                new_direction = 3;
            }
            this->direction = new_direction;
        }
        else {
            throw std::invalid_argument("Invalid argument");
        }
    }
};
class Solution {
public:
    bool isRobotBounded(string instructions) {
        Position initial = Position(0, 0, 0);
        
        for (char c: instructions) {
            initial.do_instruction(c);
        }
        
        
        if (initial.direction != 0) {
            return true;
        }
        else if (initial.x == 0 and initial.y == 0) {
            return true;
        }
        else {
            return false;
        }
    }
};
