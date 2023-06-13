def maxvowels(s,k):
        count = 0
        value = 0
        vowels= ['a','e','i','o','u']


        i =0
        while (i+k-1) < len(s):
            for x in s[i:k+i]:
                if x in vowels:
                    value += 1
                    print(x)
            print(s[i:k+i] ,"::" , value)
            i +=1
            if value > count:
                count = value
            value = 0
        return count
s = "abciiidef"
k =3
print(maxvowels(s,k))