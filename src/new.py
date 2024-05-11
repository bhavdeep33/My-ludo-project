class Test:
    __a = "test"

test = Test()
print(test._Test__a)  # prints test
print(Test.a)  # raises Attribute error