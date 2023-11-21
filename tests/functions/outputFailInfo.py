testName = getValFromGdb("testName")
testName = testName.replace("\\000",'')
testName = testName.replace("\n",'')
assertNum = int(getValFromGdb("assertNum"))
print "in test " + testName
print "!!!!!!!!test assert no."+str(assertNum)+" failed!!!!!!"