import re, collections

bots_contents = collections.defaultdict(list)
bot_operations = {}

for line in open('input', 'r'):
    value_assignment = re.match('value (\d+) goes to bot (\d+)', line)
    if value_assignment:
        bots_contents[int(value_assignment.group(2))].append(int(value_assignment.group(1)))

    bot_behaviour = re.match('bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)', line)
    if bot_behaviour:
        bot_operations[int(bot_behaviour.group(1))] = (
            (bot_behaviour.group(2), int(bot_behaviour.group(3))),
            (bot_behaviour.group(4), int(bot_behaviour.group(5)))
        )

while len([bot for bot in bots_contents if len(bots_contents[bot]) > 1]):
    for bot_id, bot_contents in bots_contents.items():
        if len(bot_contents) < 2:
            continue

        low, high = sorted(bot_contents)

        bots_contents[bot_id] = []

        low_op, high_op = bot_operations[bot_id]
        low_op_type, low_op_target = low_op
        if low_op_type == 'bot':
            bots_contents[low_op_target].append(low)
        elif low_op_target in [0, 1, 2]:
            print 'target', low_op_target, 'value', low

        high_op_type, high_op_target = high_op
        if high_op_type == 'bot':
            bots_contents[high_op_target].append(high)
        elif high_op_target in [0, 1, 2]:
            print 'target', high_op_target, 'value', high
