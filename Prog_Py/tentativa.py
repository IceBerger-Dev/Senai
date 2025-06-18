try:
    a = int(input('Digite um numero'))
    b = int(input('Digite outro número'))
    print((a/b))
except ValueError:
    print(ValueError)
except TypeError:
    print(TypeError)
except ZeroDivisionError:
    print(ZeroDivisionError)
# except IndentationError:
#     print(IndentationError)
