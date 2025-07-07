# log_parser
Pythonでログファイルを解析・集計・出力するスクリプトです
# ログファイル自動解析ツール

## 📌 概要

本ツールは、業務で発生するログファイル（.txt）を対象に、  
エラーメッセージの抽出、件数の集計、およびレポート出力を行うPythonスクリプトです。  
定期的なログ監視、障害検知、運用報告業務など、  
**時間単価ベースの業務支援や継続的な保守作業の一環として活用できる設計**となっています。

## ⚙️ 使用技術・ライブラリ

- Python 3.x
- pandas
- re（正規表現）
- argparse（CLI操作用）

## 💻 機能一覧

- 任意のログファイルを指定して読み込み
- 特定パターンのエラーメッセージ抽出
- エラー件数の集計とCSV出力
- オプションによる日付や種類でのフィルタ機能（予定）

## 📂 ファイル構成

```plaintext
log_parser/
├── main.py            # メイン処理
├── parser/
│   ├── reader.py      # ログ読み込み処理
│   ├── analyzer.py    # ログ解析・抽出処理
│   └── writer.py      # CSV出力処理
├── data/
│   └── sample.log     # サンプルログファイル
├── output/
│   └── result.csv     # 出力結果（生成される）
└── README.md
```



## 🔧 使い方（実行コマンド例）

```bash
python main.py --input data/sample.log --output output/result.csv
```


## 🔮 今後の機能追加予定（開発計画）
- GUI対応（Tkinter or Streamlit）
- ログの種類別の分類機能
- 処理速度の最適化


📜 ライセンス  
This project is licensed under the MIT License.  
利用・改変・再配布は自由ですが、著作権表記の保持をお願いいたします。


