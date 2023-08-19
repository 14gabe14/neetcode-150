class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = [0]

        for i in range(1, len(temperatures)):
            if temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                answer[j] = i - j

                while stack:
                    if temperatures[stack[-1]] < temperatures[i]:
                        j = stack.pop()
                        answer[j] = i - j
                    else:
                        break

            stack.append(i)

        return answer