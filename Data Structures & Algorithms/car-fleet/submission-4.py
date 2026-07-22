class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        prev_time = 0.0
        
        for pos, spd in sorted(zip(position, speed), reverse=True):
            time = (target - pos) / spd
            
            if time > prev_time:
                fleets += 1
                prev_time = time
                
        return fleets