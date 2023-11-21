# cases = 0
# fails = 0
# oks = 0
# gdb.execute("set print symbol off")
# gdb.execute("set print elements 0")

# gdb.execute("set $main = (int)&main")
# gdb.execute("set $main_lsb = (char)($main & 0x000000FF)")
# gdb.execute("set $main_msb = (char)(($main & 0x0000FF00) >> 8)")

# def outputFailInfo():
#     tmp = gdb.execute("p $testName", to_string=True)
#     testName = (tmp.split("= "))[1]
#     tmp = gdb.execute("p $assertNum", to_string = True)
#     assertNum = int((tmp.split("= "))[1])
#     print "in " + testName
#     print "!!!!!!!!test assert no."+str(assertNum)+" failed!!!!!!"

# func for python <-> gdb interface
def getValFromGdb(varName):
    tmp = gdb.execute("p $"+varName, to_string=True)
    tmp = (tmp.split("= "))[1]
    return tmp

def setValToGdb(varName, val):
    pass