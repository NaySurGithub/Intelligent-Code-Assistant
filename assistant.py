import sys
import time
from core.analyzer import Analyzer
from core.report import Report
from exports.exporter import Exporter

def main():
    print("=== Intelligent Code Assistant ===")
    lang = input("Language (python/js): ").strip().lower()
    path = input("Path to file or directory: ").strip()
    mode = input("Export report? (json/txt/none): ").strip().lower()
    start = time.time()
    analyzer = Analyzer(lang, path)
    issues, score = analyzer.run()
    report = Report(issues, score)
    report.display()
    if mode in ["json", "txt"]:
        Exporter.export(report, mode)
    print(f"Analysis completed in {round(time.time() - start, 2)}s")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\nInterrupted")