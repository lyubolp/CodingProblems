class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        elements_in_stack = set()
        
        i, j = (0, 0)
        l = len(pushed)
        while j < l:
            current_to_pop = popped[j]
            
            if current_to_pop in elements_in_stack:
                if current_to_pop != stack[-1]:
                    return False
                
                stack.pop()
                elements_in_stack.remove(current_to_pop)
                j += 1
            else:
                current_to_push = pushed[i]
                while current_to_push != current_to_pop:
                    stack.append(pushed[i])
                    elements_in_stack.add(pushed[i])
                    i += 1
                    if i >= l:
                        return False
                    current_to_push = pushed[i]
                
                stack.append(pushed[i])
                elements_in_stack.add(current_to_push)
                i += 1
        return True

