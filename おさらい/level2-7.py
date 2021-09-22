# バグを修正して入力した名前を表示するようにしてください。
# ただし関数内（3～5行目）を変更しないでください。
from os import name


def kansu():
    name = input("名前を入力してください：")
    print(name)
    return name

kansu()