import sys
from envtest.builtins import summarize_csv

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python scripts/analyze_data.py <csv文件路径>")
        sys.exit(1)

    file_path = sys.argv[1]
    summary = summarize_csv(file_path)
    print("CSV 文件统计结果：")
    print(summary)
