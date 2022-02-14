class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # B C D
        # B C D
        
        all_cities = set()
        visited = set()
        
        for start, end in paths:
            all_cities.add(start)
            all_cities.add(end)
            visited.add(start)
            
        
        for city in all_cities:
            if city not in visited:
                return city
        
        return ""

