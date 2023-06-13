#Maximum Number of Vowels in a Substring of Given Length

def maxVowels(s: str, k: int) -> int:
        count = 0
        value = 0
        for i in range(0,len(s)-k +1):
            value =  s[i:k+i].count("a") + s[i:k+i].count("e")  + s[i:k+i].count("i") + s[i:k+i].count("o") +  s[i:k+i].count("u") 
            if value > count:
                count = value
        return count
s = "tryharder"
k = 4
print(maxVowels(s,k))