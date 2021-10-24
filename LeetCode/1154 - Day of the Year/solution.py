class Solution:
    def is_leap_year(self, year: int) -> bool:
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True
        
    def dayOfYear(self, date: str) -> int:
        days = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }
        
        date_split = date.split('-')
        
        year = int(date_split[0])
        month = int(date_split[1])
        day = int(date_split[2])
        
        
        result = 0
        # print('{}, {}, {}'.format(year, month, day))
        
        for m in range(1, month):
            result += days[m]
            
        result += day
        
        if month > 2 and self.is_leap_year(year):
            result += 1
            
        return result

