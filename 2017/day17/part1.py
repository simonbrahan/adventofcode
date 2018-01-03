buff = [0]
current_pos = 0
step_size = 371
for i in range(1, 2018):
    current_pos = (current_pos + step_size) % len(buff) + 1
    buff.insert(current_pos, i)

print buff[buff.index(2017) + 1]
