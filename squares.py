# 1から10までの数字を二乗（同じ数字で掛け算）するPythonスクリプト

print("1から10までの数字の二乗を表示します:")
print("=" * 30)

# for文を使って1から10まで二乗計算
for i in range(1, 11):
    result = i * i
    print(f"{i} × {i} = {result}")

print("=" * 30)
print("二乗計算が完了しました！")