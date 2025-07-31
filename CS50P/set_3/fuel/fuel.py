while True:
    try:
        user_input = input("Provide fraction as x/y (e.g. 1/3): ")
        x,y = map(float, user_input.split('/'))
    except ValueError:
        pass
    else: 
        if  x >= 0 and x >= 0:
            z = x / y
        print(x, y)