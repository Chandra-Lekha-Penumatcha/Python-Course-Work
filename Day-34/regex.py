import re 

pattern = r'[0-9]'
text = 'codegnan' 

res = re.match(pattern,text)
print(res.group() if res else "Pattern not found")

import re 

pattern = 'code'
text = 'codegnan' 

res = re.match(pattern,text)
print(res.group() if res else "Pattern not found")

#search - search for entire pattern #match- used to search for return if it found the first match

import re

pattern = 'code'
text = 'codegnan2026'

res = re.search(pattern,text)
print(res.group() if res else "Pattern not found")
# findall-IT will give output as list of patterns

import re

pattern = 'code'
text = 'codegnan 2026 python version 3.14'

res = re.findall(pattern,text)
print(res)
#print(res.group() if res else "Pattern not found")
#finditer-returns an iterator of Match objects.Indexing,Matched text
# Starting index
# Ending index
import re

pattern = r'[0-9]'
text = 'codegnan 2026 python version 3.14'

res = re.finditer(pattern,text)
for i in res:
    print(i.group(),i.start())
print(res)
#fullmatch-validation ,Use exact length,exact pattern need to be match

import re

pattern = r'[0-9]{10}'
text = '9876543210'

res = re.fullmatch(pattern,text)
#for i in res:
print(res.group() if res else "Pattern not found")
#split:splits a string wherever the given pattern matches.
import re 

pattern = r'[,(#]'
text = 'java,python(html#css'

res = re.split(pattern,text)
print(res)
#sub-replace the function
import re

pattern = r'[a-z]'
text = 'python version 3.14, batch-63'

res = re.sub(pattern,'*',text)
print(res)

import re 
pattern = r'e.t'
text = 'e@t eaat eat eet ett ect Egfhjet hgjeokj'

res = re.findall(pattern,text)
print(res)

import re
pattern = r'^0678$'
text = '098765432109'
res = re.findall(pattern,text)
print(res)

import re

pattern = r'to+'
text = 'to tdfghjk too tooo toooo'

res = re.findall(pattern,text)
print(res)

import re 

pattern = r'ab+'
text = 'ab abbb a abbbbb abbbbbb'

res = re.findall(pattern,text)
print(res)

import re 

pattern = r'910'
text = '05678'

res = re.findall(pattern,text)
print(res)