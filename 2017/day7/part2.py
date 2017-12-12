class Node:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.children = []


    def addChild(self, child):
        self.children.append(child)


    def get_combined_weight(self):
        return self.weight + sum([child.get_combined_weight() for child in self.children])


    def __repr__(self):
        return 'Node: ' + self.name + ' children: ' + ', '.join([child.name for child in self.children])


def parseLine(line):
    import re
    [root, weight, _, children] = re.match(r'(\w+) \((\d+)\)( -> ([\w ,]*))?', line).groups()
    weight = int(weight)

    if children:
        children = [child.strip() for child in children.split(',')]
    else:
        children = []

    return [root, weight, children]


def find_imbalance(node):

# for children of node:
#   get weights
#   if weights are unbalanced:
#       get first child weight of unbalanced stack
#       return first child weight + weight inbalance

    child_weights = [(child, child.weight, child.get_combined_weight()) for child in node.children]

    if len(set(combined_weight for [_, _, combined_weight] in child_weights)) > 1:
        print child_weights

    for child in node.children:
        find_imbalance(child)


nodes = {}
parents = {}
with open('input.txt') as input_file:
    for line in input_file:
        [name, weight, children] = parseLine(line)
        nodes[name] = Node(name, int(weight))
        if name not in parents:
            parents[name] = None

        for child in children:
            parents[child] = name

for name, node in nodes.items():
    parent_name = parents[name]
    if parent_name is not None:
        nodes[parent_name].addChild(node)
    else:
        root_node = node

find_imbalance(root_node)
