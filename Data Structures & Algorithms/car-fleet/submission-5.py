class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed=(sorted(list(zip(position,speed)), reverse=True))
        sorted_pos, sorted_speed = map(list, zip(*pos_speed))
        time_to_target=[]
        for k in range(len(sorted_pos)): 
            time_to_target.append((target-sorted_pos[k])/sorted_speed[k])
        print(time_to_target)
        fleets=len(time_to_target)

        for i in range(len(time_to_target)-1):
            if time_to_target[i]>=time_to_target[i+1]:
                fleets-=1 
                time_to_target[i+1]=time_to_target[i]

        return fleets