assertResult = getIntFromGdb("assertResult")
if assertResult != 0:
    gdb.execute("set $fails = ($fails + 1)")
    testName = getValFromGdb("testName")
    testName = testName.replace("\n","")
    print "E000000: testcase " + testName + " failed\n"
else:
    gdb.execute("set $oks = ($oks + 1)")