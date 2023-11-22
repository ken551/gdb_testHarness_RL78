cases = 0
assertNum = 0
assertResult = 0
fails = 0
oks = 0
testName = ""

gdb.execute("r")

# get backtrace info when in main()
btMain = gdb.execute("bt", to_string=True)

print ""
print "--------------------------"
print "test start\n"
gdb.execute("source tests\\testMacros.gdbcmd")
gdb.execute("source tests\\allTests.gdbcmd")
print "--------------------------"
print "test finished"

# casesStr = gdb.execute("p $cases", to_string=True)
# failsStr = gdb.execute("p $fails", to_string=True)
# cases = int((casesStr.split("= "))[1])
# fails = int((failsStr.split("= "))[1])
print str(cases) + " tests, " + str(fails) + " failed "
# gdb.execute('printf "%d tests, %d failed\\n", $cases, $fails')
if fails > 0:
    print "E000000: test result: NG "
else:
    print "test bresult: OK "
print "--------------------------"
# gdb.execute("q")