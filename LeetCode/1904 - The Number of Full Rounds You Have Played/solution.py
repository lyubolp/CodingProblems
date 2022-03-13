class Solution:
    def convert_hours_to_minutes(self, time: str) -> int:
        hours, minutes = time.split(":")
        return int(hours) * 60 + int(minutes)
    
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        login_time_minutes = self.convert_hours_to_minutes(loginTime)
        logout_time_minutes = self.convert_hours_to_minutes(logoutTime)
        
        if login_time_minutes < logout_time_minutes:
            
            if login_time_minutes % 15 == 0:
                current_time = login_time_minutes
            else:
                current_time = 15 * (login_time_minutes // 15 + 1)
                
            result = 0
            while current_time + 15 <= logout_time_minutes:
                result += 1
                current_time += 15
        else:
            result = (24*60 - login_time_minutes) // 15
            result += logout_time_minutes // 15
                
        
        return result

