from functools import partial
import re

str  = "ujwal!@%$#5ff./,gdf52e**67gme6&"

pattern = "[0-9A-Za-z,\\.{}[]|\\\\\?\\/]"

matches = re.findall(pattern,str)
print(matches)