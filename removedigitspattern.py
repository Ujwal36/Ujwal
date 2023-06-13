str = "Ujwal36k@gmail.com/06-04-1992"

import re
pattern = "[a-zA-Z]"
listalpha = re.findall(pattern,str)
print(listalpha)
output = "".join(listalpha)

print(output)