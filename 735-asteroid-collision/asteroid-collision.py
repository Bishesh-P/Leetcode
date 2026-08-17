class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ch in asteroids:

            while stack and ch < 0 and stack[-1] > 0:

                if stack[-1] < -ch:
                    stack.pop()

                elif stack[-1] == -ch:
                    stack.pop()
                    break

                else:
                    break

            else:
                stack.append(ch)

        return stack