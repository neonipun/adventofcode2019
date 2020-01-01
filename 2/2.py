with open("input", "r") as f:
    org_mem = f.readline().split(",")
    org_mem = dict(enumerate(map(int, org_mem)))

# mem = dict(enumerate(map(int, "1,1,1,4,99,5,6,0,99".split(","))))
# print(mem, '\n')

from itertools import permutations

for noun, verb in permutations(range(100), 2):
    mem = org_mem.copy()
    mem[1] = noun
    mem[2] = verb
    # print(mem, '\n')

    idx = 0
    while idx < len(mem):
        a, b = mem[mem[idx+1]], mem[mem[idx+2]]
        addr = mem[idx+3]

        if mem[idx] == 1:
            mem[addr] = a + b
        elif mem[idx] == 2:
            mem[addr] = a * b
        elif mem[idx] == 99:
            break
        else:
            break
        
        idx += 4
    
    # print(mem[0], noun, verb)
    if mem[0] == 19690720:
        break

print("Result: noun, verb -", noun, verb)
print("Answer:", 100*noun + verb)
