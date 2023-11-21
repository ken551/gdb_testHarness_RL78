testName = getValFromGdb("testName")
testName = testName.replace("\\000",'')
testName = testName.replace("\n",'')
assertNum = getIntFromGdb("assertNum")
print "in test " + testName
print "!!!!!!!!test assert no."+str(assertNum)+" failed!!!!!!"