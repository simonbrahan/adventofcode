import sys
sys.path.append('../day18')
from processor import Processor, parse_instr

instrs = []
with open('input.txt') as input_file:
    for line in input_file:
        if line[0] not in ['#', '\n']:
            instrs.append(parse_instr(line))

proc1 = Processor(instrs, 0)

proc1.run()

print proc1.mul_count
