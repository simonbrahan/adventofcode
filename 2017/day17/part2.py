current_pos = 0
step_size = 371

for i in range(1, 50000001):
    current_pos = (current_pos + step_size) % i + 1
    if current_pos is 1:
        current_val = i

print current_val
