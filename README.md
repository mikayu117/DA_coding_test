### 実装方法
1. **parse_input関数**:
    - 標準入力から経路データを読み取り、タプルのリストとして返します。
    - 各タプルは、始点、終点、距離を表します。

2. **find_longest_path関数**:
    - ベルマンフォード法を改良したアルゴリズムを使用して、最長経路を探索します。
    - 始点と終点以外では同じ頂点を含まない条件を加えています。
    - タイムアウト機能を追加し、指定された時間内に処理が完了しない場合は、その時点での最長経路を出力します。

### プログラムの実行
    ```
    python [bellman_ford.py](http://_vscodecontentref_/0)
    ```

### ファイル構成
- `bellman_ford.py`: 最長経路を求めるためのメインプログラム。
- `README.md`: このファイル。プログラムの説明と使用方法を記載。
