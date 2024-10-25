# ディクショナリーの定義
person = { "name ": "haruna", "age": "29", "city": "Japan"}

# キーと値を巡回
for key in person:
    print(f"key: {key}, Value: {person[key]}")  # key: name , Value: haruna
print()                                                # key: age, Value: 29
                                                # key: city, Value: Japan
        
                                                                                               
# items() メソッドを作用した巡回
for key, value in person.items():
    print(f"key:{key} , value:{value}")   # 上と同様の結果を出力
print()    
    
    
# keys() メソッドを作用した巡回                                        
for key in person.keys():
    print(f"key: {key}")        # key: name
print()                         # key: age
                                # key: city                              
                                                
 
# values() メソッドを作用した巡回  
for value in person.values():
    print(f"value: {value}")        # value: haruna
                                    # value: 29
                                    # value: Japan                                      