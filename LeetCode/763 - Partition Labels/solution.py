class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = {}
        
        for i, c in enumerate(s):
            if c in pos:
                pos[c].append(i)
            else:
                pos[c] = [i]
        
        partitions = []
        
        i = 0
        while i < len(s):
            current_partition = max(pos[s[i]])
            
            j = i
            while j < current_partition:
                current_partition = max(current_partition, max(pos[s[j]]))
                j += 1
            
            i = current_partition + 1
            partitions.append(i)
        
        partitions.insert(0, 0)
        return [partitions[i] - partitions[i-1] for i in range(1, len(partitions))]   

