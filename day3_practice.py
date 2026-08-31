readme_text = "# MyProject\n## Installation\npip install mypackage\n## Usage\nRun the script"
print("Installation" in readme_text)
print("License" in readme_text )
required = ["Installation", "License"]
missing = []
for header in required:
    if header not in readme_text:
        missing.append(header)

print(missing)

#--------------
def find_missing_headers(readme_text, required):
    missing = []
    for header in required:
        if header not in readme_text:
            missing.append(header)
    return missing


readme_text = "# MyProject\n## Installation\npip install mypackage\n## Usage\nRun the script"
required = ["Installation", "Usage", "License"]

print(find_missing_headers(readme_text, required))
