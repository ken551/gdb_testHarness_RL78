pyArg0 = gdb.execute("p $pyArg0", to_string=True)

funcName = (pyArg0.split("<")[1]).split(">")[0]

funcInfo = gdb.execute("info function "+funcName, to_string=True)
funcDef = funcInfo.split(".c:\n")[1]

#print "funcDef is:"
#print funcDef

returnType = funcDef.split(" ")[0]

#print "returnType is: "
#print returnType

args = (funcDef.split("(")[1]).split(")")[0]
#print "args are:"
#print args

# pass arg (to A register)
if args == "uint8_t":
    gdb.execute("set $a = $pyArg1")
elif args == "void":
    pass
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
    gdb.execute("set $funcReturn = $a")
elif returnType == "uint16_t":
    #pass return value as uint16_t
    gdb.execute("set $funcReturn = (uint16_t)$ax")
else:
    print "not working"