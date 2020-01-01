import math

# Part One
with open("input", "r") as f:
    fuel = 0 
    for line in f.readlines():
        fuel += math.floor(int(line)/3) - 2
    
print("fuel:", fuel)

# Part Two 
with open("input", "r") as f:
    final_fuel = 0 
    for line in f.readlines():
        fuel = math.floor(int(line)/3) - 2
        if fuel>0: 
            final_fuel += fuel
            while fuel:
                temp_fuel = math.floor(fuel/3) - 2
                if temp_fuel > 0:
                    final_fuel += temp_fuel
                    fuel = temp_fuel
                else:
                    break

print("final_fuel:", final_fuel)
