# 連絡帳情報を保存するディクショナリーを生成
# 各キーは連絡帳の属性を表し各値は割り当てた属性のデータ

contact = { "name": "John Doe", \
            "e-mail": "john.doe@example.com", \
            "phone": "123-456-7890"}

# 読む
# ディクショナリーで各キーを利用して連絡帳情報を読んで出力
print("Name: ", contact["name"])   # Name:  John Doe
print("e-mail: ", contact["e-mail"])  # e-mail:  john.doe@example.com
print("phone: ", contact["phone"])  # phone:  123-456-7890


# アップデート
# ディクショナリーのキーに新しい値を割り当て既存のデータをアップデートする
contact["e-mail"] = "new.email@example.com"
contact["phone"] = "987-654-3210"
contact["address"] = "1234 Main St"
print("\nUpdated: ", contact)  # Updated:  {'name': 'John Doe', 'e-mail': 'new.email@example.com', 'phone': '987-654-3210', 'address': '1234 Main St'}


# 削除
# "phone" キーと割り当てた値がディクショナリーから削除
del contact["phone"]
print("\nDeleted phone: ",contact)  # Deleted phone:  {'name': 'John Doe', 'e-mail': 'new.email@example.com', 'address': '1234 Main St'}




