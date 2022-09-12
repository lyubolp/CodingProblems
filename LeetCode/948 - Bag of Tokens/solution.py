class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        while len(tokens) > 0:
            face_ups = [token for token in tokens if token <= power]
            
            if len(face_ups) > 0:
                face_up = min(face_ups)
                score += 1
                power -= face_up
                tokens.remove(face_up)
            elif score != 0 and len(tokens) > 1:
                face_down = max(tokens)
                score -= 1
                power += face_down
                tokens.remove(face_down)
            else:
                return score
        return score

