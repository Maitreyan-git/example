def max_equal_height(stacks):
    heights = [sum(stack) for stack in stacks]
    tops = [0, 0, 0]     
    while True:
        min_height = min(heights)
        if heights[0] == heights[1] == heights[2]:
            return min_height  
        for i in range(3):
            while heights[i] > min_height and tops[i] < len(stacks[i]):
                heights[i] -= stacks[i][tops[i]]
                tops[i] += 1
import json
with open('Input.json', 'r') as input_file:
    data = json.load(input_file)
stacks = data["stacks"]
result = max_equal_height(stacks)
output_data = {"max_equal_height": result}
with open('Output.json', 'w') as output_file:
    json.dump(output_data, output_file)
print(f"Maximum Equal Height: {result}")
