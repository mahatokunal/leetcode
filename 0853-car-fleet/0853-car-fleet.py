class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=[]
        for i in range(0, len(position)):
            cars.append((target-position[i], speed[i]))
        cars.sort(key=lambda pair:pair[0])
        # print(cars)
        times=[0]*len(cars)
        for i in range(0, len(cars)):
            dist, speed = cars[i]
            times[i] = dist/speed
        # print(times)
        fleet_time=times[0]
        fleet=1
        for i in range(1, len(times)):
            if times[i]>fleet_time:
                fleet_time=times[i]
                fleet+=1
        return fleet