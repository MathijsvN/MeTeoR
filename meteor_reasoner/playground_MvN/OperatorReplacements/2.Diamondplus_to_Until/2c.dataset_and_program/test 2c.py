from meteor_reasoner.materialization.materialize import *
from meteor_reasoner.utils.loader import load_dataset, load_program

# Original Syntax

print("ORIGINAL SYNTAX")

with open("meteor_reasoner/playground_MvN/OperatorReplacements/2.Diamondplus_to_Until/2c.dataset_and_program/data/original/dataset_original.txt") as file:
    data = file.readlines()
with open("meteor_reasoner/playground_MvN/OperatorReplacements/2.Diamondplus_to_Until/2c.dataset_and_program/data/original/program_original.txt") as file:
    program = file.readlines()

D = load_dataset(data)
D_index = build_index(D)
rules = load_program(program)
for i in range(1,4):
    print("Iteration:", i)
    print("=====================")
    print("Before D:")
    print_dataset(D)
    print("Derived facts:")
    delta_new = naive_immediate_consequence_operator(rules, D, D_index)
    print_dataset(delta_new)
    print("After D:")
    materialize(D, rules, K=1)
    print_dataset(D)


# Replacement Syntax
print("REPLACEMENT SYNTAX")

with open("meteor_reasoner/playground_MvN/OperatorReplacements/2.Diamondplus_to_Until/2c.dataset_and_program/data/replaced/dataset_replaced.txt") as file:
    data = file.readlines()
with open("meteor_reasoner/playground_MvN/OperatorReplacements/2.Diamondplus_to_Until/2c.dataset_and_program/data/replaced/program_replaced.txt") as file:
    program = file.readlines()

D = load_dataset(data)
D_index = build_index(D)
rules = load_program(program)
for i in range(1,4):
    print("Iteration:", i)
    print("=====================")
    print("Before D:")
    print_dataset(D)
    print("Derived facts:")
    delta_new = naive_immediate_consequence_operator(rules, D, D_index)
    print_dataset(delta_new)
    print("After D:")
    materialize(D, rules, K=1)
    print_dataset(D)

# Both the original and replaced syntax are unable to draw the conclusion B;
# The current code does not 'search' where A holds, which would yield the right conclusion.