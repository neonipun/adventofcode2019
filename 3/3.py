from pprint import pprint

input_file = 'input'
with open(input_file, 'r') as f:
    wires = [list(map(str.strip, x.split(','))) for x in f.readlines()]

# pprint(wires)
wire_map = {}
dir_map = dict(zip('LRUD', [-1, 1, 1, -1]))

for idx, wire in enumerate(wires):
    # wire_map[idx] = set()
    wire_map[idx] = {} 
    x, y = [0], [0]
    steps = 0
    for wd in wire:
        d = wd[0]
        if d in 'LR':
            temp = x 
        elif d in 'UD':
            temp = y
        else:
            print('Error in input')
            exit(1)
        
        s = int(wd[1:])
        for _ in range(s):
            temp[0] += dir_map[d]
            steps += 1
            # wire_map[idx].add('{} {}'.format(x[0], y[0]))
            
            p_key = '{} {}'.format(x[0], y[0])
            if p_key in wire_map[idx]:
                wire_map[idx][p_key] += ' ' + str(steps)
            else:
                wire_map[idx][p_key] = str(steps) 

# pprint(wire_map)
# wire_map_intersections = set.intersection(*wire_map.values())
# pprint(wire_map_intersections)

# with open("wire_map.txt","w") as f:
#     f.write(str(wire_map))

wire_map_intersections = set(wire_map[0].keys())
for wire in wire_map:
    wire_map_intersections &= set(wire_map[wire].keys())

print("Part One Answer:", min([abs(int(p.split()[0])) + abs(int(p.split()[1])) for p in wire_map_intersections]))

min_combined_steps = 999999999999
min_i = ""
for i in wire_map_intersections:
    combined_steps = 0
    for wire in wire_map.values():
        if ' ' in wire[i]:
            combined_steps += int(wire[i].split()[0])
        else:
            combined_steps += int(wire[i])
    if combined_steps < min_combined_steps:
        min_combined_steps = combined_steps
        min_i = i

print("Part Two Answer:", min_combined_steps, "min_i:", min_i)