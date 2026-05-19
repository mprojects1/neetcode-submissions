class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pos_speed = []

        for i in range(len(position)):

            pos_speed.append((position[i], speed[i]))

        pos_speed.sort(reverse=True)

        fleet_times = []

        for car in pos_speed:
            distance = target - car[0]
            speed = car[1]
            time = distance/speed

            while not fleet_times or time > fleet_times[-1]:

                fleet_times.append(time)
        
        return len(fleet_times)






