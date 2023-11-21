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
    setRegValToGdb(P4, 0xFF)
    callFunc("initPort4", [])
    regAssertEq(0, P4)

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

# write tests below
doTest(LED_init)
doTest(four_u8)
doTest(three_u16)