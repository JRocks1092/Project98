file1 = open("text1.txt", "r")
file2 = open("txt2.txt", "r")

fileLine1 = file1.read()
fileLine2 = file2.read()

file1.close()
file2.close()

fileWrite1 = open("text1.txt", "w")
fileWrite1.write(fileLine2)
fileWrite1.close()

fileWrite2 = open("txt2.txt", "w")
fileWrite2.write(fileLine1)
fileWrite2.close()