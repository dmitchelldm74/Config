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
                            varn = l.rsplit(".", 1)
                            t = data[varn[0]][__get(varn[1], data, var)]
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
            for line in infile:
                line = line.strip()
                if line:
                    key, value = map(str.strip, line.split(':', 1))
                    if line.startswith('--'):
                        key = list(key)
                        key[0] = ""
                        key[1] = ""
                        key = "".join(key)
                        if array == False:
                            data[main_key][key] = __get(value, data, var)
                        elif len(key) > 0:
                            data[main_key].append(__get(key, data, var))
                        else:
                            data[main_key].append(__get(value, data, var))
                    elif value != "":
                        data[key] = __get(value, data, var)
                        array = False
                    else:
                        try:
                            k = key.split(" ", 1)
                            main_key = k[1]
                            if k[0] == "ARRAY":
                                data[k[1]] = []
                                array = True
                            elif k[0] == "DICT":
                                data[k[1]] = {}
                                array = False
                        except:
                            key = key
                            data[key] = {}
                    last_line = line
            yield data
def load(filename, VARS=True):
    for section in __ld(filename, VARS):
        return section
def dump(data, filename):
    text = ""
    for d in data:
        isDict = __isIN(data[d], dict)
        isArray = isinstance(data[d], (list, tuple))
        if isDict == True:
            text += "DICT " + d + ":\n"
            for dd in data[d]:
                text += "--" + dd + ":" + str(data[d][dd]) + "\n"
        elif isArray == True:
            text += "ARRAY " + d + ":\n"
            for dd in data[d]:
                text += "--:" + str(dd) + "\n"
        else:
            text += d + ":" + str(data[d])
        text += "\n"
    return open(filename, "w").write(text)
