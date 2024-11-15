import random

def janken(player1, player2):
    janken_dict = {'グー': 0, 'チョキ': 1, 'パー': 2}
    
    result = (janken_dict[player1] - janken_dict[player2]) % 3
    
    if result == 0:
        return "引き分け"
    elif result == 1:
        return "Bの勝ち"
    else:
        return "Aの勝ち"

# ランダムに手を選ぶ
choices = ['グー', 'チョキ', 'パー']
player1 = random.choice(choices)
player2 = random.choice(choices)

# 勝敗結果を取得
result = janken(player1, player2)

# 出力結果を指定フォーマットで表示
print(f"Aの手: {player1} v.s. Bの手: {player2} → {result}")