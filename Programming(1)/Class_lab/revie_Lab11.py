# C温度の入力受けてF温度に変換する


def convert_celsius_to_fahrenheit(celsius):
    #　変換公式
    F = ( celsius * 9/5) + 32
    print("F温度は",F,"です")


c = int(input("C 温度を入力してください:"))
convert_celsius_to_fahrenheit(c)
