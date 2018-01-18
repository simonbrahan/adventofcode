import sys
sys.path.append('../day18')
from processor import Processor, parse_instr

with open('input.txt') as input_file:
    instrs = [parse_instr(line) for line in input_file]

proc1 = Processor(instrs, 0)

proc1.run()

print proc1.mul_count
