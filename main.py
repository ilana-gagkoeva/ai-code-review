import sys
from analyzer import analyze_project

path = sys.argv[1]

results = analyze_project(path)

for r in results:
    print(r)