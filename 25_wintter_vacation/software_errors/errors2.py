
num = 2

try:
    print("10")
    
    if num == 1:
        raise ValueError
    else:
        raise KeyboardInterrupt
    
    print("20")

#　except は最低1個以上は必要
       
    
except ValueError:  # Javaではcatch
    print("30")
    
# except Exception:  # ほとんどの例外の親クラスなので、
#     print("21")    # 広範な例外をキャッチできる

# except ZeroDivisionError:
#     print("50")

except ArithmeticError:
    print("21")    
    
except:
    print("32")
    
print("40")