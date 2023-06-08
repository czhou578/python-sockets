def dailyTemperatures(temperatures: list[int]) -> list[int]:
    stack = []

    result = []

    for element in temperatures:
        first = temperatures.pop(0)
        stack.append(first)

        if len(temperatures) == 0:
            result.append(0)
            return result

        pointer = 0
        while temperatures[pointer] < stack[-1]:
            pointer += 1
        
        result.append(pointer + 1)
        print(result)

dailyTemperatures([73,74,75,71,69,72,76,73])
    

