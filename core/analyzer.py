import os
from engines.python_engine import PythonEngine
from engines.js_engine import JSEngine

class Analyzer:
    def __init__(self, language, target):
        self.language = language
        self.target = target
        self.engine = PythonEngine() if language == "python" else JSEngine()
    def run(self):
        files = []
        if os.path.isdir(self.target):
            for root, _, filenames in os.walk(self.target):
                for f in filenames:
                    if f.endswith(".py") and self.language == "python":
                        files.append(os.path.join(root, f))
                    elif f.endswith(".js") and self.language == "js":
                        files.append(os.path.join(root, f))
        else:
            files.append(self.target)
        all_issues = []
        for f in files:
            with open(f, "r", encoding="utf-8") as file:
                code = file.read()
                issues = self.engine.analyze(code, f)
                all_issues.extend(issues)
        score = max(0, 100 - len(all_issues))
        return all_issues, score