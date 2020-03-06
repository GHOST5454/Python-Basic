# Lets learn about regex.

import regex.regex as re

txt = "The Rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
