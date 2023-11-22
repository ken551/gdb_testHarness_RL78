gdb.execute("set $assertNum = ($assertNum + 1)")
was = getIntVar("was")
expected = getIntVar("expected")
if expected != was:
    gdb.execute("set $assertResult = -1")
    gdb.execute("outputFailInfo")
    print "0x" + hex(expected) + " expected, was 0x" + hex(was)