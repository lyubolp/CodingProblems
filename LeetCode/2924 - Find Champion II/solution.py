class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        defeated = defaultdict(set)

        for team_a, team_b in edges:
            defeated[team_a].add(team_b)

        weaker_than = {team: self.calculate_weaker_than(team, defeated) for team in range(n)}

        champs = [team for team, weaker_than_count in weaker_than.items() if weaker_than_count == 0]

        if len(champs) == 1:
            return champs[0]
        else:
            return -1

    def calculate_weaker_than(self, team, defeated):
        return sum(1 for v in defeated.values() if team in v)
