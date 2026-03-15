file = open("sample.txt", "w")
file.write("mani\n")

lines = ["mani\n", "D.O.B-7-10-2005\n", "College - MVGR\n"]
file.writelines(lines)

file.close()

file = open("sample.txt", "r")
print("read()\n:")
print(file.read())     
file.close()

file = open("sample.txt", "r")
print("\nreadline()\n:")
print(file.readline()) 
print(file.readline()) 
file.close()

file = open("sample.txt", "r")
print("\nreadlines():")
print(file.readlines()) 
file.close()
