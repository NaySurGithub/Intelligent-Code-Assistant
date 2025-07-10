import esprima

class JSEngine:
    def analyze(self, code, filename):
        issues = []
        try:
            esprima.parseScript(code)
        except esprima.Error as e:
            issues.append({"file": filename, "line": 1, "message": str(e)})
        return issues