### 実装方法
1. **parse_input関数**:
    - 標準入力から経路データを読み取り、タプルのリストとして返す。
    - 各タプルは、始点、終点、距離とする。

2. **find_longest_path関数**:
    - ベルマンフォード法を改良したアルゴリズム。
    - 始点と終点以外では同じ頂点を含まない条件を含む。
    - timeoutで指定した時間以内に処理が終了しない場合、その時点での最長経路を返す。

### プログラムの実行
    ```
    python [bellman_ford.py](http://_vscodecontentref_/0)
    ```

### ファイル構成
- `bellman_ford.py`: 最長経路を求めるためのメインプログラム。
- `README.md`: このファイル。プログラムの説明と使用方法を記載。
