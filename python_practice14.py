# DAY 2 (Aug 11, 2026) | NeetCode: Valid Anagram + System Design: HTTP Methods & Receiving Data

# --- NEETCODE SOLO PRACTICE : Valid Anagram ---
# the flaw in the first instinct: checking just ONE char isn't enough
# "any char exists somewhere in the other string" != "same letters, same counts"
# proven false with: is_anagram("rat", "tax") -> would wrongly say True if only checking 1 char

def is_anagram(s, t):
    a = list(s)
    b = list(t)
    for char in b:
        if char in a:
            a.remove(char)      # .remove(value) - removes by VALUE, not position (Day 5)
        else:
            return False         # mismatch found - stop immediately
    return True                  # loop finished, every char in b matched something in a

print(is_anagram("anagram", "nagaram"))   # True
print(is_anagram("rat", "tax"))            # False - the exact case that broke the flawed version

# honest note: this is O(n^2) - char in a is O(n), done n times
# a faster O(n) version would count each letter once using a dict,
# same pattern as Day 2's counting exercise - worth revisiting as a "make it faster" follow-up


# --- SYSTEM DESIGN : HTTP Methods & Receiving Data ---
# Real-world tie-in: NexusAI submitting a GitHub username for analysis, not just fetching data

from flask import Flask, request

app = Flask(__name__)

# HTTP methods: GET (read) vs POST (submit/create) vs PUT (update) vs DELETE (remove)
# NexusAI: fetch saved report = GET | submit username = POST | update settings = PUT | delete report = DELETE

# restricting a route to POST, and reading submitted JSON data
@app.route("/analyze", methods=["POST"])
def analyze():
    username = request.json.get("username")   # same .get() safe-lookup as Phase A Day 3
    return f"Received username: {username}"

# simulate real POST requests with JSON data, without running a live server
with app.test_client() as client:
    response = client.post("/analyze", json={"username": "abhineshreddyalmawar"})
    print(response.get_data(as_text=True))
    # Received username: abhineshreddyalmawar

    response = client.post("/analyze", json={"username": "priya123"})
    print(response.get_data(as_text=True))
    # Received username: priya123