#metacharacters '.'
import re
a=re.search(r'AT.G.C','ATCGAC').group()
#Uses re.search to find the first match of the pattern AT.G.C in the string 'ATCGAC'. The . metacharacter matches any single character except a newline.
#.group(): Extracts the matched string. The pattern AT.G.C matches 'ATCGAC' because . can be replaced by any character, making T match T and C match C.
print(a)

'''
output
ATCGAC
'''



#metacharacter '^' - caret. Matches the start of the string
import re
seq="AUGAGCUAGC"
a=re.search(r'^AUG',seq).group()
print(a)

'''
output
AUG
'''

import re
seq="AUGAGCUAGC"
a=re.search(r'^GUA',seq)
print(a)

'''
output
None
'''


#metacharacter '$' -> Matches the end of the string
import re
a=re.search(r'UAG$','AUGCGAUCAGUAG')
print(a)

'''
output
<re.Match object; span=(10, 13), match='UAG'>
'''

import re
a=re.search(r'UAG$','AUGCGAUCAGUAGAA')
print(a)

'''
output
None
'''



#metacharacter '[]' -> they are used for specifying a character class, which is a set of characters that you wish to match
#[a-z] or [0-9]   character set
#[a-zA-Z0-9]   matches any letter from (a to z) or (A to Z) or (0 to 9)





#metacharacter '\' 
'''
\w - matches any single letter, digit or underscore
\W - matches any character not part of \w
\s - matches a single white space character like space, newline, tab, return
\S - matches any character not part of \s
\d - matches decimal digit 0-9
\D - matches any character that is not a decimal digit 
'''



#metacharacter '*' -> repeat things    matches zero or more times
import re
a=re.search(r'ca*t','ct')
print(a)

'''
output
<re.Match object; span=(0, 2), match='ct'>
'''

import re
a=re.search(r'ca*t','cat')
print(a)

'''
output
<re.Match object; span=(0, 3), match='cat'>
'''

import re
a=re.search(r'ca*t','caaat')
print(a)

'''
output
<re.Match object; span=(0, 5), match='caaat'>
'''

import re
a=re.search(r'ca*t','rat')
print(a)

'''
output
None
''' 





#metacharacter '+' ->  matches one or more times
import re
str="Bioinformatics"
a=re.search(r'i+o',str)
print(a)

'''
output
<re.Match object; span=(1, 3), match='io'>
'''

import re
str="Biinformatics"
a=re.search(r'i+o',str)
print(a)

'''
output
None
'''

import re
str="Bioinformaticso"
a=re.search(r'i+o',str)
print(a)

'''
output
<re.Match object; span=(1, 3), match='io'>
'''


