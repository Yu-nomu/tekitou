# 数字処理スクリプト統合版
# 1から10までの数字表示と二乗計算を行う関数を含むPythonスクリプト

def display_numbers():
    """1から10までの数字を順番に表示する関数"""
    print("数字を1から10まで表示します:")
    print()
    
    # for文を使って1から10まで表示
    for i in range(1, 11):
        print(f"{i}")
    
    print()
    print("完了しました！")


def calculate_squares():
    """1から10までの数字を二乗（同じ数字で掛け算）して結果を表示する関数"""
    print("1から10までの数字の二乗を表示します:")
    print("=" * 30)
    
    # for文を使って1から10まで二乗計算
    for i in range(1, 11):
        result = i * i
        print(f"{i} × {i} = {result}")
    
    print("=" * 30)
    print("二乗計算が完了しました！")


def main():
    """メイン関数：ユーザーに選択肢を提供して実行する"""
    print("=" * 50)
    print("数字処理スクリプト")
    print("=" * 50)
    print("1. 数字を1から10まで表示")
    print("2. 数字の二乗計算（1から10）")
    print("3. 両方実行")
    print("4. 終了")
    print("=" * 50)
    
    while True:
        try:
            choice = input("選択してください (1-4): ")
            
            if choice == "1":
                print("\n--- 数字表示 ---")
                display_numbers()
                break
            elif choice == "2":
                print("\n--- 二乗計算 ---")
                calculate_squares()
                break
            elif choice == "3":
                print("\n--- 数字表示 ---")
                display_numbers()
                print("\n--- 二乗計算 ---")
                calculate_squares()
                break
            elif choice == "4":
                print("プログラムを終了します。")
                break
            else:
                print("無効な選択です。1-4の数字を入力してください。")
        except KeyboardInterrupt:
            print("\n\nプログラムを終了します。")
            break
        except Exception as e:
            print(f"エラーが発生しました: {e}")


if __name__ == "__main__":
    main()