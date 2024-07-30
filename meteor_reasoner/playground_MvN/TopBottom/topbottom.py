from meteor_reasoner.materialization.materialize import *
from meteor_reasoner.utils.loader import load_dataset, load_program

with open("meteor_reasoner/playground_MvN/TopBottom/data/topbottom_dataset.txt") as file:
    data = file.readlines()
with open("meteor_reasoner/playground_MvN/TopBottom/data/topbottom_program.txt") as file:
    program = file.readlines()


D = load_dataset(data)
D_index = build_index(D)
rules = load_program(program)
for i in range(1,10):
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

# Bug found: If Top/Bottom is both in the dataset and in one of the rule bodies, an error is thrown
# Top/Bottom is in literals and in delta_old in function seminaive_join
# Then ultimately line 121 is called: ground_body(global_literal_index+1, delta, context)
# This command has only 3 parameters instead of the required 4; visited is missing.
# Fix: just insert the missing 'visited'.