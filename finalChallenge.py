import random
first_names = ["Christian", "Dylan", "Travis", "Katelyn"]
last_names = ["Sachs", "Katina", "Peck", "Mehner"]

print(" My name is", first_names[0], last_names[0])

f_name = random.choice(first_names)
l_name =  random.choice(last_names)
# print(f_name  + " " + l_name)
print(f" {f_name} {l_name}")