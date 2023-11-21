# variables for test execution

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

def setRegValToGdb(reg, val):
    gdb.execute("set {uint8_t}" + hex(reg.addr) + " = " + str(val))

def callFunc(funcName, args):
    argc = len(args)
    gdb.execute("set $pyArg0 = " + funcName)
    i = 1
    for arg in args:
        gdb.execute("set $pyArg" + str(i) + " = " + str(arg))
        i = i + 1
    gdb.execute("source tests/funcCall.py")
    funcReturn = getValFromGdb("funcReturn")
    return funcReturn

def setValToGdb(varName, val):
    pass

def doTest(testFunc):
    # test start function
    global cases, assertNum, assertResult, fails, oks, testName
    cases = cases + 1
    assertNum = 0
    assertResult = True
    testName = testFunc.__name__

    setup()
    testFunc()
    teardown()

    # test end function
    if assertResult != True:
        fails = fails + 1
        print "E000000: testcase \"" + testName + "\" failed\n"
    else:
        oks = oks+1


# func for gdb controlling
def defTest():
    gdb.execute("set $cases = ($cases + 1)")
    gdb.execute("set $assertNum = 0")
    gdb.execute("set $assertResult = 0")

def intAssertEq(expected, was):
    global assertNum, assertResult
    assertNum = assertNum + 1
    if expected != was:
        gdb.execute("set $assertResult = -1")
        outputFailInfo()
        print hex(expected) + " expected, was " + hex(was)
        assertResult = False

def outputFailInfo():
    global assertNum, testName
    print "in test \"" + testName + "\""
    print "test assert no."+str(assertNum)+" failed!"

def regAssertEq(expected, reg):
    global assertNum, assertResult
    assertNum = assertNum + 1
    was = getRegValFromGdb(reg.name)
    if expected != was:
        assertResult = False
        outputFailInfo()
        print hex(expected) + " expected, was " + hex(was)

def testEnd():
    assertResult = getIntFromGdb("assertResult")
    if assertResult != 0:
        gdb.execute("set $fails = ($fails + 1)")
        testName = getValFromGdb("testName")
        testName = testName.replace("\n","")
        print "E000000: testcase " + testName + " failed\n"
    else:
        gdb.execute("set $oks = ($oks + 1)")