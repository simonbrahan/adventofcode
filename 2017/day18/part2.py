from processor import Processor, parse_instr

with open('input.txt') as input_file:
    proc1 = Processor([parse_instr(line) for line in input_file])

proc1.register_partner(Processor([]))

proc1.run()
