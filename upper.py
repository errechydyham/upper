#get the file name 
name = input("Enter file name: ")
text = open(name, "r") 

#print each line in an uppercase format 
for line in text: 
    print(line.upper())