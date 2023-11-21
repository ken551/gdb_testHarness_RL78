gdb.execute("set $assertNum = ($assertNum + 1)")
gdb.execute("set $assertResult = 0")
expected = getIntFromGdb("expected")
readResult = getRegValFromGdb("addr")
if expected == readResult:
    gdb.execute("set $assertResult = 0")
else:
    gdb.execute("set $assertResult = -1")
    gdb.execute("outputFailInfo")
    print str(expected) + " expected, was " + str(readResult)