'''
findall - returns a list containing all matches
search - returns a match object if there is a match anywhere in the string
split - returns a list where a string has been split at each match
sub - replaces one or many matches with a string
'''


#regular expression re 
#search - to find the matches in the whole string
import re
seq='ATGCCGATTGACATCGGAT'
a=re.search(r'TGA',seq)
print(a)

'''
output
<re.Match object; span=(8, 11), match='TGA'>
'''

import re
seq='ATGCCGATTGACATCGGAT'
a=re.search(r'UUU',seq)
print(a)

'''
output
None
'''

import re 
seq=("ATGCGATAGACGTGCAGAT")
x=re.search("^ATG.*GAT$",seq)     #.*: Match any character (except newline) 0 or more times.
print(x)

'''
output
<re.Match object; span=(0, 19), match='ATGCGATAGACGTGCAGAT'>
'''

import re 
seq=("ATGCGATAGACGTGCAGAT")
x=re.search("^ATG.GAT$",seq)    #.: This matches any single character (except newline characters). It means that there can be exactly one character between "ATG" and "GAT". 
print(x)

'''
output
none
'''

import re 
seq=("ATGCGATAGACGTGCAGAT")
x=re.search("^ATG*GAT$",seq)  #G*: The asterisk (*) is a quantifier that means "zero or more" of the preceding element. In this case, it means zero or more occurrences of "G".  
print(x)

'''
output
None
'''

import re 
seq=("ATGCGATAGACGTGCAGAT")
x=re.search(r"TAG",seq)    
print(x)
mt=re.match(r"TAG",seq)
print(mt)

'''
output
<re.Match object; span=(6, 9), match='TAG'>
None
'''

import re 
seq=("TAGATGCGATAGACGTGCAGAT")
x=re.search(r"TAG",seq)    
print(x)
mt=re.match(r"TAG",seq)
print(mt)

'''
output
<re.Match object; span=(0, 3), match='TAG'>
<re.Match object; span=(0, 3), match='TAG'>
'''


#re.findall -> to find all matching patterns in the string
import re 
seq=("TGAAGATGGGGCGATAGACGGGGTGCTAGATAGG")
x=re.findall(r"TAG",seq)    
print(x)

'''
output
['TAG', 'TAG', 'TAG']
'''

import re 
seq=("TGAAGATGGGGCGAACGGGGTGCAAGG")
x=re.findall(r"TAG",seq)    
print(x)

'''
output
[]
'''



#re.sub-to replace a word with another
import re 
string="Biotechnology tool"
replace=re.sub("Biotechnology","Bioinformatics",string)
print(replace)

'''
output
Bioinformatics tool
'''

import re
x='aaa@xxx.com bbb@yyy.com ccc@zzz.com'
print(re.sub('[a-z]*@','ABC@',x))    #[a-z] -> [a,b,c,....,x,y,z]
                                     #[a-z]*@ -> any letters before @ is replaced by ABC 

'''
output
ABC@xxx.com ABC@yyy.com ABC@zzz.com
'''

import re
x='aaa@xxx.com bbb@yyy.com ccc@zzz.com'
print(re.sub('[a-z]*@','ABC@',x,2))    #only first 2 locations are changed 

'''
output
ABC@xxx.com ABC@yyy.com ccc@zzz.com
'''

import re
x='aaa@xxx.com bbb@yyy.com ccc@zzz.com'
print(re.sub('[a-z]*@','ABC@',x,1))    #only first location is changed 

'''
output
ABC@xxx.com bbb@yyy.com ccc@zzz.com
'''

import re
x='aaa@xxx.com bbb@yyy.com ccc@zzz.com'
print(re.sub('[xyz]','1',x)) 

'''
output
aaa@111.com bbb@111.com ccc@111.com
'''

import re
x='aaa@xxx.com bbb@yyy.com ccc@zzz.com'
print(re.sub('[x-z]','1',x))    

'''
output
aaa@111.com bbb@111.com ccc@111.com
'''

import re
x='aaa@xxx.com bbb@yyy.com ccc@zzz.com'
print(re.sub('aaa|bbb|ccc','ABC',x)) 

'''
output
ABC@xxx.com ABC@yyy.com ABC@zzz.com
'''



#re.split() -> to split the string
import re
peptide="GJHJHYBAYHHXYJHBXAYHBJKA"
print(re.split(r'Y',peptide,maxsplit=2))

'''
output
['GJHJH', 'BA', 'HHXYJHBXAYHBJKA']
'''

import re
peptide="GJHJHYBAYHHXYJHBXAYHBJKA"
print(re.split(r'Y',peptide))

'''
output
['GJHJH', 'BA', 'HHX', 'JHBXA', 'HBJKA']
'''

import re
x=" one1two22three333four "
print(re.split(r'\d+',x))          #d -> digits (0-9)

'''
output
[' one', 'two', 'three', 'four ']
'''

import re
x=" one-two+three#four "
print(re.split(r'[-+#]',x)) 

'''
output
[' one', 'two', 'three', 'four ']
'''

import re
x=" oneXXXtwoYYYthreeZZZfour "
print(re.split(r'XXX|YYY|ZZZ',x))  

'''
output
[' one', 'two', 'three', 'four ']
'''

import re
x=" oneXXXtwoYYYthreeZZZfour "
print(re.split(r'XXX|YYY',x)) 

'''
output
[' one', 'two', 'threeZZZfour ']
'''



'''
Character         Description                                                                 Example
[]           A set of characters                                                              "[a-m]"
\            signals a special sequence (can also be used to escape special characters)       "\d"
.            any character (except newline character)                                         "he..o"
^            starts with                                                                      "^hello"
$            ends with                                                                        "world$"
*            zero or more occurances                                                          "aix*"
+            one or more occurances                                                           "aix+"
{}           exactly the specified number of occurrences                                      "al{2}"
|            Either or                                                                        "falls|stays"
()           capture or group