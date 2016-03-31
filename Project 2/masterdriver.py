#   master driver file
#   Samuel Gluss
#   3/6/2016

from subprocess import call

pythonDriverPath = "pythondriver.py"
JSDriverPath = "JSDriver.py"
rubyDriverPath = "rubyDriver.py"
cppDriverPath = "cppdriver.py"
javaDriverPath = "javadriver.py"

#call(["python", pythonDriverPath])
#print "Python tests completed"
#call(["python", JSDriverPath], cwd="JS")
#print "JavaScript tests completed"
#call(["python", rubyDriverPath], cwd="ruby")
#print "Ruby tests completed"
call(["python", cppDriverPath])
print "C++ tests completed"
call(["python", javaDriverPath])
print "Java tests completed"

print "All tests completed"