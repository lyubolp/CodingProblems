class Solution:
    def isIpAddressValid(self, s: str) -> bool:
        res = s.split('.')
        
        if len(res) > 4:
            return False
        
        for num in res:
            if num == ' ' or num == '':
                return False
            if len(num) > 3:
                return False
            if len(num) > 1 and num[0] == '0':
                return False
            if int(num) > 255:
                return False
        return True
    
    def restoreIpAddressesHelper(self, s: str, result: List[str], dots: int, current: str):
        if dots == 0:
            result.append(current + "." + s)
        else:
            self.restoreIpAddressesHelper(s[1:], result, dots - 1, current + "." + s[:1])
            self.restoreIpAddressesHelper(s[2:], result, dots - 1, current + "." + s[:2])
            self.restoreIpAddressesHelper(s[3:], result, dots - 1, current + "." + s[:3])
            
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        
        self.restoreIpAddressesHelper(s[1:], result, 2, s[:1])
        self.restoreIpAddressesHelper(s[2:], result, 2, s[:2])
        self.restoreIpAddressesHelper(s[3:], result, 2, s[:3])
        
        return [res for res in result if self.isIpAddressValid(res)]

