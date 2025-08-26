# decorators

def logtime(function):

    def wrapper():
        # do something before
        print("Before")
        val = function()
        # do something after
        print("after")
        return val
    
    return wrapper

@logtime
def hello():
    print("hello world")

hello()