words = "It's thanksgiving day. It's my birthday,too!"
print(words.replace("day", "month", 1))
print(words.find("day"))



x = [2,54,-2,7,12,98]
print(max(x), min(x))



y = []
z = ["hello",2,54,-2,7,12,98,"world"]
y.append(z[0])
y.append(z[len(z) -1])
print(y)



w = [19,2,54,-2,7,12,98,32,10,-3,6]
new_w = w[:len(w)/2]
new_w.append(w[len(w)/2:])
print(sorted(w), new_w)

    
