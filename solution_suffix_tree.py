import sys
from suffix_trees import STree

def longest_prefix_suffix():
    s = sys.stdin.read().strip()

    if not s:
        return
    
    n = len(s)
    stree = STree.STree(s)
    longest = 0

    for i in range (1, n):
        current_prefix = s[:i]
        if stree.find(current_prefix) != -1:
            if s.endswith(current_prefix):
                longest = len(current_prefix)
    
    print(f'Answer: {longest}')

if __name__ == '__main__':
    longest_prefix_suffix()