from processor import Processor, parse_instr
import threading, time

with open('input.txt') as input_file:
    instrs = [parse_instr(line) for line in input_file]

proc1 = Processor(instrs, 0)
proc2 = Processor(instrs, 1)

proc1.register_partner(proc2)
proc2.register_partner(proc1)

for proc in [proc1, proc2]:
    threading.Thread(target=proc.run).start()

