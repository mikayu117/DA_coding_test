import sys
import time
from collections import defaultdict
from typing import List, Tuple, Dict

def parse_input() -> List[Tuple[int, int, float]]:
    """標準入力から経路データを読み取る"""
    edges = []
    for line in sys.stdin:
        parts = [part.strip() for part in line.strip().split(',')]
        if len(parts) != 3:
            continue
        try:
            start = int(parts[0])
            end = int(parts[1])
            distance = float(parts[2])
            edges.append((start, end, distance))
        except ValueError:
            # 数値に変換できない場合はスキップ
            continue
    return edges

def find_longest_path(edges: List[Tuple[int, int, float]], timeout: float) -> List[int]:
    """ベルマンフォード法を使用して最長経路を見つける"""
    start_time = time.time()
    
    # グラフの頂点を収集
    vertices = set()
    for s, e, _ in edges:
        vertices.add(s)
        vertices.add(e)
    
    # グラフを隣接リストとして構築
    graph = defaultdict(dict)
    for s, e, d in edges:
        graph[s][e] = d
        graph[e][s] = d  # 無向グラフにするため
    
    # ベルマンフォード法による最長経路探索
    def bellman_ford(start: int) -> Dict[int, List[int]]:
        # 初期化
        dist = {v: float('-inf') for v in vertices}
        dist[start] = 0
        paths = {v: [] for v in vertices}
        paths[start] = [start]
        
        # |V|-1回の反復
        for _ in range(len(vertices) - 1):
            updated = False
            for u in vertices:
                for v in graph[u]:
                    # 既に訪問済みの頂点はスキップ
                    if v in paths[u]:
                        continue
                    
                    new_dist = dist[u] + graph[u][v]
                    # 始点からの距離が更新された場合、経路も更新
                    if dist[u] != float('-inf') and new_dist > dist[v]:
                        dist[v] = new_dist
                        paths[v] = paths[u] + [v]
                        updated = True

            # 更新がない場合、終了
            if not updated:
                break
        
        return paths
    
    # 全ての頂点から探索
    max_length = float('-inf')
    best_path = None
    
    for start in vertices:
        # タイムアウトのチェック
        if time.time() - start_time > timeout:
            print("処理がタイムアウトしました")
            return best_path
        
        paths = bellman_ford(start)
        
        # サイクルを含む経路も考慮
        for end in vertices:
            if not paths[end]:
                continue
            
            # 経路の長さを計算
            path = paths[end]
            if len(path) < 2:
                continue
                
            # 経路が存在する場合、サイクルの可能性を確認
            if path[-1] in graph[start]:
                cycle_path = path + [start]
            else:
                cycle_path = path
            
            # 距離を計算
            distance = sum(graph[cycle_path[i]][cycle_path[i+1]] 
                         for i in range(len(cycle_path)-1))
            
            # 今までのすべての経路よりも長い場合、更新
            if distance > max_length:
                max_length = distance
                best_path = cycle_path

    return best_path

def main():
    edges = parse_input()
    timeout = 10  # タイムアウト時間（秒）
    
    path = find_longest_path(edges, timeout)
    
    if path:
        for vertex in path:
            sys.stdout.write(f"{vertex}\r\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()