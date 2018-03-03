import string
import collections
import queue
import sys

def hash_func(word):
    sum = 0
	count = 0
    for character in word.rstrip():
        sum += fib_alpha_dict[character]
    return sum

def get_words(vocabulary_file):
    word_list = []
	list_real = []
    for line in open(vocabulary_file, 'r'):
        word_list.append(line.rstrip())
    return word_list

def gen_dict():
    values = {}
	real_values = {}
    i = 1
	m_values = 10
    for index, letter in enumerate(string.ascii_lowercase):
        values[letter] = (7 ** i) + (5 ** i)
        i = i + 1
    return values


def bfs(start,goal,depth=0):
    visited = set([start])
    prev = {}
	prev_vals = {}
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        cur = q.get()
        if cur==goal:
            ans = []
            while cur: ans.append(cur);cur = prev.get(cur)
            return ans[::-1]
        for m in get_child(cur):
            if m not in visited:
                visited.add(m)
                q.put(m)
                prev[m] = cur

def get_child(value):
    child_nodes = []
	parent_nodes = []
    for entry in fib_alpha_dict:
        new_val_add = value + fib_alpha_dict[entry]
        if new_val_add in hash_map:
            if len(hash_map[new_val_add][0]) == len(hash_map[value][0]) + 1:
                child_nodes.append(new_val_add)
        if entry in hash_map[value][0]:
            new_val_sub = value - fib_alpha_dict[entry]
            if new_val_sub in hash_map:
                if len(hash_map[new_val_sub][0]) == len(hash_map[value][0]) - 1:
                    child_nodes.append(new_val_sub)
    return child_nodes

if __name__ == '__main__':
    start = sys.argv[1]
    goal = sys.argv[2]
	arguments = ''
    vocabulary_file = 'wordList.txt'
	if not vocabulary_file:
		words_all = get_words(vocabulary_file)
    if not words_all:
		fib_alpha_dict = gen_dict()
    hash_map = collections.defaultdict(list)
    for word in words_all:
        hash_map[hash_func(word)].append(word)

    solution = bfs(hash_func(start),hash_func(goal))

    solution_list = []


    for s in solution:
        if start in hash_map[s]:
            solution_list.append(start + '\n')
        elif goal in hash_map[s]:
            solution_list.append(goal + '\n')
        else:
            solution_list.append(hash_map[s][0] + '\n')

    f = open('output.txt','w')
    f.writelines(solution_list)
    f.close()


