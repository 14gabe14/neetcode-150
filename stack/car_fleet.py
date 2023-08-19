class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        indices = sorted(range(len(position)), key=lambda i: position[i])
        position = [position[i] for i in indices]
        speed = [speed[i] for i in indices]
        time = [(target-position[i])/speed[i] for i in range(len(position))]

        count = 1
        j = len(time)-1

        for i in range(j-1, -1, -1):
            if time[i] > time[j]:
                count += 1
                j = i
                
        return count