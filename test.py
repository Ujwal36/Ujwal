file = open("touch.txt", "wt")
str = "there once was a fish and the fish was always eating once as there were no other fishes near that fish"
file.write(str)

file.close()


file = open("touch.txt", "rt")

contents = file.read()
contents = contents.split(" ")
dict ={}
count = 0
for word in contents:
    if word not in dict:
        count += 1
        dict.update({word : count})
        count = 0
    else:
        count = dict.get(word)
        count += 1
        dict.update({word : count})
        count = 0
print(dict)

file.close()