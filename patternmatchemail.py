str = "My email ID is: ujwal36k@gmail.com"
import re
pattern = "[0-9A-Za-z_.-]+@[0-9A-Za-z_.-]+"

x= re.findall(pattern,str)
print(x)