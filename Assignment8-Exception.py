try:
    print('try block')
    x = 20
    y = 0
    z = x / y
except ZeroDivisionError:
    print("except ZeroDivisionError block")
    print("Division by 0 is not accepted")
else:
    print("else block")
    print("Division : ", z)
finally:
    print("finally block")
print("Out of try, except, else and finally blocks.")
