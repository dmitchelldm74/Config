def sub(string, substitute="%"):
    li = string.split(" ")
    nli = []
    tsub = ""
    exceptions = ".:;,!'\"?"
    for s in li:
        if len(s) != 0 and s[0] == substitute or len(s) != 0 and s[0] == "\n" and s[1] == substitute:
            s = list(s)
            if s[0] == "\n":
                nli.append("\n")
                s[1] = ""
            s[0] = ""
            if len(s) != 0 and s[len(s) - 1] in exceptions:
                tsub = s[len(s) - 1]
                s[len(s) - 1] = ""
            s = "".join(s)
            try:
                exec("ta = " + s)
                ta = ta if tsub == "" else ta + tsub
                nli.append(ta)
            except:
                ta = substitute + s
                ta = ta if tsub == "" else ta + tsub
                nli.append(ta)
            tsub = ""
        else:
            nli.append(s)
    text = ""
    sn = False
    i = 0
    for n in nli:
        if n == "\n":
            sn = True
        elif sn == False and i != 0:
            text += " "
        else:
            sn = False
        text += n
        i += 1
    return text
greetings = "hello"
person = "Daniel"
From = "Anna"
isCool = "it is"
data = {"name":"Daniel", "password":"****"}
print sub("%greetings %person, I am %From \nIs this cool? %isCool! \n%data['password']")
