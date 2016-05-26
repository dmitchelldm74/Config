#Config: A Simple Way to store Data
**In Config you must provide a key (this will come in handy in your code) and a value**
Example:```KEY:VALUE```
**To create a dictionary, first put the keyname and then -- on every line below the keyname you want in the dict. (you can't skip a line)**
Example:
```
DICT keyname:
--key:value
```
**To create an Array/List, first put the keyname and then -- on every line below the keyname you want in the Array. (you can't skip a line)**
```
ARRAY keyname:
--:value
```
**To make a variable put a % sign in front of the value**
Example:
```
key:value
key2:%key
```
**Would give key2 the value of key**
##For more **INFO** check the "config.cfg" file
```
# entry 1
ID:01
VOLUME:0.1001
DICT CONTENT:
--l1:the volume is %VOLUME
--l2:%VOLUME
#is a comment
ARRAY arr:
--:Item
--:%ID
not:in %CONTENT.l1
another:%arr.1
```

## When using python there is a module to load data (config.py) AN EXAMPLE USAGE IS LOCATED IN "test.py"
