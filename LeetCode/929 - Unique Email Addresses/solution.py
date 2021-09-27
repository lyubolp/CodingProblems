class Solution:
    def normalize_email(self, email: str) -> str:
        split_at = email.split('@')
        
        local_name = split_at[0].split('+')[0]
        local_name_no_dots = local_name.replace('.', '')
        
        
        return local_name_no_dots + '@' + split_at[1]
    def numUniqueEmails(self, emails: List[str]) -> int:
        normalized_emails = [self.normalize_email(email) for email in emails]
        
        result = set()
        
        for email in normalized_emails:
            if email not in result:
                result.add(email)
        
        return len(result)

