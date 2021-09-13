class Solution:
    def is_year_in_range(self, year: int, years: List[int]) -> int:
        return 1 if years[0] <= year < years[1] else 0
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        result = {}
        for start in logs:
            result[start[0]] = sum([self.is_year_in_range(start[0], year) for year in logs])
        
        year = 0
        population = 0
        for key in result:
            if population < result[key]:
                population = result[key]
                year = key
            elif population == result[key]:
                year = min(year, key)
                
        return year

