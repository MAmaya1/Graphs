def earliest_ancestor(ancestors, node):
    valid_node = False
    for parent in ancestors:
            if parent[1] == node:
                valid_node = True
                break
    if valid_node == False:
        return -1

    q = []
    q.append([node])
    visited = set()

    while len(q) > 0:
        path = q.pop(0)
        current = path[-1]
    
        if current not in visited:
            visited.add(current)
        
        no_parent = False

        for parent in ancestors:
            if parent[1] == current:
                path_copy = list(path)
                path_copy.append(parent[0])
                q.append(path_copy)
                no_parent = True

        if no_parent == False:
            q.append(list(path))
            break

    earliest = []
    
    for path in q:
        if len(path) > len(earliest):
            earliest = list(path)
        elif len(path) == len(earliest):
            if path[-1] < earliest[-1]:
                earliest = list(path)

    return earliest[-1]