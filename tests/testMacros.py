# variables for test execution

# func for python <-> gdb interface
def getGdbStrVar(varName):
    tmp = gdb.execute("p $"+varName, to_string=True)
    tmp = (tmp.split("= "))[1]
    return tmp

def getGdbIntVar(varName):
    tmp = getIntVar("$"+varName)
    return tmp

def getRegVal(addrVarName):
    tmp = gdb.execute("x/b $"+addrVarName, to_string=True)
    tmp = tmp.split("\t")[1]
    tmp = int(tmp)
    return tmp

def setRegVal(reg, val):
    gdb.execute("set {uint8_t}" + hex(reg.addr) + " = " + str(val))

def setIntVar(varName, val):
    gdb.execute("set var "+varName+"="+str(val))

def getIntVar(varName):
    tmp = gdb.execute("p/d "+varName, to_string=True)
    tmp = (tmp.split("= "))[1]
    tmp = int(tmp)
    return tmp

def getIntArrayVar(varName, index):
    tmp = getIntVar(varName + "[" + str(index) + "]")
    return tmp

def setStub(funcName):
    gdb.execute("tbreak "+funcName)


def callFunc(funcName, args):
    argc = len(args)
    gdb.execute("set $pyArg0 = " + funcName)
    i = 1
    for arg in args:
        gdb.execute("set $pyArg" + str(i) + " = " + str(arg))
        i = i + 1
    gdb.execute("source tests/funcCall.py")

    funcInfo = gdb.execute("info function "+funcName, to_string=True)
    funcDef = funcInfo.split(".c:\n")[1]
    returnType = funcDef.split(" ")[0]

    # set return value
    if returnType == "void":
        pass
    elif returnType == "uint8_t":
        # pass return value as uint8_t
        return getIntVar("(uint8_t)$a")
    elif returnType == "uint16_t":
        #pass return value as uint16_t
        return getIntVar("(uint16_t)$ax")
    else:
        print "not working"

def setFuncReturn(type, val):
    if type == "void":
        pass
    elif type == "uint8_t":
        gdb.execute("set $a="+str(val))
    else:
        print "this feature is not implemented"

def doTest(testFunc):
    # test start function
    global cases, assertNum, assertResult, fails, oks, testName
    cases = cases + 1
    assertNum = 0
    assertResult = True
    testName = testFunc.__name__
    print "executing test \"" + testName + "\"..."

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

def assertEq(expected, was):
    global assertNum, assertResult, testName
    assertNum = assertNum + 1
    if expected != was:
        assertResult = False
        print "in test \"" + testName + "\""
        print "test assert no."+str(assertNum)+" failed!: " + hex(expected) + " expected, was " + hex(was)+"\n"

def intAssertEq(expected, was):
    assertEq(expected, was)

def regAssertEq(expected, reg):
    was = getRegVal(reg.name)
    assertEq(expected, was)