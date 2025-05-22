class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack = []
        cars = []
        for p, s in zip(position, speed):
            cars.append([p,s])
        cars.sort(key = lambda x: x[0], reverse=True)

        for p, s in cars:
            t = (target-p)/s
            if not stack or stack[-1][1] < t:
                stack.append([p, t])
        return len(stack)


# Test
s = Solution()
print(s.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))
print(s.carFleet(target = 10, position = [3], speed = [3]))
print(s.carFleet(target = 100, position = [0,2,4], speed = [4,2,1]))
