# exceptions

try: 
    # some line of code 
except <ERROR1>:
    # handle error1
except <ERROR2>:
    # handle error2
except <ERROR3>:
    # handle error3
except Exception as e:
    # handle any other exception
    print(f"An unexpected error occurred: {e}")
finally:
    # cleanup code, if necessary
    pass 