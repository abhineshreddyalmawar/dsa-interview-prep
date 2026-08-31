# PHASE B - DAY 4 (Aug 4, 2026) | Graphs & DFS (Depth-First Search)
# Real-world tie-in: Amtrak route network - any city can connect to any number of others, any direction

# --- graph as adjacency list : dict of lists ---
routes = {
    "Newark": ["New York", "Philadelphia", "Trenton"],
    "New York": ["Newark"],
    "Philadelphia": ["Newark", "Trenton"],
    "Trenton": ["Newark", "Philadelphia"]
}
# unlike a tree, no fixed max connections - just .append() more as needed

# --- set() : fast unique membership tracking (same hashing as dicts) ---
visited = set()
visited.add("Newark")
print("Newark" in visited)   # True - O(1) check, same mechanism as dict

# --- DFS : recursion, same shape as tree traversal, adapted for N neighbors ---
def visit_all(city, visited):
    if city in visited:        # base case - already been here, stop this path
        return
    visited.add(city)           # visited is ONE SHARED set across ALL recursive calls
    print(city)
    for neighbor in routes[city]:   # loop instead of fixed .left/.right
        visit_all(neighbor, visited)

visited = set()
visit_all("Newark", visited)
# Newark, New York, Philadelphia, Trenton
# (goes as deep as possible down ONE path before backtracking - that's "depth-first")

# --- why it doesn't infinite-loop on cycles (Philadelphia <-> Trenton <-> Newark) ---
# visited is passed by reference into every recursive call - same object, not a copy.
# Once Newark is added at the very start, every later path checking "Newark in visited"
# sees it as True, no matter how many hops away that check happens.