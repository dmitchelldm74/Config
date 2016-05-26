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
Example:
```
ARRAY keyname:
--value
```
**To state something (math or string), first put the keyname and then -- on a line below the keyname (you can't skip a line)**
Example:
```
STATE keyname:
--6 * 7
STATE keyname:
--%string1 + %string2
```
Note: *it is best to user variables when adding strings together since spaces will be messed up*
#Valid Signs:
        +: adds numbers together
        -: subtracts numbers
        *: multiplies numbers
        /: divides numbers
        ^: to the power of
**To print something first put PRINT then what you want to print**
Example:
```
PRINT:what you want to print
```
**To get Input from the user put the keyname then INPUT after**
Example:
```
name:INPUT
```
*Note: You can't put any other text with INPUT or it won't recognize it as a prompt for the user*
**To use a variable put a % sign in front of the value**
Example:
```
key:value
key2:%key
```
**Would give key2 the value of key**
**FOR DICTS**
```
DICT user:
--name:Daniel
--password:****
--email:dmitchell.dm74@gmail.com
current_user:%user.name
```
*"current_user" would then equal "Daniel"*
**FOR ARRAYS**
```
ARRAY numbers:
--zero
--one
--two
--three
--four
current_number:%numbers.0
```
*"current_number" would then equal "zero"*
*Config is 0 indexed so in an ARRAY, the first member of the ARRAY has an id of 0 the next member has an id of 1 and so on*
[MORE ABOUT ARRAYS](https://en.wikipedia.org/wiki/Array)
##For more **INFO** check the "config.cfg" file
```
# entry 1
ID:01
VOLUME:0.1001
DICT CONTENT:
--l1:the volume is %VOLUME
--l2:%VOLUME
ARRAY arr:
--Item
--%ID
not:in %CONTENT.l1
another:%arr.1
test:INPUT
PRINT:hello, %CONTENT.l1
STATE a:
--%ID + %VOLUME
STATE b:
--%ID + %ID ^ 3
STATE c:
--80 * 34 / 2
STATE d:
--80 - 79
```

## When using python there is a module to load data (config.py) AN EXAMPLE USAGE IS LOCATED IN "test.py"
