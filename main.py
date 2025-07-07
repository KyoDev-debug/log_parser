def show_log_preview(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            for i, line in enumerate(file):
                print(line.strip())
                if i >= 9:
                    break
    except FileNotFoundError:
        print("ログファイルが見つかりませんでした。")

if __name__ == "__main__":
    show_log_preview("data/sample.log")
