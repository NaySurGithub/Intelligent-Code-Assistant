import json

class Exporter:
    @staticmethod
    def export(report, mode):
        if mode == "json":
            with open("report.json", "w", encoding="utf-8") as f:
                json.dump(report.to_dict(), f, indent=4)
        elif mode == "txt":
            with open("report.txt", "w", encoding="utf-8") as f:
                f.write(f"Code Quality Score: {report.score}/100\n")
                for issue in report.issues:
                    f.write(f"[{issue['file']}] Line {issue['line']}: {issue['message']}\n")