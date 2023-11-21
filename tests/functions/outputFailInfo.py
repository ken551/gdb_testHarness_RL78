tmp = gdb.execute("p $testName", to_string=True)
testName = (tmp.split("= "))[1]
testName = testName.replace("\\000",'')
testName = testName.replace("\n",'')
tmp = gdb.execute("p $assertNum", to_string = True)
assertNum = int((tmp.split("= "))[1])
print "in test " + testName
print "!!!!!!!!test assert no."+str(assertNum)+" failed!!!!!!"