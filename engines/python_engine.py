import ast

class PythonEngine:
    def analyze(self, code, filename):
        issues = []
        try:
            ast.parse(code)
        except SyntaxError as e:
            issues.append({"file": filename, "line": e.lineno, "message": str(e)})
        return issues