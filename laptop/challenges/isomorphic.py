def isomorphic(s, t):
    x = {}

    for i in range(len(s)):
        if s[i] not in x:
            x[s[i]] = t[i]

    print("_____________") 
    print(x)

    for i in range(len(t)):
        if t[i] not in x.values():
            return False

    return True


s = "egg"
t = "add"
print(s, t, isomorphic(s, t))

s = "foo"
t = "bar"
print(s, t, isomorphic(s, t))

s = "paper"
t = "title"
print(s, t, isomorphic(s, t))