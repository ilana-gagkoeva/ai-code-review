import os
import subprocess
from llm import analyze_with_llm


def get_python_files(path):
    files = []
    for root, _, filenames in os.walk(path):
        for f in filenames:
            if f.endswith(".py"):
                files.append(os.path.join(root, f))
    return files


def run_ruff(file_path):
    try:
        result = subprocess.run(
            ["ruff", file_path],
            capture_output=True,
            text=True
        )
        return result.stdout.strip().split("\n") if result.stdout else []
    except:
        return []


def analyze_project(path):
    results = []

    files = get_python_files(path)

    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()

        lint_issues = run_ruff(file)
        llm_issues = analyze_with_llm(code)

        results.append({
            "file": file,
            "issues": lint_issues + llm_issues
        })

    return results