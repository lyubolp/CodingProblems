class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        all_content = {}
        
        for path_group in paths:
            path_group = path_group.split(' ')
            current_dir = path_group[0]
            files = path_group[1:]
            
            for f in files:
                filename, content = f.split('(')
                content = content[:-1]
                
                full_path = current_dir + '/' + filename
                
                if content in all_content:
                    all_content[content].append(full_path)
                else:
                    all_content[content] = [full_path]
        
        return [all_content[key] for key in all_content if len(all_content[key]) > 1]

