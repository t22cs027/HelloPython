import random

def janken(player1, player2, player3):
    janken_dict = {'グー': 0, 'チョキ': 1, 'パー': 2}
    
    hands = [player1, player2, player3]
    unique_hands = set(hands)
    
    # 1. 全員が同じ手を出した場合は引き分け
    if len(unique_hands) == 1:
        return "引き分け"
    
    # 2. グー、チョキ、パーが全て揃った場合も引き分け
    if len(unique_hands) == 3:
        return "引き分け"
    
    # 3. グー vs チョキ vs パーの勝者を判定
    # グーが勝つ場合
    if 'グー' in hands and 'チョキ' in hands and 'パー' not in hands:
        winner = 'グーを出した人'
    # パーが勝つ場合
    elif 'パー' in hands and 'グー' in hands and 'チョキ' not in hands:
        winner = 'パーを出した人'
    # チョキが勝つ場合
    elif 'チョキ' in hands and 'パー' in hands and 'グー' not in hands:
        winner = 'チョキを出した人'
    
    # どのプレイヤーが勝者かを返す
    if winner == 'グーを出した人':
        if player1 == 'グー':
            return "Aの勝ち"
        elif player2 == 'グー':
            return "Bの勝ち"
        else:
            return "Cの勝ち"
    
    elif winner == 'パーを出した人':
        if player1 == 'パー':
            return "Aの勝ち"
        elif player2 == 'パー':
            return "Bの勝ち"
        else:
            return "Cの勝ち"
    
    elif winner == 'チョキを出した人':
        if player1 == 'チョキ':
            return "Aの勝ち"
        elif player2 == 'チョキ':
            return "Bの勝ち"
        else:
            return "Cの勝ち"

# 3回勝負の実行
def janken_best_of_3():
    choices = ['グー', 'チョキ', 'パー']
    a_wins = 0
    b_wins = 0
    c_wins = 0
    rounds = 3
    
    for i in range(1, rounds + 1):
        # ランダムに手を選ぶ
        player1 = random.choice(choices)
        player2 = random.choice(choices)
        player3 = random.choice(choices)

        # 勝敗結果を取得
        result = janken(player1, player2, player3)

        # 結果に応じてカウントを更新
        if result == "Aの勝ち":
            a_wins += 1
        elif result == "Bの勝ち":
            b_wins += 1
        elif result == "Cの勝ち":
            c_wins += 1
        
        # 出力結果を指定フォーマットで表示
        print(f"【第{i}回】Aの手: {player1} v.s. Bの手: {player2} v.s. Cの手: {player3} → {result}")
    
    # 最終結果の判定
    if a_wins > b_wins and a_wins > c_wins:
        print(f"\n最終結果: Aが{a_wins}勝、Bが{b_wins}勝、Cが{c_wins}勝 → Aの勝利！")
    elif b_wins > a_wins and b_wins > c_wins:
        print(f"\n最終結果: Aが{a_wins}勝、Bが{b_wins}勝、Cが{c_wins}勝 → Bの勝利！")
    elif c_wins > a_wins and c_wins > b_wins:
        print(f"\n最終結果: Aが{a_wins}勝、Bが{b_wins}勝、Cが{c_wins}勝 → Cの勝利！")
    else:
        print(f"\n最終結果: Aが{a_wins}勝、Bが{b_wins}勝、Cが{c_wins}勝 → 引き分け！")

# 3回勝負の実行
janken_best_of_3()