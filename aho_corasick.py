from collections import deque, defaultdict

# Wzorce do wyszukiwania
patterns = ["he", "she", "his", "hers"]
text = "ushers"

# Budowanie trie
trie = defaultdict(dict)
output = defaultdict(list)
new_node = 1

for pattern in patterns:
    node = 0
    for char in pattern:
        if char not in trie[node]:
            trie[node][char] = new_node
            new_node += 1
        node = trie[node][char]
    output[node].append(pattern)

fail = {0: 0}
queue = deque()

for char, node in trie[0].items():
    fail[node] = 0
    queue.append(node)

while queue:
    current = queue.popleft()
    for char, next_node in trie[current].items():
        queue.append(next_node)
        fail_state = fail[current]
        while fail_state and char not in trie[fail_state]:
            fail_state = fail[fail_state]
        fail[next_node] = trie[fail_state].get(char, 0)
        output[next_node].extend(output[fail[next_node]])

node = 0
results = []

for i, char in enumerate(text):
    while node and char not in trie[node]:
        node = fail[node]
    node = trie[node].get(char, 0)
    for pattern in output[node]:
        results.append((i - len(pattern) + 1, pattern))

print("Matches found:")
for start_index, pattern in results:
    print(f"Pattern '{pattern}' found at index {start_index}")
