a=19

try:
    c=a/b
except ZeroDivisionError:
    print("nahi hog bruv")
except TypeError:
    print('gadhe')
except:
    print('lol')
else:
    print(c)
finally:
    print("bye fascist")
