class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        
        version1 = [int(num) for num in version1]
        version2 = [int(num) for num in version2]
        
        if len(version1) < len(version2):
            version1 += [0] * (len(version2) - len(version1))
        elif len(version1) > len(version2):
            version2 += [0] * (len(version1) - len(version2))
        
        # print(version1, version2)
        l = len(version1)
        
        for i in range(l):
            if version1[i] < version2[i]:
                return -1
            elif version1[i] > version2[i]:
                return 1
        return 0

