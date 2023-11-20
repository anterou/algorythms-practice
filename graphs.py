from collections import deque 
graph = {
    'Wake up': ['Exersice', 'Brush teeth', 'Pack a meal'],
    'Exersice': ['Take a bath'],
    'Take a bath': ['Get dressed'],
    'Brush teeth': ['Eat'], 
}
def already_eaten(action):
    if action == "Eat":
        return True
def search(start, goal):
    search_queue = deque()
    search_queue.append((start, 0))  
    searched = set()  

    while search_queue:
        node, distance = search_queue.popleft()
        if node == goal:
            return distance

        if node not in searched:
            searched.add(node)
            neighbors = graph.get(node, [])
            for neighbor in neighbors:
                search_queue.append((neighbor, distance + 1))

    return -1  
start = "Wake up"
goal = "Eat"
steps = search(start, goal)
print(f"Steps: {steps}")
