testName = getValFromGdb("testName")
testName = testName.replace("\\000",'')
testName = testName.replace("\n",'')
assertNum = getIntFromGdb("assertNum")
print "E000000: in test " + testName
print "E000000: test assert no."+str(assertNum)+" failed!"