gdb.execute("set $assertNum = ($assertNum + 1)")
was = getIntFromGdb("was")
expected = getIntFromGdb("expected")
if expected != was:
    gdb.execute("set $assertResult = -1")
    gdb.execute("outputFailInfo")
    print "0x" + hex(expected) + " expected, was 0x" + hex(was)