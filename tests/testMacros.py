
# func for python <-> gdb interface
def getValFromGdb(varName):
    tmp = gdb.execute("p $"+varName, to_string=True)
    tmp = (tmp.split("= "))[1]
    return tmp

def getIntFromGdb(varName):
    tmp = gdb.execute("p/d $"+varName, to_string=True)
    tmp = (tmp.split("= "))[1]
    tmp = int(tmp)
    return tmp

def getRegValFromGdb(addrVarName):
    tmp = gdb.execute("x/b $"+addrVarName, to_string=True)
    tmp = tmp.split("\t")[1]
    tmp = int(tmp)
    return tmp

def setValToGdb(varName, val):
    pass


# func for gdb controlling
def defTest():
    gdb.execute("set $cases = ($cases + 1)")
    gdb.execute("set $assertNum = 0")
    gdb.execute("set $assertResult = 0")

def intAssertEq():
    gdb.execute("set $assertNum = ($assertNum + 1)")
    was = getIntFromGdb("was")
    expected = getIntFromGdb("expected")
    if expected != was:
        gdb.execute("set $assertResult = -1")
        gdb.execute("outputFailInfo")
        print "0x" + hex(expected) + " expected, was 0x" + hex(was)

def outputFailInfo():
    testName = getValFromGdb("testName")
    testName = testName.replace("\\000",'')
    testName = testName.replace("\n",'')
    assertNum = getIntFromGdb("assertNum")
    print "E000000: in test " + testName
    print "E000000: test assert no."+str(assertNum)+" failed!"

def regAssertEq():
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

def testEnd():
    assertResult = getIntFromGdb("assertResult")
    if assertResult != 0:
        gdb.execute("set $fails = ($fails + 1)")
        testName = getValFromGdb("testName")
        testName = testName.replace("\n","")
        print "E000000: testcase " + testName + " failed\n"
    else:
        gdb.execute("set $oks = ($oks + 1)")