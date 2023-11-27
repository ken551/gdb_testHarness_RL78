def setup():
    pass

def teardown():
    pass

class Reg:
    name = ""
    addr = 0
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

P4 = Reg("P4", 0xFFF04)

def LED_init():
    setRegVal(P4, 0xFF)
    callFunc("initPort4", [])
    regAssertEq(0, P4)

def turnon1():
    setRegVal(P4, 0x00)
    callFunc("toggleLed", [0])
    regAssertEq(0x04, P4)


def turnon2():
    setRegVal(P4, 0x00)
    callFunc("toggleLed", [1])
    regAssertEq(0x08, P4)

def toggle():
    setRegVal(P4, 0x00)

    # LED ON
    callFunc("toggleLed", [0])
    regAssertEq(0x04, P4)

    # LED OFF
    callFunc("toggleLed", [0])
    regAssertEq(0x00, P4)

def returnTest():
    ret = callFunc("returnTest", [1])
    intAssertEq(2, ret)

    ret = callFunc("returnTest", [0])
    intAssertEq(1, ret)

    ret = callFunc("returnTest", [130])
    intAssertEq(131, ret)

def beefTest():
    ret = callFunc("returnBeef", [])
    intAssertEq(0xBEEF, ret)

def twoArgs():
    ret = callFunc("twoArgs", [1,1])
    intAssertEq(3, ret)

    ret = callFunc("twoArgs", [2,1])
    intAssertEq(5, ret)

    ret = callFunc("twoArgs", [1,2])
    intAssertEq(4, ret)

def twoUint16():
    ret = callFunc("twoUint16s", [1,2])
    intAssertEq(4, ret)

    ret = callFunc("twoUint16s", [0x0F00, 0x0F01])
    intAssertEq(0x2D01, ret)

    ret = callFunc("twoUint16s", [0x0F01, 0x0F00])
    intAssertEq(0x2D02, ret)

def u16_u8():
    ret = callFunc("u16_u8", [1,2])
    intAssertEq(4,ret)

    ret = callFunc("u16_u8", [0x0F00, 1])
    intAssertEq(0x1e01, ret)

    ret = callFunc("u16_u8", [0x0F01, 2])
    intAssertEq(0x1e04, ret)

def u8_u16():
    ret = callFunc("u8_u16", [1,2])
    intAssertEq(4, ret)

    ret = callFunc("u8_u16", [1, 0x0F00])
    intAssertEq(0x0F02, ret)

    ret = callFunc("u8_u16", [2, 0x0F01])
    intAssertEq(0x0F05, ret)

def four_u8():
    ret = callFunc("four_u8", [1,2,3,4] )
    intAssertEq(20, ret)

    ret = callFunc("four_u8", [4,3,2,1])
    intAssertEq(30, ret)

def three_u16():
    ret = callFunc("three_u16", [0x1111, 0x2222, 0x3333])
    intAssertEq(0xaaaa, ret)

    ret = callFunc("three_u16", [0x3333, 0x2222, 0x1111])
    intAssertEq(0xeeee, ret)

def multiply():
    setIntVar("multiplier", 0)
    ret = callFunc("multiply", [5])
    intAssertEq(0, ret)

    setIntVar("multiplier", 1)
    ret = callFunc("multiply",[5])
    intAssertEq(5,ret)

    setIntVar("multiplier", 2)
    ret = callFunc("multiply", [5])
    intAssertEq(10, ret)

    setIntVar("multiplier",0xFF)
    ret = callFunc("multiply", [5])
    intAssertEq(0x4fb, ret)

    setIntVar("multiplier", 2)
    ret = callFunc("multiply", [0xFF])
    intAssertEq(0x1FE, ret)

def setArray():
    setIntVar("multiplier", 1)
    for i in range(10):
        setIntArrayVar("hogeArray", i, 0xaa)
    callFunc("setArray",[])
    for i in range(10):
        res = getIntArrayVar("hogeArray", i)
        intAssertEq((i+1), res)

def testStub():
    receiveArgs = {}
    receiveArgs["hoge"]=0xAA

    setStub("caller", receiveArgs, 10)

    ret = callFunc("callee",[2])

    intAssertEq(2, receiveArgs["hoge"])
    intAssertEq(20, ret)

# write tests below
doTest(LED_init)
doTest(turnon1)
doTest(turnon2)
doTest(toggle)
doTest(returnTest)
doTest(beefTest)
doTest(twoArgs)
doTest(twoUint16)
doTest(u16_u8)
doTest(u8_u16)
doTest(four_u8)
doTest(three_u16)
doTest(multiply)
doTest(setArray)
doTest(testStub)