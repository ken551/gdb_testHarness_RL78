pyArg0 = gdb.execute("p $pyArg0", to_string=True)

funcName = (pyArg0.split("<")[1]).split(">")[0]

funcInfo = gdb.execute("info function "+funcName, to_string=True)
funcDef = funcInfo.split(".c:\n")[1]

isRegEmpty = {
    "A": True,
    "X": True,
    "C": True,
    "B": True,
    "E": True,
    "D": True,
}

def setUint8Arg(argName):
    global isRegEmpty
    if isRegEmpty["A"]:
        gdb.execute("set $a = (uint8_t)"+argName)
        isRegEmpty["A"] = False
    elif isRegEmpty["X"]:
        gdb.execute("set $x = (uint8_t)"+argName)
        isRegEmpty["X"] = False
    elif isRegEmpty["C"]:
        gdb.execute("set $c = (uint8_t)"+argName)
        isRegEmpty["C"] = False
    elif isRegEmpty["B"]:
        gdb.execute("set $b = (uint8_t)"+argName)
        isRegEmpty["B"] = False
    else:
        print "this feature is not implemented"

def setUint16Arg(argName):
    global isRegEmpty
    if isRegEmpty["A"] and isRegEmpty["X"]:
        gdb.execute("set $ax = (uint16_t)"+argName)
        isRegEmpty["A"] = False
        isRegEmpty["X"] = False
    elif isRegEmpty["B"] and isRegEmpty["C"]:
        gdb.execute("set $bc = (uint16_t)"+argName)
        isRegEmpty["B"] = False
        isRegEmpty["C"] = False
    elif isRegEmpty["D"] and isRegEmpty["E"]:
        gdb.execute("set $de = (uint16_t)"+argName)
        isRegEmpty["D"] = False
        isRegEmpty["E"] = False
    else:
        print "this feature is not implemented"

# print "funcDef is:"
# print funcDef

returnType = funcDef.split(" ")[0]

#print "returnType is: "
#print returnType

args = (funcDef.split("(")[1]).split(")")[0]
# print "args are:"
# print args

argArray = args.split(", ")

# pass arg (to A register)
i = 1
for arg in argArray:
    if arg == "uint8_t":
        setUint8Arg("$pyArg"+str(i))
    if arg == "uint16_t":
        setUint16Arg("$pyArg"+str(i))
    elif arg == "void":
        pass
    i = i + 1
# make function call frame on stack
gdb.execute("set $sp = $sp-1")
gdb.execute("set *( (char *)( (((int)$sp) & 0x000FFFFF) ) ) = 0x00")
gdb.execute("set $sp = $sp-1")
gdb.execute("set *( (char *)( (((int)$sp) & 0x000FFFFF) ) ) = 0x00")
gdb.execute("set $sp = $sp-1")
gdb.execute("set *( (char *)( (((int)$sp) & 0x000FFFFF) ) ) = (char)$main_msb")
gdb.execute("set $sp = $sp-1")
gdb.execute("set *( (char *)( (((int)$sp) & 0x000FFFFF) ) ) = (char)$main_lsb")
# do function call (change PC value)
gdb.execute("set $pc = (int)($pyArg0)")
gdb.execute("continue")

# set return value
if returnType == "void":
    pass
elif returnType == "uint8_t":
    # pass return value as uint8_t
    gdb.execute("set $funcReturn = (uint8_t)$a")
elif returnType == "uint16_t":
    #pass return value as uint16_t
    gdb.execute("set $funcReturn = (uint16_t)$ax")
else:
    print "not working"