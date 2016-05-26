import math
def __isIN(i, ty):
	try:
		ty(i)
		return True
	except:
		return False
def __get(i, data, var):
    isINT = __isIN(i, int)
    isFLOAT = __isIN(i, float)
    isSTRING = __isIN(i, str)
    if isINT == True:
	    i = int(i)
    elif isFLOAT == True:
	    i = float(i)
    elif isSTRING == True and var == True:
        if "%" in i:
            ni = []
            i = i.split(" ")
            for l in i:
                if len(l) > 1 and l[0] == "%":
                    try:
                        l = list(l)
                        l[0] = ""
                        l = "".join(l)
                        if "." in l:
                            varn = l.split(".")
                            num = 0
                            t = data[__get(varn[num], data, var)]
                            while num != len(varn) - 1:
                                num += 1
                                try:
                                    t = t[__get(varn[num], data, var)]
                                except:
                                    print "ERROR, ITEM DOESN'T EXIST"
                                    break
                                
                        else:
                            t = data[l]
                        if len(i) == 1:
                            ni.append(t)
                        else:
                            ni.append(str(t))  
                    except:
                        ni.append("%" + l)
                else:
                    ni.append(l)
            i = ni[0] if len(i) == 1 else " ".join(ni)
    return i
def __ch(li, num):
    try:
        return li[num]
    except:
        return ""
def __add(a, b):
    return a + b
def __min(a, b):
    return a - b
def __div(a, b):
    return a / b
def __mul(a, b):
    return a * b
def __pow(a, b):
    return a ** b
OPERATORS = {
    "+":__add,
    "-":__min,
    "/":__div,
    "*":__mul,
    "^":__pow
}
def __isOperator(op, var):
    if var == False:
        return False
    try:
        OPERATORS[op]
        return True
    except:
        return False
def __ld(filename, var):
    with open(filename, 'r') as infile:
        line = ''
        while True:
            while not line.startswith('#'):
                line = infile.next()
                continue
            data = {}
            main_key = ""
            block = ""
            last_line = ""
            array = False
            statement = False
            for line in infile:
                line = line.strip()
                if line:
                    try:
                        key, value = map(str.strip, line.split(':', 1))
                    except:
                        key = line
                        value = line
                    if line.startswith('--'):
                        key = list(key)
                        key[0] = ""
                        key[1] = ""
                        key = "".join(key)
                        if statement == True or array == True:
                            value = list(value)
                            value[0] = ""
                            value[1] = ""
                            value = "".join(value)
                        key = __get(key, data, var)
                        value = __get(value, data, var) if statement == False else value
                        if value == "INPUT":
                            value = __get(raw_input(key + '> '), data, var)
                        if array == False and statement == False:
                            data[main_key][key] = value
                        elif len(key) > 0 and statement == False:
                            data[main_key].append(value)
                        elif statement == False:
                            data[main_key].append(value)
                        elif statement == True and var == True:
                            i = []
                            word = ""
                            end = 0
                            for c in value:
                                if __isOperator(c, var) == True:
                                    if word != "":
                                        i.append(__get(word, data, var))
                                        word = ""
                                    i.append(c)
                                elif c != ' ':
                                    word = word + c
                            if word != "":
                                i.append(__get(word, data, var))
                                word = ""
                            num = 0
                            new = i
                            i = 0
                            first = True
                            for c in new:
                                next = i + 1
                                last = i - 1
                                if __isOperator(c, var) == True:
                                    if first == True:
                                        num = OPERATORS[c](__ch(new, last),__ch(new, next))
                                        first = False
                                    else:
                                        num = OPERATORS[c](num,__ch(new, next))
                                i += 1
                            data[main_key] = num
                        elif statement == True and var == False:
                            data[main_key] = value
                    elif value != "":
                        key = __get(key, data, var)
                        value = __get(value, data, var)
                        if key == "PRINT":
                            print value
                        elif value == "INPUT":
                            data[key] =  __get(raw_input(key + '> '), data, var)
                        else:
                            data[key] = value
                        array = False
                        statement = False
                    else:
                        array = False
                        statement = False
                        try:
                            k = key.split(" ", 1)
                            main_key = __get(k[1], data, var)
                            if k[0] == "ARRAY":
                                data[main_key] = []
                                array = True
                            elif k[0] == "DICT":
                                data[main_key] = {}
                            elif k[0] == "STATE":
                                data[main_key] = ""
                                statement = True
                        except:
                            key = __get(key, data, var)
                            data[key] = {}
                    last_line = line
            yield data
def load(filename, VARS=True):
    for section in __ld(filename, VARS):
        return section
def __iS(statement):
    try:
        for s in statement:
            if __isOperator(s, True) == True:
                return True
    except:
        dn = ""
    return False    
def _____________dump(data, filename):
    text = ""
    for d in data:
        isDict = __isIN(data[d], dict)
        isArray = isinstance(data[d], (list, tuple))
        isStatement = __iS(data[d])
        if isDict == True:
            text += "DICT " + d + ":\n"
            for dd in data[d]:
                text += "--" + dd + ":" + str(data[d][dd]) + "\n"
        elif isArray == True:
            text += "ARRAY " + d + ":\n"
            for dd in data[d]:
                text += "--" + str(dd) + "\n"
        elif isStatement == True:
            text += "STATE " + d + ":\n--" + data[d] + "\n" 
        else:
            text += d + ":" + str(data[d])
        text += "\n"
    return open(filename, "w").write(text)
