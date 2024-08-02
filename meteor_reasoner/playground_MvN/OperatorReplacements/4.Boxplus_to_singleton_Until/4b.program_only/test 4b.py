from meteor_reasoner.materialization.materialize import *
from meteor_reasoner.utils.loader import load_dataset, load_program


# Original Syntax

print("ORIGINAL SYNTAX")

with open("meteor_reasoner/playground_MvN/OperatorReplacements/4.Boxplus_to_singleton_Until/4b.program_only/data/original/dataset_original.txt") as file:
    data = file.readlines()
with open("meteor_reasoner/playground_MvN/OperatorReplacements/4.Boxplus_to_singleton_Until/4b.program_only/data/original/program_original.txt") as file:
    program = file.readlines()

D = load_dataset(data)
D_index = build_index(D)
rules = load_program(program)
for i in range(1,5):
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


# Replacement Syntax: Boxplus to singleton Diamondplus and Until

print("REPLACEMENT SYNTAX: Boxplus to singleton Diamondplus and Until")

with open("meteor_reasoner/playground_MvN/OperatorReplacements/4.Boxplus_to_singleton_Until/4b.program_only/data/replaced/dataset_replaced_i.txt") as file:
    data = file.readlines()
with open("meteor_reasoner/playground_MvN/OperatorReplacements/4.Boxplus_to_singleton_Until/4b.program_only/data/replaced/program_replaced_i.txt") as file:
    program = file.readlines()

D = load_dataset(data)
D_index = build_index(D)
rules = load_program(program)
for i in range(1,5):
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



# Replacement Syntax: Boxplus to singleton Until

# print("REPLACEMENT SYNTAX: Boxplus to singleton Until")

# with open("meteor_reasoner/playground_MvN/OperatorReplacements/4.Boxplus_to_singleton_Until/4b.program_only/data/replaced/dataset_replaced_ii.txt") as file:
#     data = file.readlines()
# with open("meteor_reasoner/playground_MvN/OperatorReplacements/4.Boxplus_to_singleton_Until/4b.program_only/data/replaced/program_replaced_ii.txt") as file:
#     program = file.readlines()

# D = load_dataset(data)
# D_index = build_index(D)
# rules = load_program(program)
# for i in range(1,5):
#     print("Iteration:", i)
#     print("=====================")
#     print("Before D:")
#     print_dataset(D)
#     print("Derived facts:")
#     delta_new = naive_immediate_consequence_operator(rules, D, D_index)
#     print_dataset(delta_new)
#     print("After D:")
#     materialize(D, rules, K=1)
#     print_dataset(D)