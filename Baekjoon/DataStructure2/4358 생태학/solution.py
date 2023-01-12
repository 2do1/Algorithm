import sys

trees = {}
total_trees = 0
while True:
    tree = sys.stdin.readline().strip()

    if not tree:
        break

    if tree not in trees:
        trees[tree] = 1
        total_trees += 1
    else:
        trees[tree] += 1
        total_trees += 1

for key, value in sorted(trees.items()):
    print("%s %0.4f" %(key, value / total_trees * 100))