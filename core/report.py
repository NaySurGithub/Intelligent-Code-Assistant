from termcolor import colored
import json

class Report:
    def __init__(self, issues, score):
        self.issues = issues
        self.score = score
    def display(self):
        print(colored(f"Code Quality Score: {self.score}/100", "cyan"))
        for issue in self.issues:
            print(colored(f"[{issue['file']}] Line {issue['line']}: {issue['message']}", "red"))
    def to_dict(self):
        return {"score": self.score, "issues": self.issues}