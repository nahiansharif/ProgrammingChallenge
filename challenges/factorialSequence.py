def factorialSequence(n):
    fs = 1
    for i in range(n, 0, -1):
        fs = fs * i

    print(fs)


    return True

factorialSequence(6)