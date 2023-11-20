gdb.execute("target sim")
gdb.execute("load")

gdb.execute("break main")

gdb.execute("r")

print "test start"
print "--------------------------"
gdb.execute("source tests\\testMacros.gdbcmd")
gdb.execute("source tests\\allTests.gdbcmd")
print "--------------------------"
print "test finished"

casesStr = gdb.execute("p $cases", to_string=True)
failsStr = gdb.execute("p $fails", to_string=True)
cases = int((casesStr.split("= "))[1])
fails = int((failsStr.split("= "))[1])
print str(cases) + " tests, " + str(fails) + " failed "
# gdb.execute('printf "%d tests, %d failed\\n", $cases, $fails')
if fails > 0:
    print "result: NG "
else:
    print "result: OK "
print "--------------------------"
gdb.execute("q")