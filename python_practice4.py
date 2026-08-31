# PHASE A - DAY 2 (Jul 25, 2026) | Classes & Basic OOP
# Real-world tie-in: NexusAI coordinator/subagent pattern - one blueprint, many independent analyzer objects

# --- class + __init__ : the blueprint and its starting data ---
class RepoAnalyzer:
    def __init__(self, github_username, repo_name):
        self.github_username = github_username   # self = "this specific object"
        self.repo_name = repo_name
        self.rating = None                        # placeholder - no result yet

    def analyze(self):
        self.rating = 8                            # permanently updates THIS object's data
        return f"Analyzing {self.repo_name} for user {self.github_username}"

# --- creating objects (instances) from the blueprint ---
analyzer1 = RepoAnalyzer("abhineshreddyalmawar", "nexusai-portal-v2")
analyzer2 = RepoAnalyzer("priya123", "cool-project")
print(analyzer1.repo_name)     # nexusai-portal-v2
print(analyzer2.repo_name)     # cool-project -- separate objects, separate data

# --- calling a method ---
print(analyzer1.analyze())
# Analyzing nexusai-portal-v2 for user abhineshreddyalmawar

# --- self.attribute sticks around after the method runs ---
print(analyzer2.rating)        # None -- analyze() never called on analyzer2
analyzer1.analyze()
print(analyzer1.rating)        # 8 -- permanently stored on the object

# --- coordinator pattern: loop spawns one object per repo automatically ---
repo_list = [
    ("abhineshreddyalmawar", "nexusai-portal-v2"),
    ("priya123", "cool-project"),
]

analyzers = []
for username, repo in repo_list:
    a = RepoAnalyzer(username, repo)
    analyzers.append(a)

for a in analyzers:
    print(a.analyze())
# Analyzing nexusai-portal-v2 for user abhineshreddyalmawar
# Analyzing cool-project for user priya123