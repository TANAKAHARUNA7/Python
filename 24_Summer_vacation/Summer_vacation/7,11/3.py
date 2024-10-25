# 리터럴(Litral)사용한 생성
my_dict = {'name': 'Alice', 'age': 25}

# 키워드 인자 사용
my_dict = dict(name = "Alice", age = 25, country = "USA")
print(my_dict)

# 튜플 리스트 사용
paris = [("name", "Alice"), ("age", 25), ("country", "USA")]
my_dict = dict(paris)
print(my_dict)

# 키 리스트와 zip 사용
keys = ["name", "age", "country"]
values = ["Alice", 25, "USA"]
my_dict = dict(zip(keys,values))
print(my_dict)