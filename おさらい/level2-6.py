# バグを修正してください。ただし修正してよいのは1行のみです。
from os import name

def kansu():
    print(name)

name = input("名前を入力してください：")
kansu()