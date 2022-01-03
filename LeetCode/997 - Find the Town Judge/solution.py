class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = {}
        trusted_by = {}
        
        if n == 1:
            return 1
        
        for a, b in trust:
            if a in trusts:
                trusts[a].append(b)
            else:
                trusts[a] = [b]
            
            if b in trusted_by:
                trusted_by[b].append(a)
            else:
                trusted_by[b] = [a]
                
        trusts_nobody = set()
        for i in range(1, n + 1):
            if i not in trusts:
                trusts_nobody.add(i)
        
        trusted_by_all = set()
        for i in range(1, n + 1):
            if i in trusted_by and len(trusted_by[i]) == n - 1:
                trusted_by_all.add(i)
        
        intersection = trusts_nobody & trusted_by_all
        
        if len(intersection) == 1:
            return intersection.pop()
        else:
            return -1

