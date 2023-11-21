def setup():
    pass

def teardown():
    pass

def four_u8():
    ret = callFunc(four_u8, [1,2,3,4] )
    intAssertEq(20, ret)

    ret = callFunc(four_u8, [4,3,2,1])
    intAssertEq(3, ret)

def three_u16():
    ret = callFunc(three_u16, [0x1111, 0x2222, 0x3333])
    intAssertEq(0xaaa, ret)

    ret = callFunc(three_u16, [0x3333, 0x2222, 0x1111])
    intAssertEq(0xeeee, ret)

# write tests below
doTest(four_u8)
doTest(three_u16)