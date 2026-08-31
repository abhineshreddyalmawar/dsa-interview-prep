# SYSTEM DESIGN - DAY 1 (Aug 6, 2026) | Client-Server Fundamentals
# Real-world tie-in: NexusAI Portal - browser (client) requests analysis, Flask backend (server) does the work

from flask import Flask

app = Flask(__name__)          # __name__ is boilerplate - always written this way

# --- reusing Phase A's RepoAnalyzer class, completely unchanged ---
class RepoAnalyzer:
    def __init__(self, github_username, repo_name):
        self.github_username = github_username
        self.repo_name = repo_name
        self.rating = None

    def analyze(self):
        self.rating = 8
        return f"Analyzing {self.repo_name} for user {self.github_username}"

# --- @app.route() : connects a URL path to a function ---
# whatever this function returns becomes the HTTP response
@app.route("/analyze")
def analyze():
    a = RepoAnalyzer("abhineshreddyalmawar", "nexusai-portal-v2")
    result = a.analyze()
    return result
# a browser visiting yoursite.com/analyze triggers this exact function

# --- WHY client/server split exists ---
# If analysis logic (incl. the Anthropic API key from .env) ran INSIDE the browser,
# any user could open dev tools and read the key directly -> billed to your account.
# Server keeps secrets private; browser only ever sees the RESULT, never the key.

# simulate a request without running a live server:
with app.test_request_context():
    print(analyze())
# Analyzing nexusai-portal-v2 for user abhineshreddyalmawar